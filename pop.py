import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# File path
file_path = r"C:\Users\API_SP.POP.TOTL_DS2_en_xml_v2_6545412\API_SP.POP.TOTL_DS2_en_xml_v2_6545412.xml"

# Parse the XML file
tree = ET.parse(file_path)
root = tree.getroot()

# Function to extract population data for a specific country from a given year range
def extract_population_data(country_code, start_year, end_year):
    years = []
    populations = []
    for record in root.findall('.//record'):
        country = record.find(".//field[@name='Country or Area']").text
        year = int(record.find(".//field[@name='Year']").text)
        population = record.find(".//field[@name='Value']").text
        if country == country_code and start_year <= year <= end_year:
            years.append(year)
            populations.append(int(population))
    return years, populations

# Input countries and years range
country1 = input("Enter Country 1: ")
country2 = input("Enter Country 2: ")
start_year = 1960
end_year = 2022

# Extract population data for the two countries
years1, populations1 = extract_population_data(country1, start_year, end_year)
years2, populations2 = extract_population_data(country2, start_year, end_year)

# Plotting the data
plt.figure(figsize=(12, 8))
plt.hist(years1, bins=len(years1), weights=populations1, alpha=0.5, color='blue', label=country1)
plt.hist(years2, bins=len(years2), weights=populations2, alpha=0.5, color='orange', label=country2)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth Comparison ({0} vs {1})'.format(country1, country2))
plt.legend()
plt.grid(True)
plt.show()
