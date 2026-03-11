# 🗂️ Workforce Data Filtering & Management

**Real-world inspired project** | Multi-source Data Consolidation & Filtering

---

## 📌 Project Overview

A large-scale data cleaning and filtering project involving 821 workforce 
records collected from multiple sources with inconsistent formats. 
Data was standardized, validated, and filtered for operational use.

---

## 📊 Dataset Summary

| Property | Details |
|----------|---------|
| Raw Records | 821 |
| Final Clean Records | 464 |
| Removed Records | 357 |
| Columns | 23 |
| Sources | Multiple centers with different formats |

---

## ✅ Work Performed

### 1. Multi-source Data Consolidation
- Combined data from multiple training centers
- Fixed inconsistent column formats (Bengali/English mix)
- Standardized fonts and encoding

### 2. Data Validation & Cleaning
- Mobile number format standardization & incomplete removal
- ID number validation (length & format check)
- Fixed text/number format mismatches

### 3. Filtering Pipeline (821 → 464)
- Removed incomplete mobile numbers (204 records)
- Removed incomplete ID numbers (198 records)
- Final clean dataset: 464 records

### 4. Gender-based Segmentation
- Male: 257 records
- Female: 207 records

### 5. Payment Gateway Categorization
- Method-X: 162 persons
- Method-Y: 145 persons
- Method-Z: 157 persons

### 6. Final selected Workforce List Creation
- Age range: 25–40 years
- Male volunteers: 134
- Female volunteers: 95
- Total volunteer list: 229 records

---

## 📁 Output Files

| File | Description |
|------|-------------|
| `raw_data_821.xlsx` | Original raw dataset |
| `workforce_data_processed.xlsx` | Processed file with 6 sheets |
| `generate_data.py` | Data generation script |
| `process_data.py` | Data cleaning & filtering script |

---

## 🛠️ Tools Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
```

