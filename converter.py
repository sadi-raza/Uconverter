# shortcut for emojis = winKey  + ;
import streamlit as st  

st.title("Unit Converter")
st.markdown("### convert units of different catagories easily by this App")
category = st.selectbox("Select the category", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to be converted", min_value=0.0, step=0.1)


def converter_units(category, value, unit ):
        if category == "Length":
            if unit == "foot_to_meter":
                return value / 3.281
            elif unit == "meter_to_kilometer":
                return value /1000
            elif unit == "foot_to_kilometer":
                    return value / 3281
                
        if category == "Temperature":
            if unit == "Celsius_to_Fahrenheit":
                return (value * 9/5) + 32
            if unit == "Fahrenheit_to_Celsius":
                return (value - 32) * 5/9
        
        if category == "Weight":
            if unit == "gram_to_kilogram":
                return value / 1000
            elif unit == "kilogram_to_gram":
                return value * 1000
            return 0
                
if category == "Length":
   unit = st.selectbox("Select the unit to convert from", ["foot_to_meter", "meter_to_kilometer", "foot_to_kilometer"])
elif category == "Weight":
    unit = st.selectbox("Select the unit to convert from", ["gram_to_kilogram", "kilogram_to_gram"])
elif category == "Temperature":
    unit = st.selectbox("Select the unit to convert from", ["Celsius_to_Fahrenheit", "Fahrenheit_to_Celsius"])
else:
    st.error("Invalid category selected")


if st.button("Convert"):
    result = converter_units(category, value, unit )
    st.success(f"The converted value is: {result: .3f}")



