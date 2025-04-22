import re
import csv

# Load the dataset (replace the file path with your actual file path)
input_file = "extracted_meeting_texts.txt"  # Your dataset file
output_file = "annotated_dataset.csv"  # Output file for annotations

# Define categories and related keywords
categories = {
    "Decisions": ["finalize", "decided", "approved", "agreed", "concluded", "resolved"],
    "Actions": ["assign", "implement", "prepare", "completed", "task", "responsibility", "deliver"],
    "Problems": ["issue", "problem", "concern", "challenge", "risk", "difficulty"],
    "Discussion Points": ["discuss", "review", "consider", "analyze", "explore", "evaluate"]
}

# Function to categorize sentences
def categorize_sentence(sentence):
    annotation = {"Decisions": [], "Actions": [], "Problems": [], "Discussion Points": []}
    for category, keywords in categories.items():
        if any(keyword in sentence.lower() for keyword in keywords):
            annotation[category].append(sentence.strip())
    return annotation

# Read and process the dataset
annotated_data = []
with open(input_file, "r", encoding="utf-8") as file:
    documents = file.readlines()

for doc in documents:
    doc_annotations = {"Original Text": doc.strip()}
    # Split the document into sentences
    sentences = re.split(r'[.!?]', doc.strip())
    categorized_data = {"Decisions": [], "Actions": [], "Problems": [], "Discussion Points": []}
    
    for sentence in sentences:
        if sentence.strip():
            sentence_annotation = categorize_sentence(sentence)
            # Merge sentence annotations into the document annotations
            for category in categorized_data.keys():
                categorized_data[category].extend(sentence_annotation[category])

    # Combine categorized data into strings for CSV
    for category, sentences in categorized_data.items():
        doc_annotations[category] = " | ".join(sentences)

    annotated_data.append(doc_annotations)

# Save the annotated data to a CSV file
fieldnames = ["Original Text", "Decisions", "Actions", "Problems", "Discussion Points"]

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(annotated_data)

print(f"✅ Annotation complete. Results saved to {output_file}")
