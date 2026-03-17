import pandas as pd
import numpy as np

# ============================================================
# PROJECT-03: Retail Sales Data Cleaning
# Author: Mohammad Monsur Habib
# GitHub: github.com/monsurhabib01
# ============================================================

# ── STEP 1: Load Raw Data ──────────────────────────────────
df = pd.read_csv('raw_sales_data.csv')

print("=" * 55)
print("RETAIL SALES DATA CLEANING REPORT")
print("=" * 55)
print(f"\n[1] RAW DATA LOADED")
print(f"    Rows: {len(df):,}")
print(f"    Columns: {list(df.columns)}")

# ── STEP 2: Audit Before Cleaning ─────────────────────────
print(f"\n[2] PRE-CLEANING AUDIT")
print(f"    Duplicate rows     : {df.duplicated().sum()}")
print(f"    Missing values     :\n{df.isnull().sum()[df.isnull().sum() > 0].to_string()}")
print(f"    Negative quantity  : {(df['quantity'] <= 0).sum()}")
print(f"    Unique categories  : {df['category'].dropna().unique()}")
print(f"    Unique regions     : {df['region'].dropna().unique()}")

initial_rows = len(df)

# ── STEP 3: Remove Duplicates ─────────────────────────────
df.drop_duplicates(inplace=True)
print(f"\n[3] DUPLICATES REMOVED: {initial_rows - len(df)} rows dropped")

# ── STEP 4: Standardize Date Format ───────────────────────
def parse_date(d):
    for fmt in ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y', '%d-%b-%Y']:
        try:
            return pd.to_datetime(d, format=fmt)
        except:
            continue
    return pd.NaT

df['date'] = df['date'].apply(parse_date)
df['date'] = pd.to_datetime(df['date'])
print(f"\n[4] DATE FORMAT STANDARDIZED → YYYY-MM-DD")
print(f"    Invalid dates: {df['date'].isna().sum()}")

# ── STEP 5: Standardize Category ──────────────────────────
category_map = {
    'electronics': 'Electronics', 'ELECTRONICS': 'Electronics',
    'electronic': 'Electronics', 'electronis': 'Electronics',
    'accessories': 'Accessories', 'ACCESSORIES': 'Accessories',
    'accessory': 'Accessories', 'acessories': 'Accessories',
    'office': 'Office', 'OFFICE': 'Office',
    'office supplies': 'Office', 'ofice': 'Office'
}
df['category'] = df['category'].str.strip()
df['category'] = df['category'].apply(
    lambda x: category_map.get(str(x).lower(), x) if pd.notna(x) else x
)
# Fill missing categories from product mapping
product_category = {
    'Laptop': 'Electronics', 'Monitor': 'Electronics', 'Webcam': 'Electronics',
    'Mouse': 'Accessories', 'Keyboard': 'Accessories', 'Headphones': 'Accessories',
    'USB Hub': 'Accessories', 'Charger': 'Accessories',
    'Desk Lamp': 'Office', 'Notebook': 'Office'
}
df['category'] = df.apply(
    lambda r: product_category.get(r['product'], r['category']) if pd.isna(r['category']) else r['category'],
    axis=1
)
print(f"\n[5] CATEGORY STANDARDIZED")
print(f"    Unique values: {sorted(df['category'].unique())}")
print(f"    Missing remaining: {df['category'].isna().sum()}")

# ── STEP 6: Standardize Region ────────────────────────────
region_map = {
    'north': 'North', 'NORTH': 'North', 'n': 'North', 'nort': 'North',
    'south': 'South', 'SOUTH': 'South', 's': 'South', 'sout': 'South',
    'east': 'East',  'EAST': 'East',  'e': 'East',
    'west': 'West',  'WEST': 'West',  'w': 'West',
    'central': 'Central', 'CENTRAL': 'Central', 'cent': 'Central'
}
df['region'] = df['region'].str.strip()
df['region'] = df['region'].apply(
    lambda x: region_map.get(str(x).lower(), x) if pd.notna(x) else x
)
# Fill missing region with mode
region_mode = df['region'].mode()[0]
df['region'] = df['region'].fillna(region_mode)
print(f"\n[6] REGION STANDARDIZED")
print(f"    Unique values: {sorted(df['region'].dropna().unique())}")

# ── STEP 7: Standardize Payment Method ────────────────────
payment_map = {
    'credit card': 'Credit Card', 'cc': 'Credit Card', 'creditcard': 'Credit Card',
    'paypal': 'PayPal', 'pay pal': 'PayPal', 'PAYPAL': 'PayPal',
    'debit card': 'Debit Card', 'bank transfer': 'Bank Transfer', 'cash': 'Cash'
}
df['payment_method'] = df['payment_method'].str.strip()
df['payment_method'] = df['payment_method'].apply(
    lambda x: payment_map.get(str(x).lower(), x) if pd.notna(x) else x
)
pay_mode = df['payment_method'].mode()[0]
df['payment_method'] = df['payment_method'].fillna(pay_mode)
print(f"\n[7] PAYMENT METHOD STANDARDIZED")
print(f"    Unique values: {sorted(df['payment_method'].unique())}")

# ── STEP 8: Remove Invalid Quantities ─────────────────────
invalid_qty = (df['quantity'] <= 0).sum()
df = df[df['quantity'] > 0]
print(f"\n[8] INVALID QUANTITIES REMOVED: {invalid_qty} rows dropped")

# ── STEP 9: Recalculate Total Price ───────────────────────
df['unit_price'] = df['unit_price'].round(2)
df['total_price'] = (df['quantity'] * df['unit_price']).round(2)
print(f"\n[9] TOTAL PRICE RECALCULATED")

# ── STEP 10: Fill Remaining Missing Values ────────────────
df['customer_id'] = df['customer_id'].fillna('UNKNOWN')
print(f"\n[10] REMAINING NULLS HANDLED")
print(f"     Missing values: {df.isnull().sum().sum()}")

# ── STEP 11: Add Derived Columns ──────────────────────────
df['month'] = df['date'].dt.month_name()
df['year'] = df['date'].dt.year
print(f"\n[11] DERIVED COLUMNS ADDED: month, year")

# ── STEP 12: Final Audit ──────────────────────────────────
print(f"\n[12] POST-CLEANING AUDIT")
print(f"     Rows remaining  : {len(df):,}")
print(f"     Rows removed    : {initial_rows - len(df):,}")
print(f"     Duplicates      : {df.duplicated().sum()}")
print(f"     Missing values  : {df.isnull().sum().sum()}")
print(f"     Date range      : {df['date'].min().date()} → {df['date'].max().date()}")
print(f"     Total revenue   : ${df['total_price'].sum():,.2f}")

# ── STEP 13: Summary Stats ────────────────────────────────
print(f"\n[13] SUMMARY STATISTICS")
print(f"\n  Top products by revenue:")
print(df.groupby('product')['total_price'].sum().sort_values(ascending=False).head(5).to_string())
print(f"\n  Sales by region:")
print(df.groupby('region')['total_price'].sum().sort_values(ascending=False).to_string())
print(f"\n  Payment method distribution:")
print(df['payment_method'].value_counts().to_string())

# ── SAVE CLEAN DATA ───────────────────────────────────────
df.to_csv('clean_sales_data.csv', index=False)
print(f"\n{'='*55}")
print(f"CLEAN DATA SAVED → clean_sales_data.csv")
print(f"{'='*55}")
