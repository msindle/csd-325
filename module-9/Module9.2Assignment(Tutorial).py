import requests
import json

# ---------------------------------------------------------
# 1. Test API connection (required by assignment)
# ---------------------------------------------------------
print("Testing connection to Google...")
response = requests.get("http://www.google.com")
print("Status code:", response.status_code)

# ---------------------------------------------------------
# 2. Retrieve current astronauts from OpenNotify
# ---------------------------------------------------------
print("\nRetrieving current astronauts from OpenNotify...")
astro_response = requests.get("http://api.open-notify.org/astros.json")

print("Status code:", astro_response.status_code)

# ---------------------------------------------------------
# 3. Format JSON output (tutorial method)
# ---------------------------------------------------------
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("\nFormatted astronaut data:")
jprint(astro_response.json())
