import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

# ===== 1. Load Data =====
file_path = "data.csv"
data = pd.read_csv(file_path)
print(data.head(5))

# Plot distribution of target
sns.countplot(y='NObeyesdad', data=data)
plt.title('Distribution of Obesity Levels')
plt.show()

# ===== 2. Scale Continuous Columns =====
continuous_columns = data.select_dtypes(include=['float64']).columns.tolist()
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[continuous_columns])
scaled_df = pd.DataFrame(scaled_features, columns=scaler.get_feature_names_out(continuous_columns))
print(scaled_df.head(5))

# ===== 3. Combine Scaled Numerical + Categorical Columns =====
scaled_data = pd.concat([data.drop(columns=continuous_columns), scaled_df], axis=1)

# ===== 4. One-Hot Encode Categorical Features (excluding target) =====
categorical_columns = scaled_data.select_dtypes(include=['object']).columns.tolist()
if 'NObeyesdad' in categorical_columns:
    categorical_columns.remove('NObeyesdad')

encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_features = encoder.fit_transform(scaled_data[categorical_columns])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_columns))

# ===== 5. Final Prepared Data =====
prepared_data = pd.concat([scaled_data.drop(columns=categorical_columns), encoded_df], axis=1)

# Convert target to category codes
prepared_data['NObeyesdad'] = data['NObeyesdad'].astype('category').cat.codes

# ===== 6. Train-Test Split =====
X = prepared_data.drop(columns=['NObeyesdad'])
y = prepared_data['NObeyesdad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ===== 7. One-vs-All Logistic Regression =====
model_ova = LogisticRegression(multi_class='ovr', max_iter=1000)
model_ova.fit(X_train, y_train)
y_pred_ova = model_ova.predict(X_test)

# ===== 8. Accuracy =====
print("One-vs-All (OvA) Strategy")
print(f"Accuracy: {np.round(100 * accuracy_score(y_test, y_pred_ova), 2)}%")

model_ovo=OneVsOneClassifier(LogisticRegression())
model_ovo.fit(X_train,y_train)
y_pred_ovo=model_ovo.predict(X_test)

print("One-vs-All (OvA) Strategy")
print(f"Accuracy: {np.round(100 * accuracy_score(y_test, y_pred_ovo), 2)}%")
