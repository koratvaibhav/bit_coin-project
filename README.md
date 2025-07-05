# bit_coin-project


---

## 🧠 Machine Learning Overview

- **Problem Type**: Binary Classification
- **Target**: Whether the stock price will increase the next day
- **Features**:
  - `open-close`: Difference between open and close price
  - `low-high`: Difference between low and high price
  - `is_quarter_end`: Flag for quarter-end month

- **Models Used**:
  - Logistic Regression
  - Support Vector Classifier (SVC with Polynomial Kernel)
  - XGBoost Classifier

- **Best Accuracy (AUC)**: Evaluated using ROC-AUC on training and validation sets

---

## 🛠️ Tech Stack

| Category        | Technologies                   |
|----------------|--------------------------------|
| **Language**    | Python                         |
| **Libraries**   | Pandas, NumPy, scikit-learn, XGBoost, Seaborn, Matplotlib |
| **Web Framework** | Flask                        |
| **Deployment** | (Optional) Render / Heroku     |

---

## 🧾 Project Structure



---

## ⚙️ How to Run Locally

1. Clone the repository

####bash
git clone https://github.com/your-username/tesla-stock-predictor.git
cd tesla-stock-predictor
Install required libraries

pip install -r requirements.txt

python app.py
