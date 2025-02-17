# ExamShield_AI
Note: ExamShield_AI is still under active development. New features are being integrated to the app.

Live At: https://examshieldai-eufydtbkarc4h5cr.centralindia-01.azurewebsites.net/


ExamShield_AI is an online coding test evaluator and proctoring system currently under active development. 

1. It leverages modern web technologies, MS Azure cloud and AI services (FREE TIER), and AI-based face recognition to secure exam integrity and ensure that only the registered candidate is taking the test. 

2. It also uses advanced activity detection , face movements to track the candidate activity using Azure AI (Face API). Then generate reports based on the activity to identify if the candidate used any unfair means in the test.

# Features
1. User Registration & Face Enrollment:
Capture candidate images using the webcam for registration and later verify identity during the test.

2. Real-Time Proctoring & Cheating Detection:
Monitor candidate behavior with live camera feeds to detect suspicious activities, such as off-screen glances, multiple faces, abnormal keystroke patterns, and head pose deviations.

3. Integrated Code Evaluation:
Provide a built-in code editor with real-time code execution and automated assessment based on expected outputs.

# Technology Stack
1. Frontend & UI:
   - Streamlit – Rapidly build interactive web applications.
2. Backend & Face Recognition:
   - Python – Primary programming language.
   - OpenCV – Used for image processing and face detection.
   - Face recognition via traditional methods (e.g., LBPH) using OpenCV (as an alternative to deep learning libraries that require TensorFlow).  

3. Cloud & Deployment:
    - Azure Web App: Host the application for scalability and robust performance.
    - Azure Cognitive Services (Face API): (Optional) For advanced face recognition features.
      
4. CI/CD:
    - GitHub Actions – Automate build, test, and deployment pipelines to Azure.
    
5. Azure Integration
    - Azure Web App:The application is deployed to Azure Web Apps, allowing easy scaling and management.

6. Azure Cognitive Services(Azure AI):
    - Azure’s Face API is being integrated to identify headpose , and other activities to identify cheating or unfair means.

7. Continuous Deployment:
    - GitHub Actions are used for continuous integration and deployment, ensuring that changes are automatically built and deployed to Azure.

# Face Recognition & Cheating Prevention
1. Face Recognition Model:
  - The system registers the candidate’s face during registration and verifies it during the test.
  - For environments where installing TensorFlow (or similar deep learning libraries) is not feasible, the system leverages OpenCV’s LBPH (Local Binary Patterns Histograms) for face recognition.
2. Cheating Detection Methods:
  - Behavioral Analysis: Detect off-screen glances, multiple faces, and unusual head poses.
  - Keystroke Monitoring: Track typing patterns and speed to identify anomalies.
  - Live Video Logging: Monitor live camera feeds to generate logs and alerts for suspicious behavior.


# Setup & Usage
1. Clone the Repository:
```
git clone https://github.com/yourusername/ExamShield_AI.git
cd ExamShield_AI
```
2. Create a Virtual Environment & Install Dependencies:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Run the Application Locally:
```
streamlit run app.py
```
4. Deployment:
The project is set up for continuous deployment to Azure using GitHub Actions. Ensure your Azure credentials and settings are configured in the repository secrets.

# Future Work
1. Enhance real-time cheating detection algorithms.
2. Integrate additional biometric and behavioral checks.
3. Expand support for multiple programming languages and code evaluation methods.
4. Develop comprehensive reporting and analytics dashboards for exam review.

# License
This project is licensed under the MIT License – see the LICENSE file for details.








