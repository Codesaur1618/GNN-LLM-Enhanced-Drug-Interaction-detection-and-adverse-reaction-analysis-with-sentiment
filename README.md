# GNN-Enhanced Drug Interaction Detection and Adverse Reaction Analysis with Sentiment Insights

## Overview
This project leverages **Graph Neural Networks (GNNs)** to detect drug interactions and analyze adverse reactions. It incorporates sentiment analysis to enhance the interpretation of reported drug effects using diverse datasets.

## Features
- **Graph-based modeling** for drug interaction predictions.
- **Sentiment analysis** of adverse drug reactions.
- **Deep learning techniques** for improved accuracy.
- **Integration of multiple datasets** for comprehensive analysis.

## Dataset Sources
- **Drug Interaction Dataset**: [DrugBank](https://www.drugbank.ca/)
- **Adverse Drug Reactions**: [SIDER](http://sideeffects.embl.de/)
- **Sentiment Analysis Data**: [PubMed & Medline](https://www.ncbi.nlm.nih.gov/)   

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
## License
This project is licensed under the MIT License.
