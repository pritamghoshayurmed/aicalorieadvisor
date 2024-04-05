import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()  # loading all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded. Please upload an image.")

st.set_page_config(page_title="Pritam's calories Advisor")
uploaded_file = st.file_uploader("Upload your Food Image", type=["jpg", "png", "jpeg"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the total calories")
input_prompt = """
act as an expert nutritionist, where you need to see the food items from the image and calculate the total calories,
also provide the details of every food item with calories intake
in below format
1. Item 1: Calories in Item 1
2. Item 2: Calories in Item 2
-------------------------
-------------------------
finally you can also mention whether the food is healthy or not and also mention the percentage split of the ratio of carbohydrates, fats, fibers, sugar
and what things should be in our diet
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.header("The result is")
    st.write(response)
    
