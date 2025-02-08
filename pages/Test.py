import streamlit as st
import streamlit.components.v1 as components
from templates import *
from streamlit_ace import st_ace
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        return frame

st.set_page_config(layout="wide", page_title="ExamShield AI - Coding Test")
st.title("Coding Test- ExamShield AI")
if "test_started" not in st.session_state:
    st.session_state.test_started = False


if st.button("Confirm Full Screen"):
    if not st.session_state.test_started:
        components.html(fullScr, height=150)
        # Simulate that camera is activated and face recognized.
        st.session_state.test_started = True

    
    if st.session_state.test_started:
        st.markdown("---")        
        col_left, col_right = st.columns(2)
        with col_left:
            st.subheader("Problem Statement")
            st.write("""
            **Challenge:**  
            Write a Python function that takes a list of numbers and returns the sum of all even numbers.  
            *Example:* For input `[1,2,3,4]`, the output should be `6`.
            """)
        with col_right:
            st.subheader("Code Editor")
            code = st_ace(language='python', theme='github', keybinding='vscode', font_size=14)
            st.write("**Your code:**")
            st.code(code, language='python')

        st.markdown("---")
        # Button to show a third panel with video stream and activity logs.
        if st.button("Show Logs"):
            st.subheader("Monitoring Logs")
            log_cols = st.columns(2)
            with log_cols[0]:
                st.write("**Video Stream:**")
                webrtc_streamer(key="video_logs", video_transformer_factory=VideoTransformer)
            with log_cols[1]:
                st.write("**Activity Logs:**")
                st.text("Suspicious activity logs will appear here...")

        if st.button("Submit Test"):
            st.success("Your submission was successful!")
            components.html(
                """
                <script>
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.webkitExitFullscreen) {
                    document.webkitExitFullscreen();
                }
                </script>
                """,
                height=50
            )
            st.markdown=("Thank you for completing the test. You may now close this tab.")
