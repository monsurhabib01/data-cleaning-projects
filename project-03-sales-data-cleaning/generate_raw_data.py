import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n = 1200

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'USB Hub', 'Charger', 'Desk Lamp', 'Notebook']
categories = {'Laptop': 'Electronics', 'Mouse': 'Accessories', 'Keyboard': 'Accessories',
              'Monitor': 'Electronics', 'Headphones': 'Accessories', 'Webcam': 'Electronics',
              'USB Hub': 'Accessories', 'Charger': 'Accessories', 'Desk Lamp': 'Office', 'Notebook': 'Office'}
prices = {'Laptop': 950, 'Mouse': 25, 'Keyboard': 55, 'Monitor': 320, 'Headphones': 80,
          'Webcam': 70, 'USB Hub': 35, 'Charger': 20, 'Desk Lamp': 30, 'Notebook': 10}
regions = ['North', 'South', 'East', 'West', 'Central']
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash']

# Generate base data
order_ids = [f'ORD-{1000+i}' for i in range(n)]
product_list = [random.choice(products) for _ in range(n)]
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=random.randint(0, 364)) for _ in range(n)]

df = pd.DataFrame({
    'order_id': order_ids,
    'date': dates,
    'product': product_list,
    'category': [categories[p] for p in product_list],
    'quantity': [random.randint(1, 10) for _ in range(n)],
    'unit_price': [prices[p] + random.uniform(-5, 15) for p in product_list],
    'region': [random.choice(regions) for _ in range(n)],
    'payment_method': [random.choice(payment_methods) for _ in range(n)],
    'customer_id': [f'CUST-{random.randint(100, 500)}' for _ in range(n)],
})
df['total_price'] = df['quantity'] * df['unit_price']

# === INJECT REAL MESSY DATA PROBLEMS ===

# 1. Duplicate rows (80 duplicates)
dup_indices = np.random.choice(n, 80, replace=False)
duplicates = df.iloc[dup_indices].copy()
df = pd.concat([df, duplicates], ignore_index=True)

# 2. Missing values
for col, pct in [('region', 0.05), ('payment_method', 0.04), ('customer_id', 0.03), ('category', 0.04)]:
    null_idx = np.random.choice(len(df), int(len(df)*pct), replace=False)
    df.loc[null_idx, col] = np.nan

# 3. Inconsistent date formats
date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y', '%d-%b-%Y']
def random_date_format(d):
    fmt = random.choice(date_formats)
    return d.strftime(fmt)

df['date'] = df['date'].apply(random_date_format)

# 4. Inconsistent category names
cat_noise = {'Electronics': ['electronics', 'ELECTRONICS', 'Electronic', 'Electronis'],
             'Accessories': ['accessories', 'ACCESSORIES', 'Accessory', 'Acessories'],
             'Office': ['office', 'OFFICE', 'Office Supplies', 'Ofice']}
def mess_category(c):
    if pd.isna(c): return c
    for k, v in cat_noise.items():
        if c == k and random.random() < 0.3:
            return random.choice(v)
    return c
df['category'] = df['category'].apply(mess_category)

# 5. Negative/zero quantities (bad entries)
bad_idx = np.random.choice(len(df), 25, replace=False)
df.loc[bad_idx, 'quantity'] = [random.choice([-1, -2, 0]) for _ in range(25)]

# 6. Inconsistent region names
region_noise = {'North': ['north', 'NORTH', 'N', 'Nort'],
                'South': ['south', 'SOUTH', 'S', 'Sout'],
                'East': ['east', 'EAST', 'E'],
                'West': ['west', 'WEST', 'W'],
                'Central': ['central', 'CENTRAL', 'Cent']}
def mess_region(r):
    if pd.isna(r): return r
    for k, v in region_noise.items():
        if r == k and random.random() < 0.25:
            return random.choice(v)
    return r
df['region'] = df['region'].apply(mess_region)

# 7. Mixed payment method naming
pay_noise = {'Credit Card': ['credit card', 'CC', 'Credit card', 'CreditCard'],
             'PayPal': ['paypal', 'PAYPAL', 'Pay Pal', 'Paypal']}
def mess_payment(p):
    if pd.isna(p): return p
    for k, v in pay_noise.items():
        if p == k and random.random() < 0.2:
            return random.choice(v)
    return p
df['payment_method'] = df['payment_method'].apply(mess_payment)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv('raw_sales_data.csv', index=False)
print(f"Raw data generated: {len(df)} rows")
print(f"Nulls:\n{df.isnull().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")
