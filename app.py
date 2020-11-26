import streamlit as st

# Text/Title
st.title("Streamlit Tutorials by Nishchit Chakilela")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello streamlit this is nishchit chakilela.")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is a error that 'Streamlit' is not defined")

st.exception("NameError('Name one not defined')")

# Get Help Info About Python
st.help(range)


# Writing Text
st.write("Text with write")

st.write(range(10))

# Images
from PIL import Image
img = Image.open(r"C:\Users\nishc\OneDrive\Pictures\Camera Roll\spider man photo.jpg")
st.image(img,width=700,caption="Simple Spider Man Image")


# Videos
vid_file = open(r"C:\Users\nishc\OneDrive\Pictures\Camera Roll\Aardhya sweet voice.mp4","rb").read()
#vid_bytes = vid_file.read()
st.video(vid_file)

# Audio
audio_file = open(r"C:\Users\nishc\OneDrive\Documents\Sound recordings\Nishchit recording on streamlit.m4a","rb").read()
st.audio(audio_file,format='audio/m4a')


# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widgth")


# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
    st.success("You are Active")
else:
    st.warning("Your are Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)


# MulitiSelect
location = st.multiselect("Where do you work?",("London","New York","India","United States Of America","Accra","Kiev","Nepal","Turkey"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,90)


# Buttons
st.button("Streamlit Button")

if st.button("About"):
    st.text("Streamlit is cool")


# Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")
if st.button("Submit",key="k1"):
    result = firstname.title()
    st.success(result)


# text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit",key="K2"):
    result = message.title()
    st.success(result)

# Data Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())

# Time
the_time = st.time_input("The time is",datetime.time())

# Displaying JSON
st.text("Display JSON")
st.json({'name':"Nishchit",'gender':"male",'Grade':"5",'section':"k"})

# Display Raw Code
st.text("Display Raw Code")
st.code("import pandas as pd")

# Display Raw Code
with st.echo():
    # This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(100):
    my_bar.progress(p + 1)


# Spinner
with st.spinner("Waiting for you .."):
    time.sleep(2)
st.success("Finished!")


# Ballons
st.balloons()
time.sleep(2)


# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is streamlit and streamlit is cool.")


# Functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())





# Dataframes
st.dataframe(df)

# Tables

st.table(df)




