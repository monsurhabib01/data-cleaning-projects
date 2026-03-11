import pandas as pd

# Load raw data
df = pd.read_excel('raw_data_821.xlsx', dtype=str)
print(f"Raw data: {len(df)} rows")

# Step 1: Remove incomplete mobile (less than 11 digits)
df['Mobile Number'] = df['Mobile Number'].str.strip()
df_clean = df[df['Mobile Number'].str.len() == 11]
print(f"After mobile filter: {len(df_clean)} rows")

# Step 2: Remove incomplete ID (less than 17 digits)
df_clean = df_clean.copy()
df_clean['ID Number'] = df_clean['ID Number'].str.strip()
df_clean = df_clean[df_clean['ID Number'].str.len() == 17]
print(f"After ID filter: {len(df_clean)} rows")

# Step 3: Select first 500
removed = df[~df['Serial No'].isin(df_clean['Serial No'])]
df_500 = df_clean.head(500)
print(f"Final selected: {len(df_500)} rows")

# Step 4: Gender split
male = df_500[df_500['Gender'] == 'Male']
female = df_500[df_500['Gender'] == 'Female']
print(f"Male: {len(male)} | Female: {len(female)}")

# Step 5: Payment gateway split
for method in ['Method-X', 'Method-Y', 'Method-Z']:
    count = df_500[df_500['Payment Method'] == method]
    print(f"{method}: {len(count)} persons")

# Step 6: Volunteer list (Age 25-40, 250M + 250F)
df_500 = df_500.copy()
df_500['Age'] = df_500['Age'].astype(int)
volunteers_m = df_500[(df_500['Gender']=='Male') &
                       (df_500['Age']>=25) &
                       (df_500['Age']<=40)].head(250)
volunteers_f = df_500[(df_500['Gender']=='Female') &
                       (df_500['Age']>=25) &
                       (df_500['Age']<=40)].head(250)
volunteers = pd.concat([volunteers_m, volunteers_f])
print(f"Volunteer list: {len(volunteers)} (M:{len(volunteers_m)} F:{len(volunteers_f)})")

# Save all outputs
with pd.ExcelWriter('workforce_data_processed.xlsx') as writer:
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    df_500.to_excel(writer, sheet_name='Clean Data 500', index=False)
    removed.to_excel(writer, sheet_name='Removed Data', index=False)
    male.to_excel(writer, sheet_name='Male', index=False)
    female.to_excel(writer, sheet_name='Female', index=False)
    volunteers.to_excel(writer, sheet_name='Volunteer List', index=False)