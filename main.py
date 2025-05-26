import pprint
import requests

# Make the GET request
response = requests.get(
    'https://gist.githubusercontent.com/Niranjan719/179c1bfa5f0c4801b18304b41968655f/raw/4959d54980b94a0de2562308df755ad6b16a83b8/andrewng_linkedin.json'
)
# Parse JSON and pretty print it
data = response.json()
pprint.pprint(data)
