from flask import Flask, render_template, request
import torch
import torch.nn.functional as F
from custom_logic import check_custom_reaction
from transformers import T5Tokenizer, T5ForConditionalGeneration, AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

# 🧠 Load the T5 reaction model
class GNNReactionPredictor:
    def __init__(self, model_path):
        self.encoder = T5ForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)

    def forward(self, input_text):
        input_ids = self.tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True).input_ids
        output = self.encoder.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return decoded

# ✅ Load models from your specified paths
reaction_model_path = "C:/Users/abise/OneDrive/Documents/1. DRUG PAPER/Models/Model_saved"
sentiment_model_path = "C:/Users/abise/OneDrive/Documents/1. DRUG PAPER/Models/biobert_model_package"

gnn_model = GNNReactionPredictor(reaction_model_path)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_path)
sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_path)
sentiment_model.eval()

# ⚗️ Predict drug-drug interaction (with custom fallback logic)
def get_interaction(drug1, drug2):
    # First check the custom list
    custom_reaction = check_custom_reaction(drug1, drug2)
    if custom_reaction:
        return custom_reaction

    # Otherwise use the T5 model
    graph_input = f"react: {drug1} and {drug2}"
    return gnn_model.forward(graph_input)

# 😊 Predict sentiment of the reaction
def predict_sentiment(text):
    inputs = sentiment_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = sentiment_model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        predicted_class = torch.argmax(probs, dim=1).item()
        confidence = probs[0][predicted_class].item()

    sentiment = "Positive 😊" if predicted_class == 1 else "Negative ⚠️"
    return sentiment, confidence

# 🌐 Web Interface
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        drug1 = request.form["drug1"]
        drug2 = request.form["drug2"]

        reaction = get_interaction(drug1, drug2)
        sentiment, confidence = predict_sentiment(reaction)

        return render_template("index.html", drug1=drug1, drug2=drug2, reaction=reaction, sentiment=sentiment, confidence=confidence)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
