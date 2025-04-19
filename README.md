# 📝 Meeting Minutes Summarizer

This project is a **Meeting Minutes Summarizer** built using Natural Language Processing (NLP) techniques. It automatically converts long meeting transcripts into concise summaries, helping teams keep track of key points without going through entire discussions.

---

## 🚀 Features

- ✅ Preprocesses meeting transcripts to clean and normalize text
- 🧠 Extractive summarization using algorithms like **TextRank**
- ✨ Abstractive summarization using transformer models like **T5**
- 🔀 Hybrid method combining both extractive and abstractive techniques
- 📊 Easy-to-run Jupyter Notebook with clean outputs

---

## 📁 Project Structure

```
meeting-minutes-summarizer/
│
├── meeting_minutes_summarizer.py     # Main notebook
├── README.md                         # Project info
└── requirements.txt                  # Optional: libraries used
```

---

## 🧰 Technologies Used

- Python 3.x
- `nltk`
- `sumy`
- `transformers` (Hugging Face)
- `torch` or `tensorflow` (model backend)
- `t-5 model` and `bart` also Pegasus Model

---

## ⚙️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/meeting-minutes-summarizer.git
   cd meeting-minutes-summarizer
   ```

2. Install dependencies:
   ```bash
   pip install nltk transformers sumy
   ```

3. Open the notebook:
   ```bash
   jupyter notebook meeting_minutes_summarizer.ipynb
   ```

4. Follow the steps inside to upload your transcript and generate a summary.

---

## 📌 Sample Output

> **Original Transcript:**  
> "Team discussed roadmap, hiring priorities, and product goals for Q2..."

> **Summary:**  
> "Meeting focused on Q2 roadmap, recruitment strategy, and product targets."

---

## 📌 TODO (Coming Soon)

- Web app interface using **Streamlit**
- Support for speaker identification and diarization
- Integration with Zoom / Meet recordings

---

