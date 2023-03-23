import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

# Title - It is used to create a title
st.title("This is a Title")

# Header - It is used to create a header
st.header("This is a Header")

# Sub Header - It is used to create a sub header
st.subheader("This is a Sub Header")

# info - It is used to display the information 
st.info("This is a information that is used to give information")

# Warning - It is used to display the warning
st.warning("This is a warning message")

# Write - It is used to write message
st.write("This is a message that is used to write a message")
st.write(range(50))

# Error - It is used to to display error message
st.error("This is an error message")

# Success - It is used to display success message
st.success("This is a success message")

# Markdown - It is used to display the messages in different places sizes based on the # symbol
# There are only 6 different sizes available
st.markdown("# This is a header")
st.markdown("## This is a header")
st.markdown("### This is a header")
st.markdown("#### This is a header")
st.markdown("##### This is a header")
st.markdown("###### This is a header")

# It is used to display the emoji
# Search for the emoji in the website https://www.webfx.com/tools/emoji-cheat-sheet/
st.markdown(":moon:")
st.markdown(":sun_with_face:")
st.markdown(":sunrise:")
st.markdown(":sunrise_over_mountains:")
st.markdown(":cloud:")
st.markdown(":heart:")

# Adding Styles and Colours
# Enclosing a word between TWO ** gives you BOLD effect and enclosing between TWO UNDERSCORES gives you ITALIC effect
st.markdown('Streamlit is **_really_ cool**.')

# If you want to colour any word then enclose it with square brackets and then wrap it with the colour name and a colon like :red[word]
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

# Text - It is used to display the message as text like in different style maybe
st.text("This is a text")

# Caption - It is used to display the Caption
st.caption("This is a caption")

# Latex - It is used to display the formattings
st.latex(r''' a+b^2+c''')
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)''')

# Code - It is used to display the code in a codeblock and Display a code block with optional syntax highlighting
# Syntax - st.code(body, language="python")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')



# Image - It is used to display the image
image = Image.open('C:\\Users\\DELL\\Desktop\\CODE\\SWCBLACK.png')

# caption = It is used to display the caption of the image under the image
st.image(image, caption='Sunrise by the mountains')
# ------------------------------SIDEBAR------------------------

# SIDEBAR TITLE
st.sidebar.title("SIDEBAR")

# SIDEBAR SUBHEADER
st.sidebar.subheader("This is a subheader")

# SIDEBAR WRITE (SAME AS WRITE FUNCTION IN GENERAL)
st.sidebar.write("This is a message that is used to write a message")

# SIDEBAR INFO
st.sidebar.info("This is a information that is used to give information")

# SIDEBAR WARNING
st.sidebar.warning("This is a warning message")

# -----------WIDGETS------------------------------------------------

# Buttton - It is used to create a button Widget that can be used to redirect to other pages when you click
st.button('Click me')
# st.experimental_data_editor('Edit data', data)

# Checkbox - It is used to create a checkbox Widget
st.checkbox('I agree')

# Radio - It is used to create a radio Widget and the options can be given within the square brackets and with quotation marks
st.radio('Pick one', ['cats', 'dogs'])

# SelectBox - It is used to create a selectBox Widget and the options are available to choose from the list of options
st.selectbox('Pick one', ['cats', 'dogs'])

# MultiselectBox - It is used to create a multi select Widget that helps in clicking or selecting multiple options
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

# Slider - It is used to select a value using the option of slide and the value can only be a numeric value not a string
st.slider('Pick a number', 0, 100)

# Select_Slider - It is used to select a value using the option of sliding and it allows you to select only the particular value which is given in the square brackets
st.select_slider('Pick a size', ['S', 'M', 'L'])

# Text Input - It is used to create a text input Widget by which we can get input from the user, you cannot use this to type paragraph
st.text_input('First name')

# Number Input - It is used to create a number input Widget by which we can input a number from the user within a certain range
st.number_input('Pick a number', 0, 10)

# Text Area - It is used to create a text area Widget by which we can type a paragraph like it allows the user to type a paragraph
st.text_area('Text to translate')

# Date Input - It is used to create a date input Widget by which we can input a date from the user
st.date_input('Your birthday')

# Time Input - It is used to create a time input Widget by which we can input a time from the user
st.time_input('Meeting time')

# File Uploader - It is used to upload a file
st.file_uploader('Upload a CSV')
# st.download_button('Download file', data)

# Camera Input - It is used to take a live picture from the camera
st.camera_input("Take a picture")

# Color Picker - It is used to pick a color
st.color_picker('Pick a color')


with st.spinner(text='In progress'):
    time.sleep(5)
    st.success('Done')

# st.progress(progress_variable_1_to_100)
st.balloons()
st.snow()
# st.exception(e)

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

if st.user.email == 'vishnutechnophile@gmail.com':
    display_jane_content()
elif st.user.email == 'vishnutechnophile@gmail.com':
    display_adam_content()
else:
    st.write("Please contact us to get access!")






