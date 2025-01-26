import streamlit as st

def main():
    st.set_page_config(page_title="Your App")
    st.title("Your Streamlit App")
    
    # Your code here
    user_input = st.text_input("Enter something:")
    if user_input:
        st.write(f"You entered: {user_input}")

if __name__ == "__main__":
    main()
