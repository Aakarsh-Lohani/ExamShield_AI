import streamlit as st
import streamlit.components.v1 as components
from templates import *
from streamlit_ace import st_ace
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Register face using FACEAPI 
def register_face(image_bytes):
    return True


def main():
    st.title("ExamShield AI")
    menu = ["Register", "Test", "Evaluator","Practice"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.header("Candidate registration")
        captured_image = st.camera_input("Take a picture , Face should be clearly visible")
        if captured_image is not None:
            st.image(captured_image, use_column_width=True)
            if st.button("Register face"):
                image_bytes= captured_image.read()
                if register_face(image_bytes):
                    st.success("Face registered successfully!")
                else:
                    st.error("Face registration failed, Retry!")

    elif choice == "Test":
        st.header("Coding Test")
        st.write('''
        Instructions:\n
        1. You will have 60 minutes to complete the test\n
        2. You will be monitored using AI, camera access is required\n
        3. You are not allowed to open any other tabs or windows\n
        4. Give the test in full screen mode\n
        5. Don't try to cheat, else you will be disqualified\n
        ''')

        if st.button("Start Test"):
            #Request full-screen mode.
            components.html(fullScr1,height=150)
            st.write("Full screen mode activated!")

            st.success("Test Started! Please use the 'Show Logs' button if you want to view monitoring details.")
            show_logs= st.button("Show Logs")

            if show_logs:
                st.subheader("Logs")
                log_cols = st.columns(2)
                with log_cols[0]:
                    st.write("**Video Stream:**")
                    # Insert a video stream component (using streamlit-webrtc)
                    webrtc_streamer(key="video_logs", video_transformer_factory=VideoTransformer)
                with log_cols[1]:
                    st.write("**Activity Logs:**")
                    st.text("Suspicious activity logs will be displayed here...")
                st.markdown("---")  # divider

if __name__=="__main__":
    main()