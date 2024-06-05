import streamlit as st
import pandas as pd
import pickle


pipe = pickle.load(open("RidgeModel.pkl", "rb"))

# Streamlit UI
st.set_page_config(
    page_title="House Price Prediction App",
    page_icon="icon.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS to adjust the styling
st.markdown(
    """
    <style>
    
    .stApp {
        background-color: #2d2739; /* Set your desired background color */
        padding: 20px;
        border-radius: 10px;
    }
    .stMarkdownTitle {
        font-size: 40px;
        text-align: center;

    }
    
    .stHeader {
        text-align: left;
        font-size: 28px;
    }
    .css-1avcm0n {
        background: #040406;  /* Change the navbar color to your desired color */
    }
    .st-br {
    color: #040406;
    border: none;
    background-color: #695b85
    }
    
    
    .st-bw {
    background-color: #695b85;
    border: none;
    color: #040406
    }
    
    .st-di  {
    background-color: #695b85;
    border: none;
    color: #040406
    }
    .css-1hgxyac  {
    background-color: #695b85;
    border: none;
    color: #040406

    }
    
    .css-1hgxyac.focused  {
    background-color: #695b85;
    border: none;
    color: #040406

    }
    
    .css-1hdbmx1.focused {
       border: none;
    }

    .custom-button {
        background-color: #695b85;
        color: white;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s; /* Add a smooth transition for background color change */
    }

    .custom-button:active {
        background-color: green; /* Change the background color when the button is clicked (active) */
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI with centered title and left-aligned header
st.markdown("<h1 class='stMarkdownTitle'>HOUSE PRICE PREDICTION APP</h1>", unsafe_allow_html=True)
st.header('Input House Information')

# Set the page layout to centered and limit width
st.markdown(
    """
    <style>
    .stApp {
        max-width: 10000px; /* Adjust the content width as needed */
        margin: 0 auto;
        padding: 0rem 1rem 10rem; /* Add padding to the bottom for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Streamlit UI elements for inputs
city = st.selectbox('City', ['Bangalore'])
total_sqft = st.number_input('Total Area in square feets', min_value=0)
location = st.selectbox('Location', ['1st Block Jayanagar', '1st Phase JP Nagar', '2nd Phase Judicial Layout', '2nd Stage Nagarbhavi', '5th Block Hbr Layout', '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar', '8th Phase JP Nagar', '9th Phase JP Nagar', 'AECS Layout', 'Abbigere', 'Akshaya Nagar', 'Ambalipura', 'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal', 'Anjanapura', 'Ardendale', 'Arekere', 'Attibele', 'BEML Layout', 'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar', 'Balagere', 'Banashankari', 'Banashankari Stage II', 'Banashankari Stage III', 'Banashankari Stage V', 'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout', 'Bannerghatta', 'Bannerghatta Road', 'Basavangudi', 'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road', 'Bellandur', 'Benson Town', 'Bharathi Nagar', 'Bhoganhalli', 'Billekahalli', 'Binny Pete', 'Bisuvanahalli', 'Bommanahalli', 'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli', 'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chamrajpet', 'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar', 'Chikkalasandra', 'Choodasandra', 'Cooke Town', 'Cox Town', 'Cunningham Road', 'Dasanapura', 'Dasarahalli', 'Devanahalli', 'Devarachikkanahalli', 'Dodda Nekkundi', 'Doddaballapur', 'Doddakallasandra', 'Doddathoguru', 'Domlur', 'Dommasandra', 'EPIP Zone', 'Electronic City', 'Electronic City Phase II', 'Electronics City Phase 1', 'Frazer Town', 'GM Palaya', 'Garudachar Palya', 'Giri Nagar', 'Gollarapalya Hosahalli', 'Gottigere', 'Green Glen Layout', 'Gubbalala', 'Gunjur', 'HAL 2nd Stage', 'HBR Layout', 'HRBR Layout', 'HSR Layout', 'Haralur Road', 'Harlur', 'Hebbal', 'Hebbal Kempapura', 'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara', 'Horamavu Banaswadi', 'Hormavu', 'Hosa Road', 'Hosakerehalli', 'Hoskote', 'Hosur Road', 'Hulimavu', 'ISRO Layout', 'ITPL', 'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur', 'Jalahalli', 'Jalahalli East', 'Jigani', 'Judicial Layout', 'KR Puram', 'Kadubeesanahalli', 'Kadugodi', 'Kaggadasapura', 'Kaggalipura', 'Kaikondrahalli', 'Kalena Agrahara', 'Kalyan nagar', 'Kambipura', 'Kammanahalli', 'Kammasandra', 'Kanakapura', 'Kanakpura Road', 'Kannamangala', 'Karuna Nagar', 'Kasavanhalli', 'Kasturi Nagar', 'Kathriguppe', 'Kaval Byrasandra', 'Kenchenahalli', 'Kengeri', 'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli', 'Kodigehaali', 'Kodigehalli', 'Kodihalli', 'Kogilu', 'Konanakunte', 'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate', 'Kumaraswami Layout', 'Kundalahalli', 'LB Shastri Nagar', 'Laggere', 'Lakshminarayana Pura', 'Lingadheeranahalli', 'Magadi Road', 'Mahadevpura', 'Mahalakshmi Layout', 'Mallasandra', 'Malleshpalya', 'Malleshwaram', 'Marathahalli', 'Margondanahalli', 'Marsur', 'Mico Layout', 'Munnekollal', 'Murugeshpalya', 'Mysore Road', 'NGR Layout', 'NRI Layout', 'Nagarbhavi', 'Nagasandra', 'Nagavara', 'Nagavarapalya', 'Narayanapura', 'Neeladri Nagar', 'Nehru Nagar', 'OMBR Layout', 'Old Airport Road', 'Old Madras Road', 'Padmanabhanagar', 'Pai Layout', 'Panathur', 'Parappana Agrahara', 'Pattandur Agrahara', 'Poorna Pragna Layout', 'Prithvi Layout', 'R.T. Nagar', 'Rachenahalli', 'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Rajiv Nagar', 'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra', 'Sahakara Nagar', 'Sanjay nagar', 'Sarakki Nagar', 'Sarjapur', 'Sarjapur Road', 'Sarjapura - Attibele Road', 'Sector 2 HSR Layout', 'Sector 7 HSR Layout', 'Seegehalli', 'Shampura', 'Shivaji Nagar', 'Singasandra', 'Somasundara Palya', 'Sompura', 'Sonnenahalli', 'Subramanyapura', 'Sultan Palaya', 'TC Palaya', 'Talaghattapura', 'Thanisandra', 'Thigalarapalya', 'Thubarahalli', 'Thyagaraja Nagar', 'Tindlu', 'Tumkur Road', 'Ulsoor', 'Uttarahalli', 'Varthur', 'Varthur Road', 'Vasanthapura', 'Vidyaranyapura', 'Vijayanagar', 'Vishveshwarya Layout', 'Vishwapriya Layout', 'Vittasandra', 'Whitefield', 'Yelachenahalli', 'Yelahanka', 'Yelahanka New Town', 'Yelenahalli', 'Yeshwanthpur', 'others'])
bath = st.number_input('Number of Bathrooms', min_value=0)
bhk = st.number_input('BHK Value', min_value=0)



if st.button('Predict Price'):
    # Prepare the data for the model
    user_input = pd.DataFrame({
        'location': [location],  # Use a list with a single value
        'total_sqft': [total_sqft],  # Use a list with a single value
        'bath': [bath],  # Use a list with a single value
        'bhk': [bhk],  # Use a list with a single value
    })

    # Calling prediction pipeline to predict the output
    x = pipe.predict(user_input)
    
    # 12 lakhs
    
    # Return the prediction
    st.subheader('Price Predicted:')
    # Print the value of x
    st.write(f'₹ {abs(round(x[0]/100,2))} Crores')
       
    
# streamlit run house_prediction_app.py
