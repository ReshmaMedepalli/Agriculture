import streamlit as st
import pandas as pd

# Crop Data
crop_data = pd.DataFrame({
    'Crop': ['Wheat', 'Rice', 'Corn', 'Cotton', 'Tomato'],
    'Best Soil Type': ['Loamy', 'Clayey', 'Sandy', 'Loamy', 'Loamy'],
    'Climate': ['Temperate', 'Tropical', 'Temperate', 'Arid', 'Temperate'],
    'Water Requirements': ['Moderate', 'High', 'Moderate', 'Low', 'Moderate']
})

# Fertilizer Data
fertilizer_data = pd.DataFrame({
    'Crop': ['Wheat', 'Rice', 'Corn', 'Cotton', 'Tomato'],
    'Fertilizer': ['NPK 10-20-10', 'Urea', 'NPK 20-10-10', 'DAP', 'Compost']
})

# Disease Data
disease_data = pd.DataFrame({
    'Crop': ['Wheat', 'Rice', 'Corn', 'Cotton', 'Tomato'],
    'Common Diseases': ['Rust', 'Blast', 'Blight', 'Cotton Bollworm', 'Early Blight'],
    'Treatment': ['Fungicide', 'Fungicide', 'Fungicide & Pesticide', 'Pesticide', 'Fungicide']
})

# Streamlit App
st.title("Agriculture Assistant: Crop, Fertilizer, and Disease Management")

# Sidebar inputs
st.sidebar.header("User Inputs")

# Soil and Climate for Crop Recommendation
soil_type = st.sidebar.selectbox("Select Soil Type", ['Loamy', 'Clayey', 'Sandy'])
climate_type = st.sidebar.selectbox("Select Climate", ['Temperate', 'Tropical', 'Arid'])

# Function to recommend crops based on soil and climate
def recommend_crops(soil_type, climate_type):
    recommended = crop_data[(crop_data['Best Soil Type'] == soil_type) & (crop_data['Climate'] == climate_type)]
    return recommended

# Button to get crop recommendation
if st.sidebar.button("Get Crop Recommendations"):
    recommended_crops = recommend_crops(soil_type, climate_type)
    if not recommended_crops.empty:
        st.subheader("Recommended Crops")
        for _, row in recommended_crops.iterrows():
            st.write(f"- {row['Crop']}")
    else:
        st.warning("No crops found for the selected conditions.")

# Crop selection for fertilizer and disease info
selected_crop = st.sidebar.selectbox("Select Crop for Fertilizer and Disease Information", crop_data['Crop'])

# Display fertilizer information
def get_fertilizer_info(crop):
    fertilizer = fertilizer_data[fertilizer_data['Crop'] == crop]['Fertilizer'].values[0]
    return fertilizer

if st.sidebar.button("Get Fertilizer Information"):
    fertilizer = get_fertilizer_info(selected_crop)
    st.subheader(f"Fertilizer for {selected_crop}")
    st.write(f"Recommended Fertilizer: {fertilizer}")

# Display disease information
def get_disease_info(crop):
    disease_info = disease_data[disease_data['Crop'] == crop]
    return disease_info

if st.sidebar.button("Get Disease Information"):
    disease_info = get_disease_info(selected_crop)
    if not disease_info.empty:
        st.subheader(f"Disease Information for {selected_crop}")
        for _, row in disease_info.iterrows():
            st.write(f"- Common Diseases: {row['Common Diseases']}")
            st.write(f"- Treatment: {row['Treatment']}")
    else:
        st.warning(f"No disease information available for {selected_crop}.")

# Footer
st.markdown("""
    <footer style="text-align: center;">
        <p style="font-size: 14px;">This tool provides basic recommendations for crop management. For advanced guidance, consult an agricultural expert.</p>
    </footer>
""", unsafe_allow_html=True)

