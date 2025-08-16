# Title: Flavor Exploration
# Purpose: To quantify preferences and present them in a graphical form
# Last updated: 2025-07-06
# Authors: Liz and JRO

#-------------
# GOALS:
#-------------
# The idea is to use a database to create:
# - A report
# - A data visualization

# Import SQLite
import sqlite3

print("Bienvenida a la exploracion de sabores!")

# Connect with our databasse / file
connection = sqlite3.connect("data/flavors.db")
cursor = connection.cursor()
# Run some queries:
# (1) What type of preferred taste do people with Mediterranean culinary exposure have?
#     Top preferred taste for Mediterranean individuals.
#     Visualization: Bar chart

# Filter only on historical quisine of Mediterranan
# Question: In SQL, how to filter on a text value within column of data?
# SELECT *
# FROM table_name
# WHERE column_name = 'desired_text';

# select * from flavors where historical_cuisine_exposure = 'Mediterranean';

# select preferred_taste, COUNT(*) as taste_count
# FROM flavors 
# WHERE historical_cuisine_exposure = 'Mediterranean'
# GROUP BY preferred_taste
# ORDER BY taste_count DESC;

# # Question: How to sort data in SQL?
# ORDER BY column_name [ASC|DESC];

# Do a count on the preferred tastes
# Question: How can I count the occurences of data in SQL
# SELECT column_name, COUNT(*) AS occurrence_count
# FROM table_name
# GROUP BY column_name;
# Sort by highest count to lowests

rows = cursor.execute("SELECT preferred_taste, COUNT(*) AS taste_count FROM flavors WHERE historical_cuisine_exposure = 'Mediterranean' GROUP BY preferred_taste ORDER BY taste_count DESC;").fetchall()
print(rows)
# (2) What is the average age of people with an "Early Bird" sleep cycle?
#     Visualization: Histogram
rows = cursor.execute("SELECT AVG(age) AS ave_age FROM flavors WHERE sleep_cycle = 'night' ;").fetchall()
print(rows)

# (3) Cuantas personas que viven en clima frio hacen ejercicio fuerte.How many people in the cold climate zone practice heavy excericise habits.Visualization to research or explore
rows = cursor.execute("""SELECT count(*) AS count_climate_zone FROM flavors WHERE exercise_habits = 'Heavy' AND climate_zone = 'Cold' ;""").fetchall()
print(rows)

# (4) Cuales es el sabor que menos le gusta a las personas de 25 años.what flavor for people in their 25 years old hate.visualization to research
rows = cursor.execute("""SELECT preferred_taste FROM flavors WHERE age = 25 GROUP BY preferred_taste ORDER BY preferred_taste ASC;""").fetchall()
print(rows)

# (5) How many people aged between 18 and 50 enjoy intense exercise, live in a dry climate, and prefer the sour taste?
#     Visualization: To research or explore
total = cursor.execute("""SELECT COUNT(*) AS total_personas FROM flavors WHERE age > 18 AND age < 50 AND exercise_habits = 'Heavy' AND climate_zone = 'Dry' AND preferred_taste = 'Sour';""").fetchone()
print(f"Total de personas: {total[0]}")

# Display the information on the screen

# Use a visualization library (for example: Apache ECharts or D3.js)
# to perform an exploratory data visualization

# 4. Random Forest https://www.geeksforgeeks.org/machine-learning/random-forest-regression-in-python/
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, classification_report
# Connect with our database
connection = sqlite3.connect("data/flavors.db")
cursor = connection.cursor()

# Read data from a table (for example, the "orders" table)
df = pd.read_sql_query("SELECT * FROM flavors", connection)
# 3. Explore columns
df = df.copy()
df['preferred_taste'] = df['preferred_taste'].map({'Salty': 1, 'Swweet': 0, 'Sour': 2,'Spicy': 3})
df['climate_zone'] = df['climate_zone'].map({'Dry': 1, 'Temperate': 0, 'Cold': 2,'Tropical': 3})
df['sleep_cycle'] = df['sleep_cycle'].map({'Early Bird': 1, 'Night Owl': 0, 'Irregular': 2})
print("Columnas disponibles:", df.columns)

