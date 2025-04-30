import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return feedback

# Streamlit App
def app():
    st.title("Password Strength Meter")
    st.write("Enter a password to check its strength based on security criteria.")

    # User input for password
    password = st.text_input("Enter your password:")

    if password:
        feedback = check_password_strength(password)
        for line in feedback:
            st.write(line)

    # Suggest strong password feature
    if st.button("Generate a Strong Password"):
        st.write("Here is a suggested strong password: ")
        st.code("Str0ng!P@ssw0rd2023")

# Run the app
if __name__ == "__main__":
    app()
