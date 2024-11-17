import requests

def process_with_llm(entity, search_results, api_key):
    if not api_key:
        raise ValueError("API key not provided.")
    
    prompt = f"Extract the email address of {entity} from the following web results:\n\n"
    prompt += "\n\n".join([f"{result['title']}: {result['snippet']}" for result in search_results])

    response = requests.post(
        "https://api.groq.com/v1/process",
        json={"prompt": prompt},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    
    if response.status_code == 200:
        return response.json().get("extracted_info", "No data found.")
    else:
        return "Error retrieving data."
