
import streamlit as st
from PIL import Image

st.title('Malaria Prediction App')

# with st.expander("About this App"):
#   st.write("This app is used to predict malareia in patients before conducting test.")
#   image = Image.open("C:\\Users\\sraks\\AIML Internship\\AIML-Internship\\MODEL\\img.png")
#   st.image(image, caption="Price prediction")

report = 'False'
if report == 'False':
    general_details = st.sidebar.toggle('Enter General Details')
    common_symptoms = st.sidebar.toggle('Enter Common Symptoms')
    severe_symptoms = st.sidebar.toggle('Enter Severe Symptoms')
    previous_record = st.sidebar.toggle('Enter Previous Health History')

    if general_details:
        st.subheader('General Details')
        name = st.text_input("Name : ")
        age = st.number_input("Age : ")
        place = st.text_area("Place : ")
        temperature = st.number_input("Temperature (f) : ")

    if common_symptoms:
        st.subheader("Early Symptoms : ")
        fever = st.slider("FEVER (days) ", 0, 30)
        headache = st.slider("HEADACHE (days) ", 0, 30)
        bodyache = st.slider("BODYACHE (days) ", 0, 30)
        vomiting = st.slider("VOMITING (days) ", 0, 30)
        chills = st.slider("CHILLS (days) ", 0, 30)
        cough = st.slider("COUGH (days) ", 0, 30)
        weakness = st.slider("GENERALIZED WEEKNESS", 0, 30)

    if severe_symptoms:
        options = st.multiselect('Select the symptoms',
                                 ['ABDOMINAL DISCOMFORT', 'BREATHELESSNESS', 'LOOSE STOOL', 'RIGORS',
                                  'DECREASED APPETITE', 'NAUSEA', 'THROAT PAIN', 'URINAL VARIATION', 'ASHTHMA',
                                  'pallor', 'icterus', 'clubbing', 'cynosis', 'lymphadenopathy', 'pedel oedema',
                                  'DROWSY', 'DISCOMFORT', 'Appetite( Abnormal )', 'Sleep( Abnormal )', 'Skin Rashes'],
                                 ['ABDOMINAL DISCOMFORT', 'BREATHELESSNESS']
                                 )
        st.write('You selected:', options)

    if previous_record:
        diabetes = st.selectbox('Diabetes', ['Yes', 'No'])
        malaria = st.selectbox('Previous History of Malaria', ['Yes', 'No'])
        dengue = st.selectbox('Previous History of Dengue', ['Yes', 'No'])
        bronchial = st.selectbox('Bronchial', ['Yes', 'No'])

    if general_details == 0:
        st.write("Enter general details")
    elif common_symptoms == 0:
        st.write("Enter Common symptoms")
    elif severe_symptoms == 0:
        st.write("Enter Severe symptoms")
    elif previous_record == 0:
        st.write("Enter Previous health record")
    else:
        st.write("Submit your details")
        if st.sidebar.button('SUBMIT'):
          report='True'

if report == 'True':
    st.write("comming soon")









