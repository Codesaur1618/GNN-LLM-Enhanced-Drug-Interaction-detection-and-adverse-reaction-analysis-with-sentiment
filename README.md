

### 📄 README.md 

```markdown
# 💊 Drug-Drug Interaction & Reaction Sentiment Analyzer

This web application predicts **interactions between two drugs** using a **T5-based reaction generation model** and assesses the **sentiment of the predicted interaction** with a **BioBERT-based classifier**. It provides insights into whether the interaction is potentially positive or adverse, along with a confidence score.

---

## 🧠 Features

- 🔬 Predicts drug-drug reactions using a T5 model fine-tuned on biomedical data
- 📚 Falls back to known custom interactions for well-defined drug pairs
- 😊 Analyzes sentiment (Positive or Negative) of the predicted interaction using BioBERT
- 🌐 Simple and intuitive Flask web interface
- 🧪 Designed for biomedical and pharmaceutical research use

---

## 🚀 Tech Stack

- **Framework**: Flask (Python)
- **Model 1**: T5 (`T5ForConditionalGeneration`) for reaction prediction
- **Model 2**: BioBERT (`AutoModelForSequenceClassification`) for sentiment analysis
- **Custom Logic**: Rule-based fallback reactions (via `check_custom_reaction()`)

---

## 📁 Directory Structure

```
├── app.py
├── templates/
│   └── index.html
├── custom_logic.py
├── Models/
│   ├── Model_saved/             # T5 model directory
│   └── biobert_model_package/   # BioBERT model directory
└── README.md
```

---

## 🧪 Requirements

- Python 3.7+
- Install Python packages:
  ```bash
  pip install flask torch transformers
  ```

- Pretrained models:
  - T5 model trained on drug-drug interaction data
  - BioBERT sequence classification model

---

## ⚙️ Configuration

- Set your T5 and BioBERT model paths in `app.py`:
  ```python
  reaction_model_path = "path/to/t5_model"
  sentiment_model_path = "path/to/biobert_model"
  ```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 📌 Notes

- Make sure you have the correct tokenizer and model files in your model directories.
- Update `check_custom_reaction()` in `custom_logic.py` to include any domain-specific rules or known interactions.
- This project is for educational and research use; not for clinical deployment.

---

## 🧠 Author

Made by **Abisek**  
Passionate about AI in drug discovery and biomedical NLP 🌱

---

## 📜 License

This project is open-source under the MIT License.
```

Let me know if you'd like to include example input/output screenshots, model training details, or Docker deployment steps!
