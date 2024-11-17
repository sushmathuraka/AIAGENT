# app.py
import sys
import os
import json
import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv


# Ensure the project root directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local imports
from scrapers.web_search import perform_web_search
from models.llm_integration import process_with_llm

# Toggle Debug Mode (Set True for debugging, False for production)
DEBUG_MODE = False

if DEBUG_MODE:
    # Debugging information to check current paths
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Python Path: {sys.path}")

# Load environment variables from .env file
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Google Sheets API Setup
def authenticate_google_sheets():
    try:
        with open("data/service_account.json") as source:
            info = json.load(source)
            return service_account.Credentials.from_service_account_info(info)
    except FileNotFoundError:
        st.error("Service account file not found. Please upload `service_account.json`.")
        return None
    except json.JSONDecodeError:
        st.error("Failed to decode the service account JSON file.")
        return None

def connect_to_google_sheet(credentials):
    if not credentials:
        return None

    try:
        service = build('sheets', 'v4', credentials=credentials)
        return service
    except Exception as e:
        st.error(f"Failed to connect to Google Sheets: {e}")
        return None

def load_google_sheet(service, spreadsheet_id):
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range="Sheet1").execute()
        values = result.get('values', [])
        return pd.DataFrame(values[1:], columns=values[0]) if values else None
    except Exception as e:
        st.error(f"Failed to load Google Sheet: {e}")
        return None

# Main Dashboard
st.title("AI Agent Dashboard 🌐")
st.subheader("Upload CSV or Connect to Google Sheets")

# CSV File Upload Section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
csv_data = None
if uploaded_file is not None:
    try:
        csv_data = pd.read_csv(uploaded_file)
        st.write("**Uploaded CSV Preview:**")
        st.dataframe(csv_data.head())
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")

# Google Sheets Section
st.subheader("Or, Connect to Google Sheets")
spreadsheet_id = st.text_input("Enter Google Spreadsheet ID")
credentials = authenticate_google_sheets()
service = connect_to_google_sheet(credentials)
sheet_data = None

if st.button("Load Google Sheet") and spreadsheet_id:
    sheet_data = load_google_sheet(service, spreadsheet_id)
    if sheet_data is not None:
        st.write("**Google Sheet Data Preview:**")
        st.dataframe(sheet_data.head())

# Choose main column (for entity extraction)
if csv_data is not None or sheet_data is not None:
    data = csv_data if csv_data is not None else sheet_data
    main_column = st.selectbox("Select the main column to analyze", data.columns)
    st.write(f"**Selected Column:** {main_column}")

    # Dynamic Query Input
    user_prompt = st.text_input("Enter your query (use {entity} as placeholder)")
    if user_prompt and main_column:
        st.write(f"**Query Example:** {user_prompt.replace('{entity}', str(data[main_column].iloc[0]))}")

    # Process Button
if st.button("Start Information Retrieval"):
        if main_column in data.columns:
            entities = data[main_column].dropna().tolist()  # Extract entities

        if not entities:
            st.error("No entities found in the selected column.")
        else:
            if not user_prompt:
                st.error("Please enter a query with {entity} placeholder.")
            else:
                results = []

                for entity in entities:
                    try:
                        # Generate the query by replacing {entity} in the user prompt
                        query = user_prompt.replace("{entity}", str(entity))
                        st.write(f"**Query generated:** {query}")  # Confirm the query being generated

                        # Perform the search
                        search_results = perform_web_search(query, SERPAPI_KEY)
                        if not search_results:
                            st.warning(f"No results found for query: {query}")
                            extracted_info = "No data retrieved"
                        else:
                            # Display raw search results for debugging
                            st.write("**Search Results Debugging Info:**")
                            st.json(search_results)  # Check if search results are populated

                            # Process the results with LLM
                            extracted_info = process_with_llm(entity, search_results, GROQ_API_KEY)
                            st.write(f"**Extracted Information:** {extracted_info}")  # Show what LLM returned

                        # Append results
                        results.append({"Entity": entity, "Extracted Info": extracted_info})

                    except Exception as e:
                        st.error(f"Error processing entity '{entity}': {e}")
                        results.append({"Entity": entity, "Extracted Info": "Error retrieving data"})
