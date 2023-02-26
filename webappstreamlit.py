import streamlit as st
import pandas as pd
import numpy as np

# title - It is used to create a title
st.title("This is a Title")

# Header - It is used to create a header
st.header("This is a Header")

#Sub Header - It is used to create a sub header
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
st.markdown("# This is a header")
st.markdown("## This is a header")
st.markdown("### This is a header")
st.markdown("#### This is a header")
st.markdown("##### This is a header")
st.markdown("###### This is a header")
st.markdown(":moon:")

# Text - It is used to display the message as text like in different style maybe
st.text("This is a text")


