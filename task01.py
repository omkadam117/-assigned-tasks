import pandas as pd
import requests
import matplotlib.pyplot as plt

# Function to fetch data from the World Bank API
def fetch_world_bank_data(indicator):
    url = f"https://api.worldbank.org/v2/countries/all/indicators/{indicator}?per_page=10000"
    headers = {'Authorization': 'Bearer your_api_key'}  # Replace with your World Bank API key
    response = requests.get(url, headers=headers)
    data = response.json()[1]
    df = pd.DataFrame(data)
    return df

# Fetch total population data
population_data = fetch_world_bank_data("SP.POP.TOTL")

# Extract population values
population = population_data["value"]

# Create the histogram
plt.hist(population, bins=50, color='blue')  # Adjust bin size as needed
plt.title("Distribution of Total Population")
plt.xlabel("Total Population")
plt.ylabel("Frequency")
plt.show()