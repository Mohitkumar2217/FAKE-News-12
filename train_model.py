import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load datasets
true_news = pd.read_csv("True.csv")
fake_news = pd.read_csv("Fake.csv")

# Add labels
true_news["label"] = "REAL"
fake_news["label"] = "FAKE"

# Combine and shuffle
data = pd.concat([true_news, fake_news])
data = data.sample(frac=1).reset_index(drop=True)

# Use only the text column
X = data["text"]
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Logistic Regression Model
model = LogisticRegression(max_iter=200)
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("✅ Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(vectorizer, "vectorizer.jb")
joblib.dump(model, "lr_model.jb")

print("\n🎉 Model and Vectorizer saved successfully!")
