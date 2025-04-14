import streamlit as st
import pickle
import pandas as pd
import base64
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model
model_file = 'spam_model2.pkl'  # Replace with your model path
with open(model_file, 'rb') as modelfile:
    model = pickle.load(modelfile)

# Load the TF-IDF Vectorizer
vectorizer_file = 'your_vectorizer_file.pkl'  # Replace with your vectorizer path
with open(vectorizer_file, 'rb') as vectorfile:
    vectorizer = pickle.load(vectorfile)

# Function to load and encode the background image
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        return encoded_string
    except FileNotFoundError:
        st.error("Background image file not found.")
        return ""
    
# Set your background image path here
background_image_path = "C:/Users/sanga/Downloads/hacker3.jpg"  # Replace with the path to your background image
# background_image_path="C:/Users/sanga/OneDrive/Desktop/customer_recommendation_sm/background_pics/movie.jpg"
encoded_image = get_base64_image(background_image_path)

# Define CSS for the background if the image was successfully loaded
if encoded_image:
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
         background-size: 100% 100%;       /* Adjust image to cover 80% of width and height */
        background-repeat: no-repeat;
        background-attachment: fixed;
        color:blue;  /* Adjust text color if necessary */
    }}
    </style>
    """

# Inject the CSS with Streamlit's markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up the Streamlit app
st.title("SMS SPAM DETECTOR")

# Input text box for user message
user_input = st.text_area("Enter your message to check spam or not:")

# Button to make a prediction
if st.button("Predict"):
    if user_input:
        # Transform the input text using the same vectorizer
        input_tfidf = vectorizer.transform([user_input])
        
        # Make a prediction
        prediction = model.predict(input_tfidf)
        
        # Show the prediction
        if prediction[0] == 1:
            st.error("This message is classified as SPAM.")
        else:
            st.success("This message is classified as HAM.")
    else:
        st.warning("Please enter a message to classify.")
