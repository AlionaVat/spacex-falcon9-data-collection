# 🚀 SpaceX Falcon 9 Data Collection using API

## 📌 Overview

This project focuses on collecting and preparing SpaceX Falcon 9 launch data using the public SpaceX REST API.

The goal is to build a clean and structured dataset that can later be used for exploratory analysis, visualization, and machine learning models aimed at predicting the success of Falcon 9 first-stage landings.

The project demonstrates practical experience working with APIs, data extraction, data cleaning, and dataset preparation using Python.

---

## 🎯 Objectives

- Collect launch data from the SpaceX REST API
- Extract relevant launch and rocket information
- Clean and transform raw API responses
- Create a structured dataset for further analysis
- Prepare data for future predictive modeling

---

## 🧠 Methodology

### Data Collection

Launch information was retrieved directly from the SpaceX public API using HTTP requests.

Data collected includes:

- Launch dates
- Flight numbers
- Rocket information
- Payload details
- Launch sites
- Booster versions
- Landing outcomes
- Orbit information

---

### Data Processing

The following preprocessing steps were performed:

- JSON response parsing
- Missing value handling
- Data transformation
- Column standardization
- Feature extraction
- Data validation

---

### Data Cleaning

The dataset was refined by:

- Removing unnecessary fields
- Handling null values
- Formatting dates
- Standardizing categorical variables
- Creating analysis-ready features

---

## 📊 Dataset Features

Examples of extracted attributes:

- Flight Number
- Launch Date
- Booster Version
- Payload Mass
- Orbit
- Launch Site
- Landing Outcome
- Reused Booster
- Success Indicator

---

## 🧰 Technologies Used

- Python
- Requests
- Pandas
- NumPy
- Jupyter Notebook
- REST API

---

## 📂 Project Structure

```text
spacex-data-collection-api/
│
├── jupyter-labs-spacex-data-collection-api.ipynb
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/your-username/spacex-data-collection-api.git
```

Navigate to the project directory:

```bash
cd spacex-data-collection-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Step 1: Launch Jupyter Notebook

```bash
jupyter notebook
```

### Step 2: Open

```text
jupyter-labs-spacex-data-collection-api.ipynb
```

### Step 3: Run all notebook cells

---

## 🔄 Workflow

```text
SpaceX API
      ↓
Data Extraction
      ↓
JSON Processing
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Structured Dataset
      ↓
Analysis & Modeling Preparation
```

---

## 📈 Key Outcomes

- Successfully connected to the SpaceX API
- Retrieved launch-related data programmatically
- Built a clean and structured dataset
- Prepared data for future analysis and machine learning tasks
- Demonstrated practical API integration and data wrangling skills

---

## 🚀 Future Improvements

- Automated data refresh pipeline
- Data visualization dashboard
- Launch success prediction model
- Interactive analytics application
- Real-time SpaceX launch monitoring

---

## 👩‍💻 Author

**Aliona V.**

Software Engineering | Data Engineering | Data Science | Backend Development

---

## 📄 License
