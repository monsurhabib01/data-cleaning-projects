# Project 03 — Retail Sales Data Cleaning

**Tools:** Python · Pandas · NumPy  
**Dataset:** 1,280-row retail sales data (simulated real-world messy data)  
**Output:** Clean, analysis-ready CSV with full audit trail

---

## Problem

Raw sales data collected from multiple sources contained:

- **2 duplicate rows** — same order recorded twice
- **204 missing values** across category, region, payment method, customer ID
- **4 inconsistent date formats** mixed in one column (YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY, DD-Mon-YYYY)
- **15 variations** of 3 category names (e.g. `electronics`, `ELECTRONICS`, `Electronis`, `Electronic`)
- **22 variations** of 5 region names (e.g. `N`, `north`, `NORTH`, `Nort`)
- **25 invalid quantity entries** (zero or negative values)
- **Incorrect total_price** values due to bad quantities

---

## What I Did

| Step | Action | Result |
|------|--------|--------|
| 1 | Removed duplicate rows | 2 rows dropped |
| 2 | Standardized 4 date formats → YYYY-MM-DD | 0 invalid dates |
| 3 | Normalized 15 category variations → 3 clean values | 0 missing |
| 4 | Normalized 22 region variations → 5 clean values | 0 missing |
| 5 | Standardized payment method naming | 5 clean categories |
| 6 | Removed invalid quantity rows (≤ 0) | 25 rows dropped |
| 7 | Recalculated total_price from quantity × unit_price | Accurate totals |
| 8 | Filled remaining nulls (mode / product lookup) | 0 nulls remaining |
| 9 | Added derived columns: month, year | Analysis-ready |

---

## Results

| Metric | Before | After |
|--------|--------|-------|
| Rows | 1,280 | 1,253 |
| Missing values | 204 | 0 |
| Duplicate rows | 2 | 0 |
| Date formats | 4 mixed | 1 standard |
| Category variations | 15 | 3 |
| Region variations | 22 | 5 |
| Invalid quantities | 25 | 0 |

**Total revenue (clean data): $1,091,122.62**

---

## Files

```
project-03-sales-data-cleaning/
├── raw_sales_data.csv          ← Original messy data
├── clean_sales_data.csv        ← Cleaned output
├── sales_data_cleaning.py      ← Main cleaning script
└── README.md
```

---

## How to Run

```bash
pip install pandas numpy
python sales_data_cleaning.py
```

---

## Author

**Mohammad Monsur Habib** — Freelance Data Analyst  
[github.com/monsurhabib01](https://github.com/monsurhabib01)
