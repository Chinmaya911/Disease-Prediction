import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(os.path.join(working_dir, 'Save/diabetes_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(working_dir, 'Save/heart_disease_model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(working_dir, 'Save/parkinsons_model.sav'), 'rb'))

# Function to set background image
def set_background(image_path):
    # Read the image file and convert it to base64
    with open(image_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
    # Set the background image using CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64});
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Load the background image
bg_image_path = 'C:/Users/user/OneDrive/Desktop/Disease Prediction F/BG.gif'  # Replace with your image path
set_background(bg_image_path)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System',

                           ['Diabetes Prediction',
                        'Heart Disease Prediction',
                        'Parkinsons Prediction'],
                       menu_icon='hospital-fill',
                       icons=['activity', 'heart', 'person'],
                       default_index=0)


# Add background image
#bg_image_path = 'C:/Users/user/OneDrive/Desktop/Disease Prediction F/BG.gif'  # Replace with the path to your background image

# Function to handle user input and prediction
def predict_diabetes(inputs):
    prediction = diabetes_model.predict([inputs])
    return 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'

def predict_heart_disease(inputs):
    prediction = heart_disease_model.predict([inputs])
    return 'The person is having heart disease' if prediction[0] == 1 else 'The person does not have any heart disease'

def predict_parkinsons(inputs):
    prediction = parkinsons_model.predict([inputs])
    return "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')
    
    # Add a GIF
    gif_path = os.path.join(working_dir, 'Diabetes1.gif')
    
    # Display the GIF using cached function
    try:
        st.image(gif_path, caption='Diabetes', use_container_width=True)
    except FileNotFoundError:
        st.error(f"File not found: {gif_path}")
    
    # Input field for the user's name
    name = st.text_input("Name:")
    # columns
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0)

    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0)

    with col3:
        BMI = st.number_input('BMI value', min_value=0.0)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0)

    with col2:
        Age = st.number_input('Age of the Person', min_value=0)

    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), 
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            # Check for empty inputs
            if any(x == '' for x in user_input):
                st.error("Please fill in all fields with valid numbers.")
            else:
                diab_prediction = diabetes_model.predict([user_input])
                if (diab_prediction[0] == 1):
                    diab_diagnosis = 'The person is diabetic'
                else:
                    diab_diagnosis = 'The person is not diabetic'
        except ValueError:
            st.error("Please enter valid numeric values.")
    
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    
    # Add a GIF
    gif_path = os.path.join(working_dir, 'Heart Disease.gif')
    
    # Display the GIF using cached function
    try:
       st.image(gif_path, caption='Heart Disease', use_container_width=True)
    except FileNotFoundError:
       st.error(f"File not found: {gif_path}")
    
    # Input field for the user's name
    name = st.text_input("Name:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0)

    with col2:
        sex = st.number_input('Sex (1 = male; 0 = female)', min_value=0, max_value=1)

    with col3:
        cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', min_value=0, max_value=1)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0-2)', min_value=0, max_value=2)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0)

    with col3:
        exang = st.number_input('Exercise Induced Angina (1 = yes; 0 = no)', min_value=0, max_value=1)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)', min_value=0, max_value=2)

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-3)', min_value=0, max_value=3)

    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', min_value=0, max_value=2)
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        try:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    # Add a GIF
    gif_path = 'C:/Users/user/OneDrive/Desktop/Disease Prediction F/Parkinsons Disease.gif'
    
    # Display the GIF
    try:
        st.image(gif_path, caption='Parkinsons Disease', use_container_width=True)
    except FileNotFoundError:
        st.error(f"File not found: {gif_path}")
    
    # Input field for the user's name
    name = st.text_input("Name:")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)

    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)

    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)

    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0)

    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)

    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0)

    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0)

    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0)

    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)

    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0)

    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0)

    with col3:
        APQ = st.number_input('MDVP:APQ', min_value=0.0)

    with col4:
        DDA = st.number_input('Shimmer:DDA', min_value=0.0)

    with col5:
        NHR = st.number_input('NHR', min_value=0.0)

    with col1:
        HNR = st.number_input('HNR', min_value=0.0)

    with col2:
        RPDE = st.number_input('RPDE', min_value=0.0)

    with col3:
        DFA = st.number_input('DFA', min_value=0.0)

    with col4:
        spread1 = st.number_input('spread1', min_value=0.0)

    with col5:
        spread2 = st.number_input('spread2', min_value=0.0)

    with col1:
        D2 = st.number_input('D2', min_value=0.0)

    with col2:
        PPE = st.number_input('PPE', min_value=0.0)
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        try:
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
        except ValueError:
            st.error("Please enter valid numeric values for all fields.")
    
    st.success(parkinsons_diagnosis)