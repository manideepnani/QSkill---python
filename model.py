import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ---------------- LOAD DATA ----------------
df = pd.read_csv("../house-prices-advanced-regression-techniques/train.csv")

# ---------------- SELECT FEATURES ----------------
features = ["GrLivArea", "BedroomAbvGr", "FullBath", "GarageArea"]

df = df[features + ["SalePrice"]]

# ---------------- REMOVE MISSING VALUES ----------------
df = df.dropna()

# ---------------- SPLIT DATA ----------------
X = df[features]
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- TRAIN MODEL ----------------
model = LinearRegression()
model.fit(X_train, y_train)

# ---------------- PREDICT ----------------
y_pred = model.predict(X_test)

# ---------------- EVALUATION ----------------
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print("RMSE:", rmse)
print("R2 Score:", r2)

# ---------------- SAMPLE PREDICTION ----------------
print("\n🏠 SAMPLE PREDICTION")

sample = pd.DataFrame(
    [[2000, 3, 2, 500]],
    columns=["GrLivArea", "BedroomAbvGr", "FullBath", "GarageArea"]
)

prediction = model.predict(sample)

print("Predicted House Price:", prediction[0])