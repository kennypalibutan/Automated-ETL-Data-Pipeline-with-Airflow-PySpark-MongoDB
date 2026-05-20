# ⚙️ Automated ETL Data Pipeline with Airflow, PySpark & MongoDB

## 📌 Project Overview

The objective of this project is to build an automated ETL (Extract, Transform, Load) data pipeline using Apache Airflow, PySpark, Great Expectations, and MongoDB. The pipeline automates data extraction, transformation, validation, and loading processes for analytical and operational purposes.

This project demonstrates practical implementation of modern Data Engineering workflows, including orchestration, distributed data processing, and NoSQL database integration.

---

# 🎯 Project Objectives

* Build an automated ETL pipeline using Apache Airflow.
* Perform data extraction and transformation using PySpark.
* Validate dataset quality using Great Expectations.
* Store transformed data into MongoDB Atlas.
* Create a scalable and modular data engineering workflow.

---

# 🛠️ Technologies Used

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| Python             | Main programming language     |
| PySpark            | Distributed data processing   |
| Apache Airflow     | Workflow orchestration        |
| Great Expectations | Data validation               |
| MongoDB Atlas      | NoSQL database                |
| PyMongo            | MongoDB connection            |
| Pandas             | Exploratory data analysis     |
| Jupyter Notebook   | Data exploration & validation |
| CSV                | Raw dataset source            |

---

# 📂 Project Structure

```bash
├── EDA & Great Expectations
├── Extract Script.py
├── Transform Script.py
├── Load Script.py
├── Airflow DAG
├── DAG Graph.jpg
├── MongoDB Screenshot.jpg
├── README.md
```

---

# 🔍 Exploratory Data Analysis (EDA)

Before automation, exploratory data analysis was performed to understand:

* Data structure
* Missing values
* Data types
* Duplicate records
* Outliers and inconsistencies

The analysis was used to determine appropriate data cleaning and transformation steps for the ETL pipeline.

---

# ✅ Data Validation with Great Expectations

Data quality validation was implemented using Great Expectations.

### Validation Rules Included

* Column uniqueness validation
* Numeric range validation
* Accepted categorical values validation
* Data type validation
* Null value validation
* Regex pattern validation
* Row count validation

All expectations were successfully validated with:

```python
success: true
```

---

# ⚙️ ETL Pipeline Workflow

## 1️⃣ Extract

The extraction process reads raw CSV data using PySpark.

### Key Features

* SparkSession initialization
* Efficient CSV loading
* Schema inference
* Distributed data processing

---

## 2️⃣ Transform

The transformation stage performs data cleaning and preprocessing using PySpark only.

### Data Processing Steps

* Handle missing values
* Remove duplicates
* Rename columns
* Convert data types
* Standardize text formatting
* Filter invalid records

The transformed dataset is prepared for analytics and database storage.

---

## 3️⃣ Load

The final transformed dataset is stored into MongoDB Atlas using PyMongo.

### Database Activities

* MongoDB connection setup
* Convert Spark DataFrame to dictionary/JSON format
* Insert data into MongoDB collection
* Validate successful insertion

---

# 🔄 Workflow Orchestration with Apache Airflow

The ETL process is fully automated using Apache Airflow DAG.

### DAG Tasks

| Task      | Description             |
| --------- | ----------------------- |
| Extract   | Load raw dataset        |
| Transform | Clean and process data  |
| Load      | Store data into MongoDB |

### Scheduling Configuration

* Start Date: 1 November 2024
* Schedule:

  * Every Saturday
  * Every 10 minutes
  * Between 09:10 AM – 09:30 AM

### DAG Flow

```text
Extract → Transform → Load
```

---

# 📊 Sample Pipeline Architecture

```text
CSV Dataset
     ↓
PySpark Extraction
     ↓
PySpark Transformation
     ↓
Great Expectations Validation
     ↓
MongoDB Atlas
     ↓
Automated by Apache Airflow
```

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/your-repository.git
```

## 2. Install Dependencies

```bash
pip install pyspark airflow great-expectations pymongo pandas
```

## 3. Run Airflow

```bash
airflow standalone
```

## 4. Trigger DAG

Run the DAG from:

* Airflow UI
* CLI
* Scheduled execution

---

# 📈 Skills Demonstrated

* ETL Pipeline Development
* Workflow Automation
* Apache Airflow Orchestration
* Distributed Data Processing with PySpark
* Data Validation using Great Expectations
* NoSQL Database Integration
* MongoDB Atlas Integration
* Data Cleaning & Transformation
* Python Scripting
* Data Engineering Best Practices

---

# 📚 Learning Outcomes

Through this project, I learned:

* How to build automated ETL workflows
* Airflow DAG orchestration
* Distributed data processing using PySpark
* Data quality validation techniques
* MongoDB integration for NoSQL storage
* Modular pipeline architecture design

---

# 🧠 Future Improvements

Possible future enhancements:

* Docker containerization
* CI/CD integration
* Cloud deployment (AWS/GCP/Azure)
* Real-time streaming pipeline
* Logging & monitoring system
* Data warehouse integration
* Unit testing implementation

---

# 👤 Author

**Kenny Palibutan**

Aspiring Data Engineer / Data Analyst passionate about automation, scalable data systems, and modern data pipelines.

---

# ⭐ Repository Purpose

This repository is intended for:

* Portfolio showcase
* Demonstrating Data Engineering skills
* Learning documentation
* ETL automation practice
* Airflow & PySpark implementation reference
