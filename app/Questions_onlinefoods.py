#Import SQLite

import sqlite3

import requests
import time

print("Welcome to onlinefoods!")


# Connect with our database

connection = sqlite3.connect("data/onlinefood.db")

cursor = connection.cursor()

# create some queries:

#1.Top of family size preference for online food


rows = cursor.execute("SELECT Family, COUNT(*) as top_size FROM onlinefood GROUP BY Family ORDER BY top_size DESC;").fetchall()

print(rows)


#2.Which place in the world has the highest preference for online food?

rows = cursor.execute("SELECT latitude, longitude, COUNT(*) as top_place FROM onlinefood GROUP BY Longitude, latitude ORDER BY top_place DESC LIMIT 1;").fetchall()


if rows:

    lat, lon, count = rows[0]

    print(f"Coordenadas más frecuentes: {lat}, {lon} ({count} registros)")
    

    # Geocodificación inversa usando Nominatim (gratuito)

    def obtener_nombre_lugar(latitude, longitude):

        url = f"https://nominatim.openstreetmap.org/reverse"

        params = {

            'format': 'json',

            'lat': latitude,

            'lon': longitude,

            'zoom': 18,

            'addressdetails': 1

        }
        

        headers = {'User-Agent': 'tu_aplicacion/1.0'}
        

        try:

            response = requests.get(url, params=params, headers=headers)

            if response.status_code == 200:

                data = response.json()

                return {

                    'nombre_completo': data.get('display_name', 'No encontrado'),

                    'ciudad': data.get('address', {}).get('city', ''),

                    'pais': data.get('address', {}).get('country', ''),

                    'direccion': data.get('address', {})

                }

        except Exception as e:

            print(f"Error: {e}")

        return None
    

    # Obtener el nombre del lugar

    lugar_info = obtener_nombre_lugar(lat, lon)
    

    if lugar_info:

        print(f"Lugar: {lugar_info['nombre_completo']}")

        print(f"Ciudad: {lugar_info['ciudad']}")

        print(f"País: {lugar_info['pais']}")

    else:

        print("No se pudo obtener el nombre del lugar")


#3.Which occupation shows the highest preference for online food ordering, organized by gender and age?

rows = cursor.execute("SELECT Gender, Occupation, COUNT(*) as top_occupation FROM onlinefood GROUP BY Gender, Occupation ORDER BY Gender DESC LIMIT 1;").fetchall()

print(rows)


# 4. Random Forest https://www.geeksforgeeks.org/machine-learning/random-forest-regression-in-python/

# Import necessary libraries
import pandas as pd

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

connection = sqlite3.connect("data/onlinefood.db")

cursor = connection.cursor()


# Read data from a table (for example, the "orders" table)

df = pd.read_sql_query("SELECT * FROM onlinefood", connection)

# 3. Explore columnss

df = df.copy()

df['Feedback'] = df['Feedback'].map({'Positive': 1, 'Negative': 0})

df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

df['Marital'] = df['Marital'].map({'Single': 1, 'Married': 0, 'Prefer not to say': 2})

df['Occupation'] = df['Occupation'].map({'Student': 1, 'Employee': 0, 'Self Employeed': 2, 'House wife': 3})

df['Monthly'] = df['Monthly'].map({'No income': 1, 'Below10000': 0, 'More50000': 2, '1000to25000': 3, '2500to5000': 4})

print("Columnas disponibles:", df.columns)


# Remove rows where y is NaN

df = df.dropna(subset=['Feedback'])   # Make sure that 'Clase' is the correct name

X = df.drop('Feedback', axis=1)

y = df['Feedback']


# 4. Select the columns you will use

# Suppose your target variable is 'delivered' (0 or 1) and the rest are numerical

# Change these names to the actual ones according to your database

columnas_escogidas = ['age', 'Family', 'Gender', 'Marital', 'Occupation', 'Monthly']  # only those you want to use

X = df[columnas_escogidas].copy()

y = df['Feedback']


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

nuevo_dato = {'age': 0, 'Family': 6, 'Gender': 'Male', 'Marital': 'Prefer not to say', 'Occupation': 'Student', 'Monthly':'No income'}

# Convert to DataFrame

nuevo_df = pd.DataFrame([nuevo_dato])

# Map the categorical values exactly as before

nuevo_df['Gender'] = nuevo_df['Gender'].map({'Male': 1, 'Female': 0})

