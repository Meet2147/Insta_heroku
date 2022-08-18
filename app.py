import streamlit as st
import instaloader
from PIL import Image
import glob
import os



def main():
    path = os.getcwd()
    print(path)

    st.title("Instagram DP Download")
    menu = ["DP"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "DP":
        st.subheader("Welcome to Instagram Dp downloader")
        obj = instaloader.Instaloader()
        username = st.text_input('Username')
        if username:
            st.write('Username',username)
            obj.download_profile(username, profile_pic_only=True)
            file_path = f"{path}/{username}"
            for filename in glob.iglob(file_path + '**/*.jpg', recursive=True):
                image = Image.open(filename)
                st.image(image)
                with open(filename, "rb") as file:
                    st.download_button(
                    label="Download image",
                    data=file,
                    file_name=filename,
                    mime="image/jpg"
                )
        else:
            st.write("Enter valid Username")

   





	    
if __name__ == "__main__":
    main()