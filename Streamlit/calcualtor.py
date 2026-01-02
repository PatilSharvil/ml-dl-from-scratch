import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.title("🧮 Calculator")

# Session state for display
if "expr" not in st.session_state:
    st.session_state.expr = ""

# Display
st.text_input("Display", st.session_state.expr, disabled=True)

# Button handler
def press(val):
    if val == "C":
        st.session_state.expr = ""
    elif val == "=":
        try:
            st.session_state.expr = str(eval(st.session_state.expr))
        except:
            st.session_state.expr = "Error"
    else:
        st.session_state.expr += val

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            press(btn)