nuevo_df['Marital'] = nuevo_df['Marital'].map({'Single': 1, 'Married': 0, 'Prefer not to say': 2})

nuevo_df['Occupation'] = nuevo_df['Occupation'].map({'Student': 1, 'Employee': 0, 'Self Employeed': 2, 'House wife': 3})

nuevo_df['Monthly'] = nuevo_df['Monthly'].map({'No income': 1, 'Below10000': 0, 'More50000': 2, '1000to25000': 3, '2500to5000': 4})

columnas_escogidas = ['age', 'Family', 'Gender', 'Marital', 'Occupation', 'Monthly']

nuevo_df = nuevo_df[columnas_escogidas]

import joblib

# Load model from the .pkl file

modelo_cargado = joblib.load('modelo_random_forest.pkl')

# Make prediction

prediccion = modelo_cargado.predict(nuevo_df)


# Display result

print("Predicción:", "Feedback Positivo" if prediccion[0] == 1 else "Feedback Negativo")

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


# I will use Scatter plot with Matplotlib for a better understanding of the variables 

import matplotlib.pyplot as plt


#columnas_escogidas = ['age']  # only those you want to use

#X = df[columnas_escogidas].copy()

#y = df['Feedback']


# Create scatter plot

#plt.scatter(X, y)


# Add labels and title

#plt.xlabel("X-axis")

#plt.ylabel("Y-axis")

#plt.title("Simple Scatter Plot")


# Show plot

#plt.show()


# Correlation Matrix + Heatmap
#See how strongly each pair of variables is related.

#import seaborn as sns
#import matplotlib.pyplot as plt

#corr = nuevo_df.corr(numeric_only=True)  # Get correlation for numeric columns
#sns.heatmap(corr, annot=True, cmap='coolwarm')
#plt.title("Correlation Matrix")
#plt.show()
#Values near 1 or -1 = strong relationship

#Near 0 = weak/no linear relationship

#View correlation Matrix as numbers
import pandas as pd

# Calculate the correlation matrix
numeric_df = nuevo_df.select_dtypes(include='number')
corr_matrix = numeric_df.corr()
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
# Checking if columns are numerical 
print(nuevo_df.dtypes)
numeric_cols = nuevo_df.select_dtypes(include='number').columns
print("Numeric columns:", numeric_cols)
# the results show that the categorical variables/gender/marital/occupation/ encoded as numbers may not be meaningful or may cause weird results like NaNs
# Lets try with three variables
subset_df = nuevo_df[['age', 'Monthly', 'Family']]
# Calculate correlation matrix
corr_matrix = subset_df.corr()

# Show the numeric correlation matrix
print(corr_matrix)

#Fix the Nan
print(nuevo_df[['age', 'Monthly', 'Family']].head(10))
subset_df = nuevo_df[['age', 'Monthly', 'Family']].apply(pd.to_numeric, errors='coerce')
subset_df = subset_df.dropna()  # drop rows with any NaNs
# OR
# subset_df = subset_df.fillna(0)  # fill with 0s, if that makes sense

# Now calculate correlation
corr_matrix = subset_df.corr()
print(corr_matrix)

# Optional Heat map
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix: age, Monthly, Family")
plt.show()
#Check for missing values
print(nuevo_df[['age', 'Monthly', 'Family']].isnull().sum())
#Check unique values (useful if columns might be categorical)
for col in ['age', 'Monthly', 'Family']:
    print(f"Unique values in {col}:")
    print(nuevo_df[col].unique())
    print()

#Check data types
print(nuevo_df[['age', 'Monthly', 'Family']].dtypes)

#Are There Enough Non-Constant Values?
print(nuevo_df[['age', 'Monthly', 'Family']].nunique())
# the result says >correlation will be NaN because there’s no variability.

#Preview the Data
print(nuevo_df[['age', 'Monthly', 'Family']].head(10))

#Try This All-in-One Diagnostic Script
subset = nuevo_df[['age', 'Monthly', 'Family']]

print("Data Preview:")
print(subset.head())

print("\nMissing Values:")
print(subset.isnull().sum())

print("\nUnique Values:")
print(subset.nunique())

print("\nBasic Stats:")
print(subset.describe())

print("\nCorrelation Matrix:")
print(subset.corr())

# the results show that the categorical variables/gender/marital/occupation/ encoded as numbers may not be meaningful or may cause weird results like NaNs.End of the analysis