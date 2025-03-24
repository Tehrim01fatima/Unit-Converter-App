import streamlit as st


st.set_page_config(page_title="Unit Converter", page_icon="🔁")

st.title("💡 Unit Converter App")
st.markdown("### Converts 📏 Length, ⚖ Weight, and ⏱ Time Instantly")

st.write("Welcome! Select a Category, enter a value, and get results in real-time.")

category = st.selectbox("Choose Category", ["length", "weight", "time"])

if category == "length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to Kilometers"])
elif category == "weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "time":
    unit = st.selectbox("⏱ Select Conversion", [
        "Seconds to minutes", "Minutes to seconds",
        "Minutes to hour s", "Hours to minutes",
        "Hours to days", "Days to hours"
    ])

value = st.number_input("Enter the value to convert")

def convert_units(category, value, unit):
    if category == "length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    return 0

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion. Please select a valid category and unit.")
