import streamlit as st
from openai import OpenAI

# Set your API key
my_key = ""
MODEL = "gpt-4o"

# Initialize the OpenAI client
client = OpenAI(api_key=my_key)

def get_completion(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    return response.choices[0].message.content

# Prompts for different categories
prompts = {
    "theme_development": "You are an expert in Shopify theme development. Answer the user's questions related to theme development.",
    "back_end_development": "You are an expert in Shopify back-end development. Answer the user's questions related to back-end development.",
    "database": "You are an expert in database management for Shopify. Answer the user's questions related to databases.",
    "rest_api": "You are an expert in Shopify REST API. Answer the user's questions related to REST APIs."
}

# Streamlit application
def main():
    st.title("AI Shopify Development Helper ")
    st.markdown("Welcome to the AI Shopify Development Helper! Please select a category and ask your questions.")
    
    st.sidebar.title("Select a Category")
    category = st.sidebar.selectbox("Category", list(prompts.keys()))
    
    st.markdown(f"## You selected: **{category.replace('_', ' ').title()}**")
    st.markdown("Ask your questions below. Type 'exit' to quit.")
    
    user_input = st.text_input("Your question:", "")
    
    if st.button("Ask"):
        if user_input.lower() == "exit":
            st.markdown("Thank you for using the AI Shopify Development Helper ")
        else:
            messages = [
                {"role": "system", "content": prompts[category]},
                {"role": "user", "content": user_input}
            ]
            response = get_completion(messages)
            st.markdown("### Assistant's Response")
            st.success(response)

# Run the Streamlit application
if __name__ == "__main__":
    main()