# Remove rows where y is NaN
df = df.dropna(subset=['preferred_taste'])  # Make sure that 'Clase' is the correct name
X = df.drop('preferred_taste', axis=1)
y = df['preferred_taste']
df.replace('', np.nan, inplace=True)
# 4. Select the columns you will use
# Suppose your target variable is 'delivered' (0 or 1) and the rest are numerical
# Change these names to the actual ones according to your database
columnas_escogidas = ['age', 'climate_zone', 'sleep_cycle']  # only those you want to use
X = df[columnas_escogidas].copy()
y = df['preferred_taste']


# 5. Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
# 6. Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=10)
model.fit(X_train, y_train)
# 7. Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))
# 8. Save the trained model (optional)
import joblib
joblib.dump(model, 'modelo_random_forest.pkl')
print(df.head())
print(df.dtypes)

# New data
nuevo_dato = {'age': 39, 'climate_zone': 3, 'sleep_cycle': 'Early Bird'}
# Convert to DataFrame
nuevo_df = pd.DataFrame([nuevo_dato])
# Map the categorical values exactly as before
nuevo_df['climate_zone'] = nuevo_df['climate_zone'].map({'Dry': 1, 'Temperate': 0, 'Cold': 2,'Tropical': 3})
nuevo_df['sleep_cycle'] = nuevo_df['sleep_cycle'].map({'Early Bird': 1, 'Night Owl': 0, 'Irregular': 2})
print("Columnas disponibles:", nuevo_df.columns)
columnas_escogidas = ['age', 'climate_zone', 'sleep_cycle']
nuevo_df = nuevo_df[columnas_escogidas]
import joblib
# Load model from the .pkl file
modelo_cargado = joblib.load('modelo_random_forest.pkl')
# Make prediction
prediccion = modelo_cargado.predict(nuevo_df)

# Display result
if prediccion[0] == 0:
    sabor = "Sweet"
elif prediccion[0] == 1:
    sabor = "Salty"
elif prediccion[0] == 2:
    sabor = "Sour"
elif prediccion[0] == 3:
    sabor = "Spicy"
else:
    sabor = "Desconocido"

print("Predicción:", sabor)
# This shows you how many positives/negatives it predicts correctly or incorrectly
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

conf_matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
disp.plot()
# This will show you if your model is failing to detect the negative cases.

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
# Pay attention to:

# Precision (for class 1) → how many of the predicted positives were actually positive.

# Recall (for class 0) → whether it really detects the negatives.

# F1-Score → balance between precision and recall.
print(y.value_counts(normalize=True))


# Calculate the correlation matrix
numeric_df = nuevo_df.select_dtypes(include='number')
corr_matrix = numeric_df.corr()
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
print(corr_matrix)
#Fix the Nan
print(nuevo_df[['age', 'climate_zone', 'sleep_cycle', ]].head(10))
subset_df = nuevo_df[['age', 'climate_zone', 'sleep_cycle']].apply(pd.to_numeric, errors='coerce')
subset_df = subset_df.dropna()  # drop rows with any NaNs
# OR
# subset_df = subset_df.fillna(0)  # fill with 0s, if that makes sense
#Make sure you have enough rows
print(nuevo_df[['age', 'climate_zone', 'sleep_cycle']].shape)
#Handle missing data
subset_df = nuevo_df[['age', 'climate_zone', 'sleep_cycle']].dropna()

#
corr_matrix = subset_df.corr()
print(corr_matrix)
# the results show that the categorical variables/climate zone/sleep cycle/ encoded as numbers may not be meaningful or may cause weird results like NaNs.End of the analysis