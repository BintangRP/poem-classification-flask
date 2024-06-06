import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split    
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix

from joblib import dump

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="poem_database_big_data"
)


def fetch_data():
    try:
        # Query to select data
        query = "SELECT * FROM poem_table"
        # Use pandas to read data into a DataFrame
        df = pd.read_sql(query, mydb)
    finally:
        mydb.close()
    
    return df

# Fetch the data
data = fetch_data()
print("Data fetched from the database:")
print("cek data :  ", data.head())
# print(data.poem)
# print('')
# print(data.topic)

# Separate features and target variable
X = data.poem
y = data.topic

# print(X)

# Convert text data to numerical data using TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
# model_rf = RandomForestClassifier()
model_svm = SVC(verbose=True)

# model_rf.fit(X_train, y_train)
model_svm.fit(X_train, y_train)


# Make predictions on the test set
# y_pred_rf = model_rf.predict(X_test)
y_pred_svm = model_svm.predict(X_test)


# Encode labels
label_mapping = {label: idx for idx, label in enumerate(set(y))}
y = y.map(label_mapping)


# Evaluate the model
# print("Random Forest", classification_report(y_test,y_pred_rf))
print("SVM", classification_report(y_test,y_pred_svm, target_names=label_mapping.keys()))


# Save the model to a file
# model_filename_rf = 'trained_model_random-forest.pkl'
model_filename_svm = 'trained_model_svm.pkl'
vectorizer_filename = 'tfidf_vectorizer.pkl'

dump(model_svm, model_filename_svm)
dump(vectorizer, vectorizer_filename)

print(f"Model saved to {vectorizer_filename} and {model_filename_svm}")

# Predict on the test set
y_pred = model_svm.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)