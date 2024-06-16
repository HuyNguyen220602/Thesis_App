from altair import Column
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container
import pandas as pd 
import mne
import google.generativeai as genai
import streamlit as st
import numpy as np
import tempfile
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from mne.preprocessing import ICA
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import io
import os
import pickle
import google.generativeai as genai
import streamlit as st


page_theme = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.hdqwalls.com/wallpapers/abstract-simple-background-4k-lp.jpg");
background-size: 85%;
background-position: right;
background-repeat: repeat;
background-size: 100% auto;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}

[data-testid="StyledLinkIconContainer"]{
margin-top: -50px;
}

[data-testid="stImage"]{
padding: 10px;
margin-top: 30px;
display: flex;
align-items: stretch;
img {border-radius: 10px;}
}

[data-testid="stBottomBlockContainer"]{
padding: 2px;   
border-radius: 1em;
}

[data-testid="stChatMessage"]{
background-color: #FFFACD;
padding: 1em;
margin-top: 10px;
border-radius: 0.5em;
word-wrap: break-word; /* Tự động xuống dòng nếu từ quá dài */
overflow: hidden; /* Ẩn phần tràn ra ngoài */
text-align: justify; /* Căn chỉnh văn bản để fit vào hộp */
font-weight: bold; /* In đậm phông chữ */
font-family: "Times New Roman", Times, serif;
font-size: 16px
}

[data-testid="stBottom"]{
background-color: #000000;
}
# [data-testid="stText"]{
background-color: #FFFACD;
padding: 0.5em;
margin-top: 10px;
border-radius: 1em;
}

[data-testid="stMarkdown"]{
padding: 10px;
margin-top: 10px;
}

