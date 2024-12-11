import csv
import io
import streamlit as st

st.title('Hello world!')
st.write('hello hello')


name = st.text_input("Enter your name:")
if name:
    upload = st.file_uploader(f'ikelk faila cia {name}', type=['csv'])

if upload is not None:
    data = []
    
    file_content = io.StringIO(upload.getvalue().decode("utf-8"))
    csv_reader = csv.reader(file_content)

    for row in csv_reader:
        data.append(row)
        st.write(row)

# number = st.slider("Choose a number", 0, 100)
# st.write(f"You selected: {number}")
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.DataFrame({
#     "x": range(10),
#     "y": [i**2 for i in range(10)]
# })
#
# fig, ax = plt.subplots()
# ax.plot(data["x"], data["y"])
# st.pyplot(fig)