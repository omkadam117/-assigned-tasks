import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_data = pd.read_csv("titanic.csv")

# Explore the data
print(titanic_data.head())
print(titanic_data.info())

# Handle missing values
titanic_data.fillna({"Age": titanic_data["Age"].mean()}, inplace=True)

# Explore the distribution of ages
sns.histplot(titanic_data["Age"], bins=30)
plt.title("Distribution of Ages")
plt.show()

# Explore the relationship between sex and survival
sns.barplot(x="Sex", y="Survived", data=titanic_data)
plt.title("Survival Rate by Sex")
plt.show()

# Explore the relationship between class and survival
sns.barplot(x="Pclass", y="Survived", data=titanic_data)
plt.title("Survival Rate by Class")
plt.show()

# Explore the correlation between variables
correlation_matrix = titanic_data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Matrix")
plt.show()