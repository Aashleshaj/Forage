1. Project Overview
This project is a prototype web-based AI chatbot designed to provide instant financial insights based on SEC 10-K filings. Built using Python, Pandas, and the Streamlit framework, the chatbot allows users to query specific financial metrics (Revenue, Net Income, and Operating Cash Flow) for major technology companies (Apple, Microsoft, and Tesla) across recent fiscal years.

2. Core Functionality
Interactive Web Interface: Utilizes Streamlit to provide a modern, chat-based User Interface (UI) where users can seamlessly type questions and read formatted responses.

Data-Driven Responses: Connects to a local, structured dataset (Financial_Data.csv) using the Pandas library, ensuring all financial figures returned are accurate and grounded in verified data rather than AI hallucinations.

State Management (Context Memory): Employs Streamlit's session_state to remember the context of the conversation. If a user asks a broad question (e.g., "What is the total revenue?"), the bot will pause, ask which company the user means, remember that interaction, and process the user's subsequent reply correctly.

Supported Queries: The chatbot is programmed to accurately route and answer the following predefined intents:

Total Revenue inquiries (e.g., "What is Microsoft's total revenue?")

Net Income inquiries (e.g., "What is the net income for Tesla?")

Year-over-Year calculations (e.g., "How has Apple's net income changed?")

Comparative metrics (e.g., "Which company had the highest cash flow?")

3. Known Limitations
As a streamlined prototype, the chatbot has several purposeful limitations:

Rule-Based Logic (No NLP): The bot relies on hardcoded if/elif statements and strict keyword matching (e.g., looking for the exact phrase "net income change"). It lacks advanced Natural Language Processing (NLP) or Large Language Model (LLM) integrations, meaning it cannot understand complex phrasing, spelling errors, or questions outside its programmed scope.

Static Dataset: The application relies on a static .csv file. It does not currently feature API integration to automatically fetch real-time data or new SEC filings from the web.

Limited Scope: The database is currently restricted to three specific companies (AAPL, MSFT, TSLA) and primarily covers the fiscal years 2024 and 2025.

4. How to Run the Application
- Ensure Python is installed on your machine.
- Install the required libraries via the terminal: pip install streamlit pandas
- Ensure app.py and data.csv are in the same directory.
- Run the application from the terminal: streamlit run app.py