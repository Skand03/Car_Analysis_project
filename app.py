import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# Title and description
st.title("🚗 Car Price Prediction")
st.markdown("### Get an estimated price for your used car")
st.markdown("---")

# Load the trained model
final_model = pickle.load(open('final_model.pkl', 'rb'))

# Mapping dictionaries
insurance_map = {
    'Comprehensive': 0,
    'Third Party Insurance': 1,
    'Zero Dep': 2,
    'Not Available': 3
}

fuel_map = {
    'Petrol': 0,
    'Diesel': 1,
    'CNG': 2
}

transmission_map = {
    'Manual': 0,
    'Automatic': 1
}

ownership_map = {
    'First Owner': 0,
    'Second Owner': 1,
    'Third Owner': 2,
    'Fourth Owner': 3,
    'Fifth Owner': 4
}

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    insurance_validity = st.selectbox(
        "Insurance Type",
        options=list(insurance_map.keys()),
        help="Select the type of insurance coverage"
    )
    
    fuel_type = st.selectbox(
        "Fuel Type",
        options=list(fuel_map.keys()),
        help="Select the fuel type of the car"
    )
    
    transmission = st.selectbox(
        "Transmission",
        options=list(transmission_map.keys()),
        help="Select the transmission type"
    )

with col2:
    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        max_value=500000,
        value=50000,
        step=1000,
        help="Enter the total kilometers driven"
    )
    
    ownership = st.selectbox(
        "Ownership",
        options=list(ownership_map.keys()),
        help="Select the ownership status"
    )

st.markdown("---")

# Predict button
if st.button("🔍 Predict Price", type="primary", use_container_width=True):
    # Convert inputs to model format
    insurance_val = insurance_map[insurance_validity]
    fuel_val = fuel_map[fuel_type]
    transmission_val = transmission_map[transmission]
    ownership_val = ownership_map[ownership]
    
    # Prepare test data
    test = [[insurance_val, fuel_val, int(kms_driven), ownership_val, transmission_val]]
    
    # Make prediction
    predicted_price = int(final_model.predict(test)[0])
    
    # Display result
    st.success("### Prediction Complete!")
    st.metric(
        label="Estimated Car Price",
        value=f"₹ {predicted_price} Lakhs"
    )
    
    # Additional info
    st.info(f"""
    **Your Car Details:**
    - Insurance: {insurance_validity}
    - Fuel Type: {fuel_type}
    - Kilometers Driven: {kms_driven:,} km
    - Ownership: {ownership}
    - Transmission: {transmission}
    """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Powered by Machine Learning (KNN Regression Model)</p>",
    unsafe_allow_html=True
)