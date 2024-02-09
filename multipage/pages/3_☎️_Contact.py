import streamlit as st 

# st.set_page_config(page_title="Contact Me⏎",page_icon="👥")
# st.sidebar.success("Select a page")

def main():
    st.set_page_config(page_title="Contact Me", page_icon="☎️")

    st.title("Contact Me")

    # st.image("assets/techguy.jpeg", width=500) 
    st.header("About Me")
    st.write("""
        Hello! I'm Atharv Awle, a passionate individual dedicated to making a difference through technology.
        Feel free to reach out to me using the contact form below.
    """)

    # Contact Form
    st.header("Contact Form")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message", height=150)

    # Submit button
    if st.button("Submit"):
        # Process the form data (you can add your logic here)
        # For now, just display the submitted information
        st.success(f"Thank you, {name}! Your message has been submitted.")

if __name__ == "__main__":
    main()