import time
import streamlit as st  
from streamlit_option_menu import option_menu



# Assuming 'palm' is the correct module name
import google.generativeai as palm 
palm.configure(api_key=st.secrets["PALM_API_KEY"])
st.set_page_config(page_title="StreamChatify", page_icon="🤖")
# Define the model (replace 'your_model_name' with the actual model name)
model = "models/text-bison-001"

def generate_prompt(prompt):
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )
   
    return completion.result

def main():
    st.title("StreamChatify : Chat App 🗯️")

    # Get user input
    user_prompt = st.text_input("Enter your text prompt:")

    

    if st.button("Generate Chat"):
        with st.spinner(text='In progress'):
            chat = generate_prompt(user_prompt)
            time.sleep(3)  # Simulating processing time (remove in a real application)
            st.success('Done')

            # Display the generated chat
            st.markdown(f"**Generated Chat:**\n{chat}", unsafe_allow_html=True)
    
    if st.button("Clear Input",type="primary"):
        user_prompt = ""


  
   

if __name__ == "__main__":
    main()