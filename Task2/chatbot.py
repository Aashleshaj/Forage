import streamlit as st
import pandas as pd


# @st.cache_data ensures the CSV is only loaded once, making the app much faster
@st.cache_data 
def load_data():
    try:
        return pd.read_csv('data.csv')
    except FileNotFoundError:
        st.error("CRITICAL ERROR: 'data.csv' not found.")
        return pd.DataFrame()

df = load_data()
# A simple dictionary to map our chatbot's internal terms to the exact CSV column headers
metric_map = {
    "revenue": "Total Revenue",
    "net_income": "Total Income",
    "operating_cash_flow": "Operating Cash flow"
}

# logic to analyze financial data and generate insights
def get_financial_data(company, metric, year):
    if df.empty: 
        return "Database error: CSV file missing."
    
    #Here, metric would be the user-friendly term (like "revenue") that was passed to the function. 
    #The .get() method of the dictionary looks up this metric in our metric_map
    col_name = metric_map.get(metric)
    #It takes the metric (e.g., "revenue") provided by the Chatbot Query Resolver and looks up its 
    #corresponding technical column name (e.g., "Total Revenue") in the metric_map dictionary.

    # Filter the DataFrame for the specific company and year
    result = df[(df['Company Name'].str.lower() == company.lower()) & (df['Fiscal Year'] == year)]
    if not result.empty:
        # Extract the specific value from the matched row
        value = int(result.iloc[0][col_name])
        return f"${value:,} Million"
    return "Data not available."

def calculate_net_income_change(company, start_year, end_year):
    if df.empty: 
        return "Database error: CSV file missing."
    
    # Filter for the specific company first
    comp_df = df[df['Company Name'].str.lower() == company.lower()]
    
    # Find the rows for the start and end years
    start_data = comp_df[comp_df['Fiscal Year'] == start_year]
    end_data = comp_df[comp_df['Fiscal Year'] == end_year]
    
    if not start_data.empty and not end_data.empty:
        old_val = int(start_data.iloc[0]['Total Income'])
        new_val = int(end_data.iloc[0]['Total Income'])
        
        direction = "increased" if new_val > old_val else "decreased"
        return f"{direction} from ${old_val:,} Million in {start_year} to ${new_val:,} Million in {end_year}"
        
    return "Data not available to calculate change."

def find_highest_cash_flow(year):
    if df.empty: return "Database error: CSV file missing."
    
    # Filter the DataFrame to only show rows for the requested year
    year_df = df[df['Fiscal Year'] == year]
    
    if not year_df.empty:
        # Find the index of the row with the maximum cash flow
        max_index = year_df['Operating Cash flow'].idxmax()
        # Extract the data from that specific row
        max_row = year_df.loc[max_index]
        
        company = max_row['Company Name']
        max_val = int(max_row['Operating Cash flow'])
        
        return f"{company} at ${max_val:,} Million"
        
    return "Data not available for that year."

# function definition and cleaning the input
def simple_chatbot(user_query):
    query = user_query.strip().lower()

    #After get_financial_data returns the raw revenue figure (like "$245,000 Million"), 
    #simple_chatbot uses an f-string to combine this result into a complete, user-friendly sentence.'''
    if query == "what is microsoft's total revenue for 2025?":
        result = get_financial_data("microsoft", "revenue", 2025)
        return f"Microsoft's total revenue for FY 2025 was {result}."
    
    elif query == "what is apple's total revenue for 2025?":
        result = get_financial_data("Apple", "revenue", 2025)
        return f"Apple's total revenue for FY 2025 was {result}."
    
    elif query == "what is tesla's total revenue for 2025?":
        result = get_financial_data("Tesla", "revenue", 2025)
        return f"Tesla's total revenue for FY 2025 was {result}."
    
    # calculate_net_income_change is called with the company name and the two years to compare. 
    # It returns a string like "increased from $X Million in 2024 to $Y Million in 2025", which is then 
    # embedded into a complete sentence for the user.

    elif query == "how has apple's net income changed from 2024 to 2025?":
        result = calculate_net_income_change("apple", 2024, 2025)
        return f"Apple's net income {result}."
    
    # ''' find_highest_cash_flow is called with the year as an argument. It returns a string like 
    # s"CompanyName at $X Million", which is then used to construct the final response.'''
    elif query == "which company had the highest operating cash flow in 2025?":
        result = find_highest_cash_flow(2025)
        return f"The highest operating cash flow in 2025 was {result}."

    elif query == "what is tesla's net income for 2025?":
        result = get_financial_data("Tesla", "net_income", 2025)
        return f"Tesla's net income for FY 2025 was {result}."

    elif query == "what is apple's net income for 2025?":
        result = get_financial_data("apple", "net_income", 2025)
        return f"Apple's net income for FY 2025 was {result}."
    
    elif query == "what is microsoft's net income for 2025?":
        result = get_financial_data("microsoft", "net_income", 2025)
        return f"Microsoft's net income for FY 2025 was {result}."
        
    else:
        return "Sorry, I can only provide information on the predefined queries."

# Streamlit UI
st.title("📈 Financial AI Chatbot")

# Sidebar for the menu
with st.sidebar:
    st.header("Available Queries")
    st.markdown("""
    You can ask me exactly:
    1. What is Microsoft's total revenue for 2025?
    2. What is Apple's total revenue for 2025?
    3. What is Tesla's total revenue for 2025?
    4. How has Apple's net income changed from 2024 to 2025?
    5. Which company had the highest operating cash flow in 2025?
    6. What is Tesla's net income for 2025?
    7. What is Apple's net income for 2025?
    8. What is Microsoft's net income for 2025?
    """)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Ask me one of the financial queries from the sidebar."}
    ]

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# creates the text input box at the bottom. When the user types something and presses Enter, 
# their text is stored in the prompt variable, and the code inside the if block runs.
if prompt := st.chat_input("Type your query here..."):
    # we add this user message to our st.session_state.messages list so it's remembered.
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Get chatbot response
    response = simple_chatbot(prompt)

    # 3. Display bot response and save it to history
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})