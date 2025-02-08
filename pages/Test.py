import streamlit as st
import streamlit.components.v1 as components
from templates import *
from streamlit_ace import st_ace
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        return frame

st.title("Coding Test - ExamShield AI")

# st.markdown(fullScr1, unsafe_allow_html=True)

if st.button("Confirm Full Screen"):
    components.html(fullScr, height=150)


if st.button("Show Logs"):
    st.subheader("Monitoring Logs")
    log_cols = st.columns(2)
    with log_cols[0]:
        st.write("**Video Stream:**")
        webrtc_streamer(key="video_logs", video_transformer_factory=VideoTransformer)
    with log_cols[1]:
        st.write("**Activity Logs:**")
        st.text("Suspicious activity logs will be displayed here...")
    st.markdown("---")  # divider

# Main test interface split into two columns: problem and code editor.
main_cols = st.columns(2)
with main_cols[0]:
    st.subheader("Problem Statement")
    st.write("""
    **Challenge:**  
    Write a Python function that takes a list of numbers and returns the sum of all even numbers.  
    *Example:* For input `[1,2,3,4]`, the output should be `6`.
    """)
with main_cols[1]:
    st.subheader("Code Editor")
    code = st_ace(language='python', theme='github', keybinding='vscode', font_size=14)
    st.write("Your code:")
    st.code(code, language='python')

# Submit test button to end the test session.
if st.button("Submit Test"):
    st.success("Your submission was successful!")
    # Optionally, exit full screen via JavaScript.
    components.html("""
    <script>
      if (document.exitFullscreen) {
          document.exitFullscreen();
      } else if (document.webkitExitFullscreen) { 
          document.webkitExitFullscreen();
      }
    </script>
    """, height=50)
    # Here, you could also trigger backend logic to record data and generate a report.
