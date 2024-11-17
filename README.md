
# AI Agent Project - Web Search & LLM Integration

This project involves the development of an AI agent that reads through a dataset (CSV or Google Sheets), performs web searches for each entity in a selected column, and integrates with a Large Language Model (LLM) to parse and format the extracted data. The project also features a user-friendly dashboard built with Streamlit for interactive data manipulation and visualization.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Keys and Environment Variables](#api-keys-and-environment-variables)
- [Optional Features](#optional-features)
- [Dependencies](#dependencies)
- [Loom Video Walkthrough](#loom-video-walkthrough)
- [License](#license)

---

## Project Overview
The AI Agent is designed to assist users by extracting specific data for each entity (e.g., company names) from a web search, leveraging a web scraping module and LLM for advanced data parsing and structuring. Users can upload CSV files or connect to Google Sheets, define search queries, and download the extracted results in an easy-to-read format.

### **Key Capabilities:**
- Upload and process CSV or Google Sheets data.
- Perform web searches for specific entities from a defined column.
- Use AI-driven parsing via LLM to format and extract structured information.
- Interactive dashboard for easy user input and result visualization.

---

## **Features**
- **CSV/Google Sheets Integration**: Upload and process your data from CSV files or connect to Google Sheets directly.
- **Entity Search**: Choose the primary column (e.g., company names) for web searches and extraction.
- **Custom Search Prompts**: Input custom queries to refine search results and retrieve specific information.
- **Web Search API Integration**: Leverages SerpAPI and Groq API to perform web searches and gather relevant data.
- **Results Display**: View and download structured data with the option to export in CSV format.
- **Streamlit Dashboard**: A simple, interactive user interface for easy data handling and result viewing.

---

## **Project Structure**
The project is organized as follows:

```
ai-agent-project-1/
│
├── dashboard/                  # Streamlit dashboard application
│   └── app.py                  # Main application file for the dashboard
│   └── .env                        # API keys and environment variables
│   └── requirements.txt            # Project dependencies
├── scrapers/                   # Web scraping functionality
│   └── web_search.py           # Scraping functionality for web search
│
├── models/                     # LLM integration and parsing
│   └── llm_integration.py      # LLM integration with APIs (OpenAI, etc.)
│
├── data/                       # Data files and credentials
│   └── service_account.json    # Service account credentials for API access
│
├── venv/                       # Virtual environment for dependency isolation
│
├── README.md                   # Project overview and setup instructions
└── __init__.py                 # Initialization for the project
```

---

## **Installation**
To install the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Dragoon1243/ai-agent-project.git
    cd ai-agent-project-1
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On **Windows**:
    ```bash
    venv\Scripts\activate
    ```

    - On **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## **Service Account Setup**

This project interacts with Google APIs (like Google Sheets) using a service account. You need to create a service account in your Google Cloud project and configure the project to use the credentials file.

### **Steps to Set Up a Service Account:**

1. **Create a Service Account** in the [Google Cloud Console](https://console.cloud.google.com/).
    - Navigate to **IAM & Admin > Service Accounts**.
    - Click **Create Service Account**, provide a name, and assign the necessary roles (like **Editor** or custom roles depending on your needs).
    - Click **Done**.

2. **Generate and Download the Service Account Credentials**:
    - After creating the service account, generate the JSON key file. This file contains the private key and other details necessary for authentication.
    - Download this JSON file and save it in a secure location.

### **Configuring the Project with Service Account Credentials**

Once you have the service account credentials JSON file, follow these steps:

1. **Store the Credentials File** securely and **do not commit it to version control** (e.g., GitHub). Add the file path to your `.gitignore` file to ensure it isn't accidentally uploaded.

2. **Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable** to the path of your credentials file:
    - **For Windows:**
      ```bash
      set GOOGLE_APPLICATION_CREDENTIALS="path\to\your\service_account.json"
      ```
    - **For macOS/Linux:**
      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service_account.json"
      ```

3. The project will use these credentials to authenticate and interact with Google Sheets or other Google services.

### **Important Notes:**
- Ensure that the service account has the necessary permissions to access the resources you intend to use (e.g., Google Sheets, Google Drive).
- For security reasons, **never share your service account JSON file publicly**.

### Example of Service Account JSON Structure (Do not use this exact content):
```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "your-private-key",
  "client_email": "your-service-account-email",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your-cert-url"
}
```

## **Usage**

Once the project is installed, follow these steps to run the application:

1. Run the Streamlit app:

    ```bash
    streamlit run dashboard/app.py
    ```

   This will start the Streamlit application in your web browser.

### Dashboard Features:
- **Upload CSV or Google Sheets**: Upload your dataset in CSV format or connect to Google Sheets for data processing.
- **Define Search Column**: Select the column with entities (e.g., company names) that you want to search for.
- **Enter Custom Queries**: Input custom search prompts for tailored information retrieval.
- **View and Download Results**: View the extracted data directly in the dashboard and export it as a CSV file.

---

## API Keys and Environment Variables
To enable the web search functionality, you need to provide your **SerpAPI** and **Groq API** keys. Add the following lines to your `.env` file:

```bash
SERPAPI_KEY=your_serpapi_key
GROQ_API_KEY=your_groq_api_key
```

Make sure to keep these API keys private and secure.

---

## Optional Features
- **Google Sheets Integration**: You can connect to Google Sheets by setting up your service account credentials and ensuring the correct configuration.
- **Advanced Search Options**: You can extend the search functionality with multiple queries or additional filtering options to narrow down results.

---

## Dependencies
The project requires the following Python packages, which are listed in `requirements.txt`:

- **Streamlit==1.23.1**: For building the interactive dashboard.
- **Pandas==1.5.2**: For data handling and manipulation.
- **Google API Python Client==2.53.0**: To interact with Google Sheets.
- **Google Auth==2.11.0** and **Google Auth OAuthlib==0.6.0**: For authenticating Google APIs.
- **Requests==2.28.1**: For HTTP requests to external APIs.
- **Python-dotenv==0.21.0**: To manage environment variables securely.

Install all dependencies by running:

```bash
pip install -r requirements.txt
```

---

## Loom Video Walkthrough
A brief Loom video has been provided, explaining the following:
- The overall purpose and capabilities of the project.
- A walkthrough of the Streamlit dashboard and its key features.
- Explanation of important code implementations and challenges faced.
- link: "https://www.loom.com/share/3b74be3c98f04ccf811ad3688b97a188?sid=30c18683-8924-4e72-98bf-ed86a8572fad"

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```

### Adjustments Made:
- I corrected the **Usage** section’s formatting issue.
- The document maintains proper Markdown syntax to ensure that everything is correctly formatted, especially the headings and code blocks.