</style>
"""

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
st.markdown(page_theme, unsafe_allow_html= True)

# Sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Upload", "Visualize", 'Analysis', 'Recommendation'], 
        icons=['house', 'cloud-upload', "card-image", 'file-earmark-bar-graph','chat-left-heart-fill'], menu_icon="cast", default_index=0)
    
if selected == "Home":
    st.title(" Welcome to the WebPage ")
    # Remove st.image and use CSS for background image instead
    a1, a2, a3 = st.columns(3)
    with a1:
        st.image("https://gvb-gelimed.com/wp-content/uploads/2023/01/EEG_10-10_system_with_additional_information-1.jpg")
    with a2:
        st.image("https://images.squarespace-cdn.com/content/v1/56da516107eaa05aaab21625/1620858918034-R8ZNVGWDIVQRP4G4C8RU/brainwaves-diagram.png")
    with a3:
        st.image("https://www.researchgate.net/profile/Sebastian-Nagel-4/publication/338423585/figure/fig1/AS:844668573073409@1578396089381/Sketch-of-how-to-record-an-Electroencephalogram-An-EEG-allows-measuring-the-electrical.png")

    
    #Introduction
    st.markdown(
    """
    <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
        <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
            Information
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)
    path = "E:\\App_Thesis\\static\\intro.txt"
    
    with open(path, 'r') as file:
        string_data = file.read()
        st.markdown(f"<p style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 3; word-spacing: 7px;'>{string_data}</p>", unsafe_allow_html=True)
    
    
    #Sleep stages 
    st.markdown(
    """
    <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
        <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
            Sleep Stages 
        </h1>
    </div>
    """,
    unsafe_allow_html=True) 
    
    st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="https://i.insider.com/5cfa9e0011e2053193580bf3?width=2400" style="max-width: 50%; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)
    
    # Define the data for the table
    # data = {
    #     'Sleep Stages': ['N1', 'N2', 'N3', 'REM'],
    #     'Type of Sleep': ['Light Sleep', 'Light Sleep', 'Deep Sleep', 'Dream Sleep'],
    #     'Other Names': ['Stage 1', 'Stage 2', 'Stage 3', 'Paradoxical Sleep'],
    #     'Normal Length': ['5-10 minutes', '10-60 minutes', '20-40 minutes', '10-60 minutes']
    # }

    # # Create a dataframe from the data
    # df = pd.DataFrame(data)
    # st.write(df)
    path = "E:\App_Thesis\static\sleep.txt"
    with open(path, 'r') as file_obj:
        text_file_n = file_obj.read()
        # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
        text_file_n = text_file_n.replace("\n", "<br>")
        text_file_n = text_file_n.replace("â€¢", "")
        # If you want to display the text_file_n with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
        text_file_n = "<ul>" + text_file_n.replace("\t", "<li>") + "</ul>"
        st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-family: \"Times New Roman\", Times, serif; font-size: 20px; line-height: 2; word-spacing: 7px;'>{text_file_n}</ul>", unsafe_allow_html=True)
    
    
    #disease
    
    #Brux
    st.markdown(
    """
    <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
        <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
            Disease Feature
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)
    
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>Bruxism</h2>", unsafe_allow_html=True)

    b1, b2 = st.columns(2)

    with b1:
        path = "E:\App_Thesis\static\Brux.txt"
        with open(path, 'r') as file_obj:
            text_file = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file = text_file.replace("\n", "<br>")
            text_file = text_file.replace("â€¢", "")
            # If you want to display the text_file with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file = "<ul>" + text_file.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 26px; line-height: 2.5; word-spacing: 7px;'>{text_file}</ul>", unsafe_allow_html=True)

    with b2: 
        st.image("https://res.cloudinary.com/jerrick/image/upload/c_crop,fl_progressive,h_630,q_auto,w_1200/5db7fe696c8529001dc0a40c.png", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://th.bing.com/th/id/R.61eb9eea7dc03dd2a48e492e771d75e6?rik=LsdqcUPJboP9Tg&pid=ImgRaw&r=0", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
    
    
    
    #Insomnia
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>Insomnia</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        path = "E:\App_Thesis\static\Insomnia.txt"
        with open(path, 'r') as file_obj:
            text_file_2 = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file_2 = text_file_2.replace("\n", "<br>")
            text_file_2 = text_file_2.replace("â€¢", "")
            # If you want to display the text_file_2 with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file_2 = "<ul>" + text_file_2.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 26px; line-height: 2.3; word-spacing: 7px;'>{text_file_2}</ul>", unsafe_allow_html=True)

    with c2: 
        st.image("https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/38893/woman-insomnia-clipart-md.png", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://www.sleepfoundation.org/wp-content/uploads/2018/10/SF-23-112_Insomnia_Causes_Graphic-1024x717.png", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
    
    
    
        
    #Narcolepsy    
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>Narcolepsy</h2>", unsafe_allow_html=True)
    d1, d2 = st.columns(2)

    with d1:
        path = r"E:\App_Thesis\static\Narco.txt"
        with open(path, 'r') as file_obj:
            text_file_3 = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file_3 = text_file_3.replace("\n", "<ul>")
            text_file_3 = text_file_3.replace("â€”", "")
            text_file_3 = text_file_3.replace("â€¢", "•")
            # If you want to display the text_file_3 with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file_3 = "<ul>" + text_file_3.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 26px; line-height: 2.6; word-spacing: 7.5px;'>{text_file_3}</ul>", unsafe_allow_html=True)

    with d2: 
        st.image("https://osmose-it.s3.amazonaws.com/52Of4LHGTKmCX6rgwSsqXD5_TkukzkZN/_.jpg", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://cdn.xcode.life/wp-content/uploads/2023/06/is-narcolepsy-genetic_narcolepsy-symptoms.png", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        
        
        
    #Nocturnal frontal lobe epilepsy    
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>Nocturnal frontal lobe epilepsy</h2>", unsafe_allow_html=True)
    e1, e2 = st.columns(2)   
    with e1:
        path = r"E:\App_Thesis\static\NFLE.txt"
        with open(path, 'r') as file_obj:
            text_file_4 = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file_4 = text_file_4.replace("\n", "<br>")
            # text_file_4 = text_file_4.replace("â€”", "")
            text_file_4 = text_file_4.replace("â€¢", "")
            text_file_4 = text_file_4.replace("â€™", "")
            # If you want to display the text_file_4 with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file_4 = "<ul>" + text_file_4.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 26px; line-height: 3; word-spacing: 7px;'>{text_file_4}</ul>", unsafe_allow_html=True)

    with e2: 
        st.image("https://th.bing.com/th/id/OIP.wfn0tN0-d6FcCq7YwcPfGwAAAA?rs=1&pid=ImgDetMain", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://www.casestacks.com/wp-content/uploads/2020/09/FTLD.png", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        
    
    #Periodic leg movements   
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>Periodic leg movements</h2>", unsafe_allow_html=True)
    f1, f2 = st.columns(2)   
    with f1:
        path = r"E:\App_Thesis\static\PLM.txt"
        with open(path, 'r') as file_obj:
            text_file_5 = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file_5 = text_file_5.replace("\n", "<br>")
            # text_file_5 = text_file_5.replace("â€”", "")
            text_file_5 = text_file_5.replace("â€¢", "")
            text_file_5 = text_file_5.replace("â€™", "")
            # If you want to display the text_file_5 with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file_5 = "<ul>" + text_file_5.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 2.7; word-spacing: 9px;'>{text_file_5}</ul>", unsafe_allow_html=True)

    with f2: 
        st.image("https://creativeside.me/wp-content/uploads/2020/07/e9b0aa558ea834866c6ebc0a27.jpg", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://th.bing.com/th/id/R.3d3c5a76a8e48831052328f105098928?rik=sd%2b7NTCrUUos2Q&pid=ImgRaw&r=0", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
    
    
    
    #REM behavior disorder  
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>REM behavior disorder</h2>", unsafe_allow_html=True)
    g1, g2 = st.columns(2)   
    with g1:
        path = r"E:\App_Thesis\static\REM.txt"
        with open(path, 'r') as file_obj:
            text_file_6 = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file_6 = text_file_6.replace("\n", "<br>")
            # text_file_6 = text_file_6.replace("â€”", "")
            text_file_6 = text_file_6.replace("â€¢", "")
            text_file_6 = text_file_6.replace("â€™", "")
            text_file_6 = text_file_6.replace("â€”", "")
            # If you want to display the text_file_6 with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file_6 = "<ul>" + text_file_6.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 26px; line-height: 2.6; word-spacing: 7px;'>{text_file_6}</ul>", unsafe_allow_html=True)

    with g2: 
        st.image("https://i.ytimg.com/vi/2nc8jUOQA1c/maxresdefault.jpg", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://th.bing.com/th/id/R.ea679b688bc144066b0f5eee46c31be6?rik=sbeA0xgLm%2fhKiw&riu=http%3a%2f%2f2.bp.blogspot.com%2f_6j6j9ae25v4%2fTTuf1vV3JjI%2fAAAAAAAAAfU%2fTU52wmy5VdI%2fs1600%2fREM.jpg&ehk=ECHE4eY5yzHL9fwgYq%2fu%2bZ7egVb2%2fI8eT5sjEZ1b%2biQ%3d&risl=&pid=ImgRaw&r=0", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        
        
    #Sleep-disordered breathing
    st.markdown("<h2 style='margin-top: 80px; color: #AFEEEE; '>Sleep-disordered breathing</h2>", unsafe_allow_html=True)
    h1, h2 = st.columns(2)   
    with h1:
        path = r"E:\App_Thesis\static\SDB.txt"
        with open(path, 'r') as file_obj:
            text_file_7 = file_obj.read()
            # To preserve the bullet points, you can use the .replace() method to replace newline characters with HTML line breaks
            text_file_7 = text_file_7.replace("\n", "<br>")
            # text_file_7 = text_file_7.replace("â€”", "")
            text_file_7 = text_file_7.replace("â€¢", "")
            text_file_7 = text_file_7.replace("â€™", "")
            # If you want to display the text_file_7 with bullet points, you can wrap it in an HTML <ul> tag and replace bullet points with <li> tags
            text_file_7 = "<ul>" + text_file_7.replace("\t", "<li>") + "</ul>"
            st.markdown(f"<ul style='margin-top: 15px; background-color: #FFFACD; padding: 1.5em ;border-radius: 2em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;'>{text_file_7}</ul>", unsafe_allow_html=True)

    with h2: 
        st.image("https://www.sleepadvisor.org/wp-content/uploads/2021/03/sleep-related-breathing-disorder-and-tips.jpg", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        st.image("https://th.bing.com/th/id/R.caf3f2f57166f8f01de56f553c610b4e?rik=FZtcDQojrFMwNw&riu=http%3a%2f%2fi.ytimg.com%2fvi%2f-gie2dhqP2c%2fmaxresdefault.jpg&ehk=0Z2RChspJXW%2b%2btAujgRUXYDsQ%2bUIg3WzsMeZY8ESN98%3d&risl=&pid=ImgRaw&r=0", caption=None, width=None, use_column_width=None, clamp=False, output_format="auto")
        
               
if selected == "Upload":
    
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = {}

    @st.cache_data
    def process_file(file, file_type):
        file_buffer = io.BytesIO(file.getvalue())

        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_type}') as tmp_file:
            tmp_file.write(file_buffer.getvalue())
            tmp_file_path = tmp_file.name

        try:
            if file_type == "edf":
                raw = mne.io.read_raw_edf(tmp_file_path, preload=True, verbose=0).crop(tmin=30, tmax=None)
            elif file_type == "fif":
                raw = mne.io.read_raw_fif(tmp_file_path, preload=True, verbose=0).crop(tmin=30, tmax=None)
            elif file_type == "bdf":
                raw = mne.io.read_raw_bdf(tmp_file_path, preload=True, verbose=0).crop(tmin=30, tmax=None)
            elif file_type == "gdf":
                raw = mne.io.read_raw_gdf(tmp_file_path, preload=True, verbose=0).crop(tmin=30, tmax=None)
            else:
                raise ValueError("Invalid file format")
            
        # finally:
        #     os.remove(tmp_file_path)
        except Exception as e:
            print(f"Error processing file: {e}")
            return None
        
        
        # Define the desired sampling frequency
        desired_sfreq = 128
        raw = raw.resample(desired_sfreq)
        
        # Define a dictionary mapping channel names to their types
        channel_types = {
            'Fp2-F4': "eeg", 
            'F4-C4': "eeg", 
            'C4-P4': "eeg", 
            'P4-O2': "eeg",
            'C4-A1': "eeg"
        }

        # Define the default type for EEG channels
        default_type = 'stim'

        # Set channel types for selected channels using a dictionary comprehension
        channel_types_dict = {channel_name: channel_types.get(channel_name, default_type) for channel_name in raw.ch_names}
        raw.set_channel_types(channel_types_dict)

        # Select only EEG channels
        raw = raw.pick_types(eeg=True)

        # Channel names in the current system
        current_channel_names = [
            'Fp2-F4', 'F4-C4', 'C4-P4', 'P4-O2',
            'C4-A1',
        ]

        # Corresponding channel names in the 10-20 system
        new_channel_names = [
            'F4', 'C4', 'P4', 'O2',
            'A1',
        ]

        # Rename the channels to match the 10-20 system
        channel_name_mapping = dict(zip(current_channel_names, new_channel_names))
        raw.rename_channels(channel_name_mapping)

        # Set the standard 10-20 montage
        raw.set_montage('standard_1020')
        
        filter_length = '30s'

        # Filter the data
        raw.filter(0.5, 30, fir_design='firwin', filter_length=filter_length, method='fir', fir_window='hamming')

        # Apply function to standardize the data
        raw.apply_function(lambda x: (x - x.mean()) / x.std())

        # Set EEG reference to 'average'
        raw.set_eeg_reference('average')
        
        return raw

    st.title("Please update your data here")

    # Display a header with HTML markup
    st.markdown("<h2 style='margin-top: 80px;'>Select a file</h2>", unsafe_allow_html=True)

    # Provide a non-empty label for the file uploader
    # Streamlit file uploader
    file  = st.file_uploader("Upload a file", type=['edf', 'fif', 'bdf', 'gdf'], label_visibility="hidden")

    # Add a button to clear cache
    if st.button("Clear Cache"):
        st.cache_data.clear()
        st.session_state.uploaded_files.clear()
        st.session_state.uploaded_file = None
        st.session_state.raw = None
        st.success("Cache cleared successfully!")

    if file is not None:
        # Save the uploaded file to the session state
        st.session_state.uploaded_file = file
        st.success("File uploaded successfully!")

        file_type = file.name.split('.')[-1]

        try:
            # Process and cache the file
            raw = process_file(file, file_type)
            
            # Store the file name and its content in a dictionary
            st.session_state.uploaded_files[file.name] = raw
            # Also store raw data in session state for access in other sections
            st.session_state.raw = raw

        except ValueError as e:
            st.error(str(e))
        
    # Display the cached data if it exists
    if 'uploaded_file' in st.session_state:
        file = st.session_state.uploaded_file
        if file and file.name in st.session_state.uploaded_files:
            st.write(f"Loaded file: {file.name}")
            raw = st.session_state.uploaded_files[file.name]
            st.write(raw)



if selected == "Visualize":
    styl = """
    <style>
    [data-testid="stMarkdownContainer"]{
        color: #000000; 
        font-weight: bold;    
    }
    
    
    [data-testid="stImage"]{
    padding: 10px;
    margin-top: 30px;
    display: flex;
    align-items: stretch;}
    
    img {border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    }
    
    </style>
    """

    st.markdown(styl, unsafe_allow_html=True)
    
    st.title("Data Visualize")
    
    st.markdown(
    """
    <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
        <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
           Raw data plot
        </h1>
    </div>
    """,
    unsafe_allow_html=True
    )   
    
    # Check if "Clear Cache" button is clicked
    if st.button("Clear Cache"):
        # Clear all cached functions and data
        st.cache_data.clear()

        # Clear uploaded files and processed data from session state
        st.session_state.uploaded_files.clear()
        st.session_state.uploaded_file = None
        st.session_state.processed_data = None
        st.session_state.com_fig = None
        st.session_state.source_fig = None
        
        st.success("Cache cleared successfully!") 
    
    # Function to process and plot ICA components and sources
    @st.cache_data
    def process_and_plot_ICA(_raw_data):
        try:
            ica = ICA(n_components=5, method="fastica", random_state=32, max_iter="auto")
            ica.fit(_raw_data)
            _raw_data = ica.apply(_raw_data)

            # Plot the ICA components
            com_fig = ica.plot_components(show=True)
            st.pyplot(com_fig)

            # Scale and plot the ICA sources manually
            sources_data = ica.get_sources(_raw_data).get_data()
            scaled_sources_data = sources_data * 20000e-5  # Manually scale the sources data
            n_sources = scaled_sources_data.shape[0]

            fig, axes = plt.subplots(n_sources, 1, figsize=(12, 12), sharex=True)
            if n_sources == 1:
                axes = [axes]

            times = _raw_data.times
            for i, ax in enumerate(axes):
                source = scaled_sources_data[i]
                ax.plot(times, source)
                ax.set_title(f'ICA Source {i + 1}')
                ax.set_ylabel('Amplitude')

            axes[-1].set_xlabel('Time (s)')
            fig.tight_layout()
            st.pyplot(fig)
            
            # Save processed data and figures into session state
            st.session_state.processed_data = _raw_data
            st.session_state.com_fig = com_fig
            st.session_state.source_fig = fig

        except RuntimeWarning as e:
            st.error(f"ICA fitting issue: {e}")
                    
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Check if a file has been uploaded
    if 'uploaded_file' in st.session_state:
        file = st.session_state.uploaded_file

        if file and file.name in st.session_state.uploaded_files:
            raw = st.session_state.uploaded_files[file.name]

            # Plot the raw data without displaying it immediately
            fig = raw.plot(start=5,
                                duration=10,
                                color="black",
                                scalings=dict(eeg=600000e-5), show=True, show_scrollbars=True)
            # Resize the figure
            fig.set_size_inches(12, 8)
            # Display the figure using Streamlit
            st.pyplot(fig)
            
            
            st.markdown(
                """
                <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
                    <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
                    Raw data after ICA
                    </h1>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Process and plot ICA components and sources
            process_and_plot_ICA(raw)
            
        else:
            st.error("No file uploaded. Please upload a file first.")
    else:
        st.error("No file uploaded. Please upload a file first.")    
            
    # # Markdown section for indicating raw data after ICA
    # st.markdown(
    #     """
    #     <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
    #         <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
    #         Raw data after ICA
    #         </h1>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    # # Check if processed data and figures are available in session state
    # if 'processed_data' in st.session_state and 'com_fig' in st.session_state and 'source_fig' in st.session_state:
    #     # Display ICA components and sources from session state
    #     st.pyplot(st.session_state.com_fig)
    #     st.pyplot(st.session_state.source_fig)
        
    # Markdown section for indicating spectral density
    st.markdown(
        """
        <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
            <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
            Spectral Density
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Check if a file has been uploaded for computing and plotting spectral density
    if 'uploaded_file' in st.session_state:
        file = st.session_state.uploaded_file

        if file and file.name in st.session_state.uploaded_files:
            raw = st.session_state.uploaded_files[file.name]

            try:  
                spectrum = raw.compute_psd()
                img = spectrum.plot(average=True, picks="data", exclude="bads", amplitude=True)
                st.pyplot(img)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

        else:
            st.error("No file uploaded. Please upload a file first.")
            
            
            
if selected == "Analysis":
    st.title("Here are your results")

    @st.cache_data
    def process_eeg_data():
        raw = st.session_state.uploaded_files[list(st.session_state.uploaded_files.keys())[0]]

        # Create fixed-length events and epochs
        events = mne.make_fixed_length_events(raw, duration=30. , overlap=3)
        
        tmax = 30.0 - 1.0 / raw.info['sfreq']  # tmax is included
        
        # epochs = mne.make_fixed_length_epochs(raw, duration=30.0, overlap=3, preload=True)
        # Define tmin and tmax
        
        # event_id =  {
        #     'SLEEP-REM':1,
        #     'SLEEP-N1':2,
        #     'SLEEP-N2':3,
        #     'SLEEP-N3':4}

        # Create epochs using the manually defined tmin and tmax
        epochs = mne.Epochs(raw, events = events, event_id = None, tmin=0. , tmax=tmax, baseline=(0.5, 30.0), preload=True)
        
        # Apply baseline correction
        epochs.apply_baseline(baseline=(0.5, 30.0))

        # Apply bandpass filter
        epochs.filter(0.5, 30, picks=['eeg'])
        
        spectrum = epochs.compute_psd()
        
        img = spectrum.plot(average=True, picks="data", exclude="bads", amplitude=True, spatial_colors=True)
        
        st.pyplot(img) 

        # noise_cov = mne.compute_raw_covariance(raw, tmin=0.5, tmax=None) 
        
        # noise_cov_baseline = mne.compute_covariance(epochs, tmax=None)
        
        # fig1 = noise_cov.plot(raw.info, proj=False)
        
        # st.pyplot(fig1) 
        
        # fig2 = noise_cov_baseline.plot(epochs.info, proj=False)
        
        # st.pyplot(fig2)
        
        # Compute the evoked response
        evoked = epochs.average()

        # Compute the power spectral density (PSD)
        evk_spectrum = evoked.compute_psd()

        # Define the frequency bands
        bands = {
            'Delta (0-4 Hz)': (0, 4), 
            'Theta (4-8 Hz)': (4, 8),
            'Alpha (8-12 Hz)': (8, 12), 
            'Beta (12-30 Hz)': (12, 30),
            'Gamma (30-45 Hz)': (30, 45)
        }

        # Plot the topomap and extract the figure
        topomap_fig = evk_spectrum.plot_topomap(bands=bands, normalize=True, ch_type="eeg", outlines='head')

        # Display the topomap figure in Streamlit
        st.pyplot(topomap_fig)

        # # Plot the image and extract the figure
        # image_fig = epochs.plot_image(picks="eeg", combine="median")[-1]

        # # Display the image figure in Streamlit
        # st.pyplot(image_fig)
        
        def bin_power_spectrum_1hz(psd, freqs):
            freqs_1hz_inc = list(range(1, 31))
            psds_binned_1hz = []
            curr_bin_freq = 1
            curr_bin_sum = 0
            curr_bin_size = 0

            for f in range(len(freqs)):
                if int(freqs[f]) >= curr_bin_freq:
                    psds_binned_1hz.append(curr_bin_sum / curr_bin_size if curr_bin_size > 0 else 0)
                    curr_bin_sum = 0
                    curr_bin_size = 0
                    curr_bin_freq += 1

                curr_bin_sum += psd[f]
                curr_bin_size += 1

            psds_binned_1hz.append(curr_bin_sum / curr_bin_size if curr_bin_size > 0 else 0)
            return freqs_1hz_inc, psds_binned_1hz

        def create_frequency_domain_features(epoch_data, info, normalize_band_power_within_trials=False):
            psds, freqs = mne.time_frequency.psd_array_multitaper(epoch_data, info['sfreq'], fmax=36, verbose=False)
            num_electrodes = len(psds)
            features_dict = {}

            for j in range(num_electrodes):
                freqs_binned, psd_binned = bin_power_spectrum_1hz(psds[j], freqs)
                if normalize_band_power_within_trials:
                    psd_binned /= sum(psd_binned) if sum(psd_binned)!= 0 else 1
                for k in range(len(freqs_binned)):
                    ch_name = info['ch_names'][j]
                    freq_bin_str = str(freqs_binned[k]) + 'Hz'
                    band_power = psd_binned[k]
                    feature_name = f'{ch_name}_{freq_bin_str}'
                    features_dict[feature_name] = band_power

            return features_dict

        X = epochs.get_data(picks=['eeg'], tmin=0.5)
        normalize_band_power_within_trials = True
        X_s = pd.DataFrame([create_frequency_domain_features(epoch_data, epochs.info, normalize_band_power_within_trials) for epoch_data in X])
        X_s_1 = X_s.filter(regex='C4|A1')

        return X_s_1

    # Handle file uploads and session state
    if 'uploaded_file' in st.session_state:
        
        X_s_1 = process_eeg_data()
        
        
        smote = SMOTE(sampling_strategy = 'all',random_state=42)

        sc = StandardScaler()

        X_s_2 = sc.fit_transform(X_s_1)


        if X_s_1 is not None and len(X_s_1) > 0:
            # Display the DataFrame
            st.markdown(
                """
                <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
                    <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
                    EEG data after processing 
                    </h1>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            
            st.dataframe(X_s_1.style.set_table_styles(
                    [{'selector': 'thead th', 
                    'props': [('font-weight', 'bold'), 
                                ('color', '#FFA500'), 
                                ('background-color', '#000000')]}]
                ))
            
            # Load the model and make predictions# Load the model and make predictions
            try:
                with open(r'E:\App_Thesis\model\trained_model_best.pkl', 'rb') as file:
                    loaded_model = pickle.load(file)
                    
                    st.markdown(
                    """
                    <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
                        <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
                        Sleep stages predict
                        </h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                    )

                    predictions = loaded_model.predict(X_s_2)
                    
                    # Get the unique labels and their counts
                    unique, counts = np.unique(predictions, return_counts=True)
                    

                    # Define a dictionary that maps the integer labels to the corresponding sleep stage labels
                    label_map = {
                        0: 'SLEEP-N1',
                        1: 'SLEEP-N2',
                        2: 'SLEEP-N3',
                        3: 'SLEEP-REM'
                    }

                    # Use the dictionary to map the integer labels to the corresponding sleep stage labels
                    unique_labels = [label_map[label] for label in unique]
                    
                    # Add the predictions to the end of X_s_2
                    X_s_2_with_predictions = np.c_[X_s_1, predictions]

                    # Rename the last column to "prediction"
                    column_names = list(X_s_1.columns) + ['Prediction']
                    X_s_2_with_predictions = pd.DataFrame(X_s_2_with_predictions, columns=column_names)

                    # Replace the integer labels with their corresponding sleep stage labels
                    X_s_2_with_predictions['Prediction'] = X_s_2_with_predictions['Prediction'].map(label_map)

                    st.write(X_s_2_with_predictions)
                    
                    markdown_str = """
                    <table style="width:100%; border-collapse: collapse; margin-top: 20px; font-size: 22px">
                    <tr>
                        <th style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">Sleep Stage</th>
                        <th style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">Count</th>
                    </tr>
                    """

                    for label, count in zip(unique_labels, counts):
                        markdown_str += f"""
                    <tr>
                        <td style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">{label}</td>
                        <td style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">{count} stages </td>
                    </tr>
                    """

                    markdown_str += """
                    </table>
                    """

                    st.markdown(markdown_str, unsafe_allow_html=True)
                    
                    # Create a new event_id that unifies stages 3 and 4
                    event_id = {
                        'SLEEP-REM': 1,
                        'SLEEP-N1': 2,
                        'SLEEP-N2': 3,
                        'SLEEP-N3': 4
                    }

                    # Convert the prediction column into an events array
                    events_sleep = np.zeros((len(predictions), 3), dtype=int)
                    events_sleep[:, 0] = np.arange(len(predictions))  # sample numbers
                    events_sleep[:, 2] = [event_id[label_map[label]] for label in predictions]  # event IDs

                    fig, ax = plt.subplots(figsize=(6, 3))  # Adjust the figsize as needed
                    mne.viz.plot_events(events_sleep, event_id=event_id, sfreq = 128.00, first_samp=events_sleep[0, 0], equal_spacing=True, axes=ax)
                    st.pyplot(fig)

                    # Keep the color-code for further plotting
                    stage_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
                                                
                                        
                    
                # st.markdown(
                # """
                # <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
                #     <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
                #     Sleep stages predict
                #     </h1>
                # </div>
                # """,
                # unsafe_allow_html=True
                # )

                # # Print the results
                # for label, count in zip(unique_labels, counts):
                #     st.write(f"Number {label}: {count} stages")
                    
            except FileNotFoundError:
                st.error("The trained model file is missing. Please upload the file first.")
                
            try:
                with open(r'E:\App_Thesis\model\best_RF_model.pkl', 'rb') as file:
                    loaded_model = pickle.load(file)

                # Step 2: Preprocess the CSV file data (if necessary)

                data = X_s_1

                # Upsample the data to have at least 1645 rows
                current_rows = data.shape[0]
                rows_needed = max(1645, current_rows)
                repeat_factor = -(-rows_needed // current_rows)

                # Set random seed for reproducibility
                random_seed = 42
                np.random.seed(random_seed)

                upsampled_data = data.sample(frac=repeat_factor, replace=True, random_state=random_seed)

                # Preprocess the upsampled data using a standard scaler
                scaler = StandardScaler()
                features_scaled = scaler.fit_transform(upsampled_data)

                # Apply PCA to scaled features with a fixed random seed
                n_components = 60
                pca = PCA(n_components=n_components, random_state=random_seed)
                features_pca = pca.fit_transform(features_scaled)

                # Define a dictionary that maps the integer labels to the corresponding sleep disease labels
                label_map_2 = {
                    0: 'Bruxism',
                    1: 'Insomnia',
                    2: 'No pathology',
                    3: 'Narcolepsy',
                    4: 'Nocturnal frontal lobe epilepsy',
                    5: 'Periodic leg movements',
                    6: 'REM behavior disorder',
                    7: 'Sleep-disordered breathing'
                }

                # Make predictions using the loaded model and PCA-transformed features
                predicted_pca = loaded_model.predict(features_pca)

                # Calculate the percentage of each predicted class
                class_counts_pca = Counter(predicted_pca)

                total_samples_pca = len(predicted_pca)

                st.markdown(
                    """
                    <div style='margin-top: 100px; background-color: #000000; padding: 5px; border-radius: 30px;'>
                        <h1 style='color: #FFA500; text-align: center; margin-top: 40px;'>
                        Sleep disease predict 
                        </h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                markdown_str = """
                <table style="width: 100%; border-collapse: collapse; border-radius:20px; margin-top: 20px; font-size: 22px">
                <tr>
                    <th style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">Disease</th>
                    <th style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-weight: bold; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">Percentage</th>
                </tr>
                """

                for class_label, count in sorted(class_counts_pca.items(), key=lambda x: (x[1] / total_samples_pca) * 100, reverse=True):
                    percentage_pca = (count / total_samples_pca) * 100
                    disease_label = label_map_2[class_label]
                    markdown_str += f"""
                <tr>
                    <td style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">{disease_label}</td>
                    <td style="background-color: #FFFACD; padding: 0.5em; word-wrap: break-word; text-align: justify; font-family: \"Times New Roman\", Times, serif; font-size: 16px; line-height: 1.9; word-spacing: 9px;">{percentage_pca:.2f}%</td>
                </tr>
                """

                markdown_str += """
                </table>
                """

                st.markdown(markdown_str, unsafe_allow_html=True)
                
                # Prepare data for the pie chart
                target_counts = list(class_counts_pca.values())
                target_labels = [label_map_2[key] for key in class_counts_pca.keys()]
                target_percentages = [count / total_samples_pca * 100 for count in target_counts]

                # Create labels with both percentage and count
                labels = [f'{target_labels[i]}' for i in range(len(target_counts))]

                # Create and display the pie chart
                fig, ax = plt.subplots(figsize=(4.5, 4.5))
                ax.pie(target_percentages, labels=labels, autopct='%1.1f%%', startangle= 160)
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                # plt.title('Percentage of Each Sleep Disease Class')

                st.pyplot(fig)

            except FileNotFoundError:
                st.error("The trained model file is missing. Please upload the file first.")

        else:
            st.error("No valid EEG data found in the uploaded file. Please upload a valid file.")

    else:
        st.error("No file uploaded. Please upload a file first.")
        
        
if selected == "Recommendation":
    st.title("Here are some suggestions for you !!!")
    # Add a button to clear cache
    if st.button("Clear Cache"):
        st.cache_data.clear()
        st.session_state.messages.clear()
        
        # Display chat messages
        # Display chat messages
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    if st.session_state.messages:  # Check if messages list is not empty
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Function for generating LLM response
    def generate_response(prompt_input):
        # Hugging Face Login
        genai.configure(api_key='AIzaSyBQr8yrACmw0ANADrDGeIJT13-2ZulbR1I')
        model = genai.GenerativeModel('gemini-pro')
        
        # Create ChatBot                        
        chatbot = model.generate_content(prompt_input)
        
        response_text = None
        
        # Iterate over chatbot.parts to find the part containing text
        for part in chatbot.parts:
            if hasattr(part, 'text'):
                response_text = part.text
                break

        # Check if response_text is still None
        if response_text is None:
            return "Sorry, I cannot create a response. Please ask more questions!!"
        else:
            return response_text

    # User-provided prompt
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if there are messages and the last message is not from the assistant
    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt) 
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)