import streamlit as st

st.title("Unit Converter App")
st.markdown("### Convert Length,Weight And Time Instantly")
st.write("Wlecome! Select a Category, enter a value and get the converted result in real-life")

Category = st.selectbox("Choose a catgory", ["Length","Weight","Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometer to mlies":
            return value * 0.621371
        elif unit == "mlies to kilometer":
            return value / 0.621371
        
        elif category == "Weight":
            if unit == "kilogram to pounds":
                return value * 2.20462
            elif unit == " pounds to kilogram":
                return value / 2.20462
            
            elif category == "Time":
                if unit == "Hours to minutes":
                    return value * 60
                elif unit == "minutes to hours":
                    return value / 60
                if unit == "Seconds to minutes":
                    return value * 60
                elif unit == "minutes to Second":
                    return value / 60
                if unit == "Hours to days":
                    return value * 24
                elif unit == "days to hours":
                    return value / 24
            if category == "Length":
                unit = st.selectbox("select conversation ",["kliometer to mlies","mlies to kliometer"])
            elif category == "Weight":
                unit = st.selectbox("select conversation ",["kliogram to pound","pound to kliogram"])
            elif category == "Time":
                unit = st.selectbox("select conversation ",["Hours to minutes","minutes to hours""Seconds to minutes""minutes to Second""Hours to days""days to hours"])

            value = st.number_input("Enter the value the convert")

            if st.button("convert"):
                result = convert_units(Category,value,unit)
                st.success(f" the result is {result: .2f}")


                

                

                
            

    
