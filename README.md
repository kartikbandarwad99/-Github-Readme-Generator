# Product Hunt Post Success Prediction and Comment Generation

## Description

This project analyzes Product Hunt post data to predict post success and generate synthetic comments based on existing ones. It leverages the Product Hunt API to collect data on top and recent posts, performs exploratory data analysis (EDA) to understand post characteristics, and builds a classification model to predict post success based on features like launch day, vote count, comment count, and topics. Additionally, it trains a character-level language model on post comments to generate new text, mimicking the style and content of the original comments.

## File Structure

```
.
├── EDA_and_classification_model.ipynb       # Notebook for EDA and classification model training
├── char_level_model.py                    # Script for training the character-level language model
├── helper_funcs.py                        # Python file containing helper functions for API interaction and data processing
├── microtorch.py                           # Python file implementing a minimal PyTorch-like neural network library
└── top_posts_data.json                   # Example JSON file containing Product Hunt Post data (replace with your actual data file)
```

## Installation

1. Clone this repository: `git clone https://github.com/your-username/your-repo-name.git`
2. Navigate to the project directory: `cd your-repo-name`
3. Install required libraries: `pip install -r requirements.txt` (Create a `requirements.txt` file listing necessary libraries like pandas, scikit-learn, xgboost, requests, and any others used in the project)

## Usage

### EDA and Classification

1. Open and run the `EDA_and_classification_model.ipynb` notebook. This will fetch data from the Product Hunt API, perform EDA, preprocess the data, train the XGBoost classification model, and evaluate its performance.
2. Modify the date range and other parameters in the notebook as needed.

### Comment Generation

1. Run the `char_level_model.py` script to train the character-level language model. This script will read comment data from `top_posts_data.json` (or your specified data file), preprocess the text, train the model, and save the trained model (optional). You will likely need to adjust the file paths within the script to match your setup.
2. After training, you can use the `generate_text` function (within the script) to generate new text based on the trained model.


## Contributing

Contributions are welcome!  Please feel free to submit pull requests for bug fixes, feature enhancements, or documentation improvements.  When submitting a pull request, ensure your code is well-documented and follows the existing coding style.

## License

This project is licensed under the [MIT License](LICENSE).  (Create a LICENSE file in the root directory containing the MIT License text). 
