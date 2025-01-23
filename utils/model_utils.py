from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

MODEL_PATH = "./models/earnings_model.pkl"

def train_model(df):
    """Train and save a Random Forest model for earnings prediction."""
    # Features and target
    X = df[["base_pay", "tips", "peak_pay", "adjustments"]]
    y = df["total_earnings"]
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, MODEL_PATH)
    return model

def predict_earnings(base_pay, tips, peak_pay, adjustments):
    """Predict earnings given feature inputs."""
    model = joblib.load(MODEL_PATH)
    return model.predict([[base_pay, tips, peak_pay, adjustments]])[0]
