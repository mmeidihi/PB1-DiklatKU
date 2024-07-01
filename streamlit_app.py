import streamlit as st
from PIL import Image
from multipage import MultiPage

# Import your page modules (make sure these files are in your 'pages' directory)
from pages import about 
from pages import predict_mushroom


# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.title("Mushroom Edibility Prediction App")
# image = Image.open('california.jpg')
# st.image(image, caption='California Housing', use_column_width=True)

# Add all your pages 
app.add_page("Home", predict_mushroom.app) # Assuming 'predict_house_price.py' is your home page
app.add_page("About the Data", about.app)

# Run the app
if __name__ == "__main__":
    app.run()