import requests
import json

# ---------------------------------------------------------
# 1. Test API connection
# ---------------------------------------------------------
print("Testing connection to Cat Facts API...")
test_response = requests.get("https://catfact.ninja/fact")
print("Status code:", test_response.status_code)

# ---------------------------------------------------------
# 2. Print raw response (no formatting)
# ---------------------------------------------------------
print("\nRaw response text:")
print(test_response.text)

# ---------------------------------------------------------
# 3. Print formatted JSON (tutorial-style formatting)
# ---------------------------------------------------------
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("\nFormatted JSON output:")
jprint(test_response.json())
