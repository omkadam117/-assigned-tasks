import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load the traffic accident data
accident_data = pd.read_csv("us_accidents.csv")

# Explore the data
print(accident_data.head())
print(accident_data.info())

# Handle missing values
accident_data.dropna(inplace=True)

# Convert data types
accident_data["Start_Time"] = pd.to_datetime(accident_data["Start_Time"])

# Analyze accidents by hour
accident_data["Hour"] = accident_data["Start_Time"].dt.hour
sns.countplot(x="Hour", data=accident_data)
plt.title("Accidents by Hour")
plt.show()

# Analyze accidents by weather condition
sns.countplot(x="Weather_Condition", data=accident_data)
plt.title("Accidents by Weather Condition")
plt.xticks(rotation=45)
plt.show()

# Visualize accident hotspots (assuming you have latitude and longitude columns)
accident_map = folium.Map(location=[accident_data["Start_Lat"].mean(), accident_data["Start_Lng"].mean()])
for index, row in accident_data.iterrows():
    folium.Marker(location=[row["Start_Lat"], row["Start_Lng"]]).add_to(accident_map)
accident_map.save("accident_hotspots.html")