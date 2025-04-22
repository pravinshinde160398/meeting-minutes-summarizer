import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

# Download required NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize resources
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Load the extracted text file
input_file = "extracted_meeting_texts.txt"  # Path to your extracted text file
with open(input_file, "r", encoding="utf-8") as f:
    documents = f.readlines()

# Preprocessing function
def preprocess_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove special characters and numbers
    text = re.sub(r"[^a-z\s]", "", text)
    
    # 3. Tokenize
    words = word_tokenize(text)
    
    # 4. Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # 5. Lemmatize
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return " ".join(words)

# Apply preprocessing to each document
cleaned_documents = [preprocess_text(doc) for doc in documents]

# Save preprocessed data to a new file (optional)
with open("preprocessed_meeting_texts.txt", "w", encoding="utf-8") as f:
    for doc in cleaned_documents:
        f.write(doc + "\n")

print("✅ Preprocessing complete. Cleaned data saved to 'preprocessed_meeting_texts.txt'.")

# Convert text to numerical representation using TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # Limit features for efficiency
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_documents)

print(f"✅ TF-IDF matrix created with shape: {tfidf_matrix.shape}")
