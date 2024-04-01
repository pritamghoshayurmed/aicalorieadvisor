
# Pritam's Calories Advisor

This is a Streamlit web application that serves as a calorie advisor based on food images. It utilizes the Google Generative AI model to analyze images and provide information about the total calories and nutritional details of the food items in the image.

## Installation

1. Clone this repository to your local machine.

2. Create a virtual environment using `conda` or `virtualenv`.

3. Install the required dependencies using the following command:

   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Ensure you have a Google API key and set it in a `.env` file. Refer to `.env.example` for the required format.

5. Run the Streamlit application using the following command:

   ```
   streamlit run app.py
   ```

## Usage

1. Upload a food image using the provided file uploader.

2. Click the "Tell me about the total calories" button to analyze the uploaded image.

3. The application will display the total calories and nutritional details of the food items detected in the image.

## Contributing

Contributions are welcome! If you find any bugs or want to enhance the application, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
