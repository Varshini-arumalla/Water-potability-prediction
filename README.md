# Water-potability-prediction
Developed a machine learning model to classify water quality using Python. Collected and preprocessed data, engineered features, and trained classification models to determine the potability of water. Achieved high accuracy with effective use of scikit-learn.
# Water Potability Prediction App

This Streamlit web app predicts whether water is potable (safe to drink) based on various chemical and physical parameters. It uses a pre-trained machine learning model to classify water samples as either safe or unsafe.

## Features

- User-friendly Streamlit interface.
- Inputs for parameters like pH, hardness, solids, turbidity, etc.
- Real-time prediction using a trained ML model.
- Displays clear visual feedback on water safety.

## Tech Stack

- Python
- Streamlit
- NumPy
- Scikit-learn (for model and scaler)
- Pickle (for loading model and scaler)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/water-potability-predictor.git
   cd water-potability-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure the following files are present:
   - water_model.pkl: Pre-trained ML model file
   - scaler.pkl: Fitted scaler for input normalization

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Input Parameters

| Parameter         | Description                          |
|------------------|--------------------------------------|
| pH               | Acidity/basicity of water (0–14)     |
| Hardness         | Concentration of calcium & magnesium |
| Solids           | Total dissolved solids in ppm        |
| Chloramines      | Disinfectants in water (ppm)         |
| Sulfate          | Sulfate ions concentration (mg/L)    |
| Conductivity     | Ability to conduct electricity       |
| Organic Carbon   | Organic content (ppm)                |
| Trihalomethanes  | Harmful chemical compounds (μg/L)    |
| Turbidity        | Clarity of water (NTU)               |

## Sample Output

- The water is potable (safe to drink).
- The water is not potable (unsafe to drink).

## Project Structure

```
water-potability-predictor/
│
├── app.py               # Streamlit application script
├── water_model.pkl      # Trained ML model (binary classification)
├── scaler.pkl           # Scaler used for input normalization
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
```

## Contributing

Feel free to fork the project and submit pull requests.

## License

This project is open-source under the MIT License.
