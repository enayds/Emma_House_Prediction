import streamlit as st
import joblib

# Load the models
lagos_model = joblib.load('final_model_lag.joblib')
abuja_model = joblib.load('final_model_abj.joblib')

# Configure Streamlit Page
st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")

# Navigation Menu
menu = ["Project Overview", "Student Information", "Prediction App"]
choice = st.sidebar.selectbox("Navigate", menu)

# Page 1: Project Overview
if choice == "Project Overview":
    st.title("🏠 House Price Prediction App")
    st.markdown("""
    ### Welcome to the House Price Prediction App! 🎉
    This project was built to help predict the **price of houses** in **Abuja** and **Lagos**, based on key features like the number of bedrooms, bathrooms, and location.

    #### How to Use the App:
    1. Navigate to the **Prediction App** page.
    2. Fill in the required details about the house.
    3. Select the city (Abuja or Lagos).
    4. Click **Predict** to get the estimated house price!

    #### About the Project:
    - Utilizes **Machine Learning** models tailored for Abuja and Lagos.
    - Features **Gradient Boosting Regressor** for high accuracy.
    - Built with a user-friendly **Streamlit** interface.

    Enjoy exploring house prices in Nigeria! 💡
    """)

# Page 2: Student Information
elif choice == "Student Information":
    st.title("📚 Student Information")
    st.markdown("""
    #### Developer Information:
    - **Student Name**: Azumara Emmanuel
    - **Matriculation Number**: Enter Matric Number
    - **Supervisor Name**: [Enter Supervisor Name]
    - **Department**: Computer Science
    - **School**: Imo State University
    """)
    
    st.subheader("Passport Photograph")
    st.image("WhatsApp Image 2024-11-28 at 23.14.18.jpeg", width=150, caption="Student Passport")

# Page 3: Prediction App
# Page 3: Prediction App
elif choice == "Prediction App":
    st.title("🏡 House Price Prediction")
    st.markdown("#### Enter the house details below to get a price estimate.")

    # Towns for Abuja and Lagos
    abuja_towns = [
        'Lokogoma District', 'Katampe', 'Kaura', 'Galadimawa', 'Gwarinpa',
        'Lugbe District', 'Jahi', 'Others_abuja', 'Guzape District',
        'Utako', 'Life Camp', 'Gaduwa', 'Asokoro District', 'Wuye',
        'Kubwa', 'Apo', 'Wuse 2', 'Durumi', 'Mabushi', 'Karsana', 'Wuse',
        'Karmo', 'Maitama District', 'Gudu', 'Mbora (Nbora)', 'Jabi',
        'Garki', 'Kado'
    ]
    
    lagos_towns = [
        'Lekki', 'Ajah', 'Victoria Island (VI)', 'Ikeja', 'Magodo', 'Yaba',
        'Agege', 'Ikorodu', 'Isheri North', 'Others_lagos', 'Ikoyi',
        'Ipaja', 'Ibeju Lekki', 'Ojodu', 'Ogudu', 'Isolo', 'Surulere',
        'Alimosho', 'Ikotun', 'Maryland', 'Gbagada', 'Ifako-Ijaiye', 'Ojo',
        'Ilupeju', 'Amuwo Odofin'
    ]

    # City Selection
    city = st.selectbox("City", ["Lagos", "Abuja"])
    
    # Dynamically populate towns based on the selected city
    if city == "Lagos":
        town = st.selectbox("Town", lagos_towns)
        model = lagos_model
    else:
        town = st.selectbox("Town", abuja_towns)
        model = abuja_model

    # Input Features
    bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
    bathrooms = st.number_input("Number of Bathrooms", min_value=1, step=1)
    toilets = st.number_input("Number of Toilets", min_value=1, step=1)
    parking_space = st.number_input("Parking Space", min_value=1, step=1)
    title = st.selectbox("Type of House", ["Detached Duplex", "Terraced Duplexes", "Semi Detached Duplex", "Block of Flats",
                                           "Detached Bungalow", "Semi Detached Bungalow", "Terraced Bungalow"])

    # Prediction
    if st.button("Predict"):
        # Prepare input
        input_features = [[bedrooms, bathrooms, toilets, parking_space, title, town]]

        try:
            # Predict the price
            predicted_price = model.predict(input_features)[0]
            st.success(f"The estimated price for this house in {city} is: ₦{predicted_price:,.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
