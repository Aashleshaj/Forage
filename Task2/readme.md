Financial AI Chatbot designed to act as a personal financial analyst. It allows users to ask specific questions about companies' financial performance, such as their revenue or net income, for different years. The chatbot retrieves this information from a centralized financial data model and provides clear, quick answers through an interactive chat interface, while also maintaining a visual history of the conversation.

It's built using a magical Python library called Streamlit. Its main job is to create the visual "conversation room" where users can talk to the chatbot. Without it, our powerful financial brain wouldn't have a way to communicate with anyone!

Key Features of Our Chat Interface
Our chat interface has a few main components, all powered by Streamlit:

The Chatbot's "Welcome Mat": The Title and Sidebar
This sets the stage, giving our chatbot a name and a clear purpose.
The sidebar acts like a helpful menu, showing you what the chatbot can do or examples of questions you can ask.
The "Conversation Scroll": Displaying Past Messages
Just like scrolling through a text message history, our interface shows all the previous turns in the conversation.
It clearly labels who said what (you or the chatbot).
The "Speaking Tube": The Input Box
This is where you type your questions. It's the primary way you initiate a conversation with the AI.
The "Memory Board": Storing the Conversation
Our chatbot remembers what has been said using something called st.session_state. This is like a whiteboard where we quickly jot down each message as it happens, so we don't forget the flow of the conversation.

How We Use the Interface: A Simple Chat Example
Let's walk through a typical interaction:
User Input: "What is Microsoft's total revenue for 2025?"
Chatbot Output: "Microsoft's total revenue for FY 2025 was $245,000 Million."
This seems straightforward, but behind the scenes, our Interactive Chat Interface is orchestrating everything you see!
- Instead of flask stramlit is used as it is easy to use and create data-driven UI
To run the chatboat we need to run the below command used stramlit as it is easy to use and create data-driven UI
streamlit run .\chatbot.py