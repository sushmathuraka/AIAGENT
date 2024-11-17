import requests

def perform_web_search(query, api_key):
    if not api_key:
        raise ValueError("API key not provided.")
    
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }
    
    response = requests.get("https://serpapi.com/search", params=params)
    
    if response.status_code == 200:
        results = response.json().get("organic_results", [])
        return results
    else:
        return []
