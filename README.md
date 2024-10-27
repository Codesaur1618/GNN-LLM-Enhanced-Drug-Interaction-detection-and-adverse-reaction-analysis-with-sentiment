# GNN – Enhanced Drug Interaction Detection and Adverse Reaction Analysis with Sentiment Insights

## Abstract
This study introduces a comprehensive approach for detecting Drug-Drug Interactions (DDIs) and predicting Adverse Drug Reactions (ADRs) by integrating Graph Neural Networks (GNNs) with Sentiment Analysis. The rising prevalence of polypharmacy has amplified the need for precise detection of harmful drug interactions. While traditional models often focus on molecular interactions, they frequently overlook real-world patient experiences. Our methodology addresses this gap by using GNNs to model complex drug interactions and incorporating sentiment analysis from the FDA's Adverse Drug Reaction database. This combined approach not only estimates the probability of DDIs but also assesses their severity, leveraging both molecular data and patient feedback. Performance metrics such as AUPR and AUC confirm that our model surpasses existing methods, offering a robust tool for improving drug safety and aiding clinical decision-making.

## Project Overview
This project leverages Graph Neural Networks (GNN) and sentiment analysis to identify DDIs and assess adverse reactions. The model integrates the DDI dataset from NCBI with adverse effect data from the FDA, processes patient demographic details, and performs sentiment analysis on feedback. This hybrid system enables precise drug interaction detection, while logistic regression-based sentiment analysis refines adverse reaction predictions, adding valuable insight into patient-reported experiences.

## Key Features
- **Graph Neural Network Modeling**: Utilizes GNN to model drug interactions based on molecular and interaction data.
- **Sentiment Analysis**: Employs logistic regression to analyze patient feedback from the FDA's ADR database, capturing sentiment polarity and intensity.
- **Enhanced Predictive Accuracy**: Combines molecular and patient-reported data for comprehensive DDI and ADR prediction.
- **Clinical Relevance**: Offers a valuable tool for clinicians to assess drug safety, minimizing adverse reactions and supporting better patient outcomes.

## Repository Structure
- `data/`: Contains preprocessed NCBI DDI and FDA ADR datasets.
- `notebooks/`: Jupyter notebooks for data exploration, model training, and performance evaluation.
- `src/`: Source code implementing GNN and sentiment analysis models.
- `results/`: Evaluation metrics, AUPR and AUC scores, and comparison results.
- `README.md`: Project documentation.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo-name.git
2. Navigate to the project directory:
    cd repo-name
3. Install dependencies:
    pip install -r requirements.txt
## Usage
Data Preparation: Load and preprocess the datasets from the data/ directory.
Train the Model: Execute the Jupyter notebooks in notebooks/ to train and evaluate the GNN and sentiment analysis models.
Evaluate: View evaluation metrics in results/.
## Results
Our integrated model outperforms existing approaches with an AUPR of 0.983 and an AUC of 0.981, demonstrating a higher predictive accuracy for DDIs and ADRs. This approach provides a comprehensive view of potential drug interactions, considering both molecular and patient-experienced insights.

## Future Improvements
Future work could refine sentiment analysis, tailor models to disease-specific drugs, and incorporate continuous learning to improve adaptability in clinical environments.

## Contributors
Abisek Kamthan R S, SRM Institute of Science and Technology
Dr. S.V. Shri Bharathi, Harith Bala, Gaurang Srivastava, Venkatadurga Pranesh B.
