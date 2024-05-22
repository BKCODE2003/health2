import google.generativeai as genai
import streamlit as st
import streamlit.components.v1 as components

genai.configure(api_key = st.secrets["api_key"])
model = genai.GenerativeModel("gemini-pro")

def get_email(age,gender,height,weight,fitness,exercise,diet):
   # prompt="Write an email from {} to {}.Subject Line is {}.Keep the email {}.The email is regarding {}.".format(src,dest,subject,tone,about)
    prompt="Generate a Personalized Fitness Plan: if this is the age {},this is the gender {},this is height in cm {},this is weight in kg {}, this is current fitness level {},this is exercise preference {}, this is the dietary restrictions {},so please give a tailored fitness plan to achieve our objectives and recommend a type of diet.".format(age,gender,height,weight,fitness,exercise,diet)
    response=model.generate_content(prompt)
    return response.text


# print(get_email("student","princpal","leave for 3 days","formal","I cannot attend college for the next 3 days"))
components.html("""
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
    </style>
    <span class="material-symbols-outlined">fitness_center</span>
""", height=0)



#website using steamlit

st.set_page_config(
    page_title="Fitness Plan Generator",
    page_icon=":fitness_center:",
    layout="centered",
    initial_sidebar_state="collapsed" #for side bar initially collapsed
)

#this will create empty web page
st.header("Get Your Personalised Fitness Plan")
st.write("Desribe your current fitness parameters and we will provide action plan for you.")

col1,col2=st.columns(2)
with col1:
    age=st.text_input("Enter your age") 
    height =st.text_input("Height")
    fitness=st.selectbox("Select your current fitness level",["Poor","Good","Excellent"])
    
with col2: 
   gender=st.selectbox("Select your gender",["Male","Female"])
   weight=st.text_input("Weight")
   exercise=st.selectbox("Select your intensity of exersice",["Light","Moderate","Vigorous"])
 #This will create dropdown 
 
diet=st.text_area("Enter your Dietary restrictions and preferances") 
# resizable text box(using text_area)
send_request =st.button("Give me my plan") 
# This will create button

if send_request:
    if age and gender and height and weight and diet and fitness and exercise:
        #this to make compulsory to add this field      
     st.write(get_email(age,gender,height,weight,fitness,exercise,diet))
    else:
        st.error("Please fill all the fields.")
        
        
        
        
        
