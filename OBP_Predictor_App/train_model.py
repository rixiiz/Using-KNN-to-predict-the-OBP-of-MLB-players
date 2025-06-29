import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

# Load your CSVs
april_df = pd.read_csv("april.csv", encoding='cp861', sep=';')
fullseason_df = pd.read_csv("Fullseason.csv", encoding='cp861', sep=';')

# Preprocessing
april_df = april_df.drop_duplicates(subset=['Name'])
fullseason_df = fullseason_df.drop_duplicates(subset=['Name'])
common_names = set(april_df['Name']).intersection(set(fullseason_df['Name']))
april_filtered = april_df[april_df['Name'].isin(common_names)]
fullseason_filtered = fullseason_df[fullseason_df['Name'].isin(common_names)]

# Merge
april_selected = april_filtered[['Name', 'AVG', 'SLG']]
fullseason_selected = fullseason_df[['Name', 'OBP']]
merged = pd.merge(april_selected, fullseason_selected, on='Name')

X = merged[['AVG', 'SLG']].values
y = merged['OBP'].values

# Train and scale
X_train, _, y_train, _ = train_test_split(X, y, random_state=0, test_size=0.2)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = KNeighborsRegressor(n_neighbors=7, metric='minkowski', p=2)
model.fit(X_train_scaled, y_train)

# Save model + scaler
with open("model_bundle.pkl", "wb") as f:
    pickle.dump({"scaler": scaler, "model": model}, f)

print("✅ Model trained and saved as model_bundle.pkl")