# Hospital Readmission Prediction using Markov Random Fields

This project aims to predict hospital readmissions using Markov Random Fields (MRFs) and compare its performance with traditional machine learning models such as Gradient Boosting.

## Dataset

The [dataset](https://www.kaggle.com/datasets/brandao/diabetes?resource=download) used in this project contains patient information, including demographic data, medical history, and hospital admission details. The data was collected from a national data warehouse that collects comprehensive clinical records across hospitals throughout the United States.

## Methodology

The project follows these main steps:

1. **Data Preprocessing:**
   - Handling missing values and data inconsistencies.

2. **Feature Engineering:**
   - Encoding categorical variables.
   - Selecting relevant features for readmission prediction.

3. **Model Development:**
   - Constructing an MRF model using the selected features.
   - Defining potential functions and edges based on domain knowledge and correlation analysis.
   - Creating a factor for the target variable 'readmitted'.

4. **Model Training and Evaluation:**
   - Training the MRF model using the preprocessed data.
   - Evaluating the model's performance using metrics such as accuracy, precision, recall, F1 score, and AUC-ROC.
   - Comparing the performance of the MRF model with traditional models like Gradient Boosting.

5. **Model Refinement:**
   - Adjusting the potential functions and edges to improve the model's performance.
   - Applying techniques like thresholding to balance the trade-off between true positives and false positives.

## Results

The MRF model achieved the following performance metrics:
- Accuracy: 0.6000
- Precision: 0.6000
- Recall: 1.0000
- F1 Score: 0.7500
- AUC-ROC: 0.2928

Compared to the Gradient Boosting model, the MRF model had a lower accuracy and AUC-ROC score but a perfect recall. The low AUC-ROC score suggests that the MRF model had a high number of false positive predictions.

To address this issue, several refinements were made to the MRF model, including:
- Adjusting the potential function for the target variable 'readmitted' to assign higher probabilities to the negative class.
- Incorporating additional features and domain knowledge to improve the model's discriminative power.
- Applying thresholding to the predicted probabilities to control the balance between true positives and false positives.

## Usage

To run the code and reproduce the results, follow these steps:

1. Install the required dependencies:
   - Python 3.11
   - pgmpy
   - numpy
   - pandas
   - scikit-learn

2. Prepare the dataset:
   - Place the dataset file in the designated directory.
   - Ensure that the dataset follows the expected format and structure.

3. Run the code:
   - Open the Jupyter Notebook `Notebook-MRF.ipynb`.
   - Execute the notebook cells in sequential order.
   - Modify the notebook as needed to adjust parameters, feature selection, and model configuration.

4. Evaluate the results:
   - Review the performance metrics displayed in the notebook.
   - Compare the results of the MRF model with other models if available.

## Future Work

- Experiment with different inference methods and elimination orders for the MRF model.
- Explore the inclusion of temporal and spatial information in the model.
- Investigate the impact of different feature selection techniques on model performance.
- Validate the model's generalizability using external datasets or cross-validation techniques.

## References

- pgmpy documentation: [https://pgmpy.org/](https://pgmpy.org/)
- scikit-learn documentation: [https://scikit-learn.org/](https://scikit-learn.org/)
