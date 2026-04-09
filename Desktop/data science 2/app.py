import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("housing.csv")

# Remove outliers
data = data[data['price'] < 3000000]
data = data[data['sqft_living'] < 10000]

# Features
features = ['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'lat', 'long']
X = data[features]
y = data['price']

# Model
model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# UI
st.title("🏠 Advanced House Price Predictor")
st.write("Enter house details below:")

col1, col2 = st.columns(2)

with col1:
    sqft_living = st.number_input("Area", 300, 20000, 1000)
    bedrooms = st.slider("Bedrooms", 1, 6, 3)
    bathrooms = st.slider("Bathrooms", 1, 5, 2)

with col2:
    floors = st.slider("Floors", 1, 3, 1)
    lat = st.number_input("Latitude", value=47.5)
    long = st.number_input("Longitude", value=-122.2)

if st.button("Predict Price"):
    input_data = pd.DataFrame([[sqft_living, bedrooms, bathrooms, floors, lat, long]],
                              columns=features)

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Price: ${int(prediction):,}")