# test_modules.py

from scrapers.web_search import perform_web_search
from models.llm_integration import process_with_llm

# Simple test to verify if the modules are working
print("Testing perform_web_search function:")
try:
    results = perform_web_search("Test search", "test_api_key")
    print("Web Search Test Passed")
except Exception as e:
    print(f"Web Search Test Failed: {e}")

print("Testing process_with_llm function:")
try:
    results = process_with_llm("Test Entity", [], "test_api_key")
    print("LLM Test Passed")
except Exception as e:
    print(f"LLM Test Failed: {e}")
