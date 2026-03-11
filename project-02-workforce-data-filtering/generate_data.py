import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

training_centers = ['Center-A', 'Center-B', 'Center-C', 'Center-D']
staff_categories = ['Type-A', 'Type-B', 'Type-C', 'Type-D']
payment_methods = ['Method-X', 'Method-Y', 'Method-Z']
mfs_owner = ['Self', 'Spouse', 'Father']
education = ['SSC', 'HSC', 'Graduate', 'Class-8']
municipality = ['Municipality-1', 'Municipality-2', 'Municipality-3']
zone_areas = ['Zone-North', 'Zone-South', 'Zone-East', 'Zone-West']
sub_zones = ['Sub-Zone-1', 'Sub-Zone-2', 'Sub-Zone-3']
genders = ['Male', 'Female']

rows = []
for i in range(1, 822):
    gender = random.choice(genders)
    mobile_complete = random.choice([True, True, True, False])
    id_complete = random.choice([True, True, True, False])

    mobile = '01' + str(random.choice([3,4,5,6,7,8,9])) + \
             ''.join([str(random.randint(0,9)) for _ in range(8)]) \
             if mobile_complete else \
             '01' + ''.join([str(random.randint(0,9)) for _ in range(7)])

    id_num = ''.join([str(random.randint(0,9)) for _ in range(17)]) \
             if id_complete else \
             ''.join([str(random.randint(0,9)) for _ in range(13)])

    dob_year = random.randint(1970, 2000)
    age = 2024 - dob_year
    dob = f"{dob_year}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"

    payment_acc = '01' + str(random.choice([3,5,8])) + \
                  ''.join([str(random.randint(0,9)) for _ in range(8)])

    rows.append({
        'Serial No': i,
        'Full Name': fake.name(),
        'Father/Husband Name': fake.name(),
        'Mother Name': fake.name(),
        'Gender': gender,
        'Date of Birth': dob,
        'Age': age,
        'ID Number': id_num,
        'Education': random.choice(education),
        'Staff Category': random.choice(staff_categories),
        'Basic Training': random.choice(['Yes', 'No']),
        'Technical Training': random.choice(['Yes', 'No']),
        'Training Center': random.choice(training_centers),
        'Training Year': random.randint(2015, 2023),
        'Municipality': random.choice(municipality),
        'Zone Area': random.choice(zone_areas),
        'Sub-Zone': random.choice(sub_zones),
        'Sub-Zone No': random.randint(1, 3),
        'Village/Area': fake.city(),
        'Mobile Number': mobile,
        'Payment Method': random.choice(payment_methods),
        'Payment Account': payment_acc,
        'Account Owner': random.choice(mfs_owner),
    })

df = pd.DataFrame(rows)
df.to_excel('raw_data_821.xlsx', index=False)
print(f"✅ Done! raw_data_821.xlsx created with {len(df)} rows.")
print(f"   Male:   {len(df[df['Gender']=='Male'])}")
print(f"   Female: {len(df[df['Gender']=='Female'])}")
print(f"   Incomplete Mobile: {len(df[df['Mobile Number'].str.len() < 11])}")
print(f"   Incomplete ID:     {len(df[df['ID Number'].str.len() < 17])}")