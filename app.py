import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title='DHV Thumbnails', layout='wide')

import streamlit as st

st.markdown(
    """
    <style>
    .header-style {
        display: flex;
        justify-content: center;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="header-style">DHV AI Startup Packages Animate Thumbnails Demo</h1>', unsafe_allow_html=True)
st.header("")
st.header("")
st.header("")

# Read the package data from CSV
package_data = pd.read_csv('package.csv')

# Directory path containing the GIFs
directory = "C:\\Users\\kamth\\gif\\"

# Get the list of GIF file names in the directory
gif_files = [file for file in os.listdir(directory) if file.endswith(".gif")]

# Set the desired size for the thumbnails
thumbnail_width = 1000
thumbnail_height = 1000

# Display thumbnails in a single row
cols = st.columns(len(gif_files))
for col, gif_file in zip(cols, gif_files):
    gif_path = os.path.join(directory, gif_file)

    # Find the corresponding package information in the CSV based on the GIF file name
    package_info = package_data[package_data['name'] == gif_file]

    if not package_info.empty:
        package_name = package_info.iloc[0]['name']
        package_link = package_info.iloc[0]['link']

        # Make the thumbnail clickable and redirect to the provided link
        col.image(gif_path, width=thumbnail_width, caption="")
        col.markdown(f"[{package_name}]({package_link})", unsafe_allow_html=True)