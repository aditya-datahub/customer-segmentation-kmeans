# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project performs **customer segmentation** using **K-Means Clustering** on retail customer data.
The goal is to group customers into meaningful segments based on their demographics, spending behavior, and purchase patterns.

This helps businesses:

* Identify high-value customers
* Target the right audience
* Improve marketing strategies

---

## 📁 Data Understanding

This project clearly separates **raw input data** and **processed output data**:

### 🔹 Raw Dataset

* `data/raw_customer_data.csv`
* Contains original customer data (age, income, purchases, etc.)
* Used for data cleaning, EDA, and model building

### 🔹 Processed Output

* `data/customer_segments_output.csv`
* Generated after applying clustering
* Includes a new **"Segment"** column with customer group labels

📌 Workflow:
**Raw Data → Analysis → Clustering → Segmented Output**

---

## 🔄 Project Pipeline

```text
raw_customer_data.csv
        ↓
customer_segmentation.ipynb
(EDA + Feature Engineering)
        ↓
KMeans Model (kmeans_model.pkl + scaler.pkl)
        ↓
segmentation.py (Streamlit App)
        ↓
customer_segments_output.csv
```
---

## 🛠️ Tech Stack

`Python` • `Pandas` • `NumPy` • `Matplotlib` • `Seaborn` • `Scikit-learn (KMeans, PCA, StandardScaler)` • `Streamlit` • `Joblib`

---

## 📊 Steps Performed

1. Data Cleaning

   * Handled missing values and duplicates
   * Removed outliers using IQR

2. Feature Engineering

   * Created meaningful features like total spending

3. Exploratory Data Analysis (EDA)

   * Distribution plots
   * Correlation analysis

4. Clustering

   * Used **Elbow Method** and **Silhouette Score** to find optimal clusters
   * Applied **K-Means Clustering**

5. Dimensionality Reduction

   * Used **PCA** for visualization

6. Deployment

   * Built an interactive **Streamlit app** for live predictions

---

## 🏷️ Customer Segments

| Segment              | Description                |
| -------------------- | -------------------------- |
| 💎 Premium Customers | High income, high spending |
| 💰 Budget Shoppers   | Low income, low spending   |
| 🌐 Digital Buyers    | Prefer online shopping     |
| 😴 Dormant Customers | Inactive customers         |

---

## 🚀 Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit App

```bash
streamlit run segmentation.py
```

---

## 📂 Project Structure

```
customer-segmentation-eda/
│
├── data/
│   ├── raw_customer_data.csv
│   └── customer_segments_output.csv
│
├── customer_segmentation.ipynb
├── segmentation.py
├── kmeans_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## 📈 Future Improvements

* Add more features for better segmentation
* Try advanced clustering (DBSCAN, Hierarchical)
* Deploy app online (Streamlit Cloud)

---

## 🤝 Contributing

Feel free to fork this repo and improve it.

---

## 📜 License

This project is licensed under the MIT License.
