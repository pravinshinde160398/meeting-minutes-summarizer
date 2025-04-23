import os
import xml.etree.ElementTree as ET
import re
import gensim
from gensim.utils import simple_preprocess
from gensim.corpora import Dictionary
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")

# Define stopwords
stop_words = set(stopwords.words("english"))

# Root directory containing XML annotation files
root_dir = "D:/2nd sem/NLP/NLP projects/AMI_Annotations"  # Update to your actual path

# List to store extracted text data
documents = []

# Recursively scan all XML files
for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)

        # Ignore metadata files and only process annotation files
        if not filename.endswith(".xml") or "metadata" in filename.lower() or "resource" in filename.lower():
            continue  

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            text_data = []

            for section in ["abstract", "actions", "decisions", "problems"]:
                section_element = root.find(f".//{section}")
                if section_element is not None:
                    for sentence in section_element.findall("sentence"):
                        text_data.append(sentence.text)

            if text_data:
                full_text = " ".join(text_data)
                documents.append(full_text)

        except ET.ParseError:
            print(f"❌ Skipping invalid XML file: {file_path}")

print(f"\n✅ Extracted text from {len(documents)} annotation XML files.")

# Save extracted text to a file for reference
with open("extracted_meeting_texts.txt", "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc + "\n")

print("\n✅ Saved extracted text to extracted_meeting_texts.txt")
