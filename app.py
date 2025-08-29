import streamlit as st
import random

# --- List of Urdu Quotes ---
urdu_quotes = [
    "خودی کو کر بلند اتنا کہ ہر تقدیر سے پہلے خدا بندے سے خود پوچھے بتا تیری رضا کیا ہے۔",
    "ناکامی کامیابی کی پہلی سیڑھی ہے۔",
    "صبر کا پھل میٹھا ہوتا ہے۔",
    "علم ایک ایسا خزانہ ہے جو کبھی ختم نہیں ہوتا۔",
    "محبت ہر چیز فتح کر لیتی ہے۔",
    "وقت ایک دریا ہے، جس میں ہم سب بہہ رہے ہیں۔",
    "اُمید پر دنیا قائم ہے۔",
    "ہر مشکل کے بعد آسانی ہے۔",
    "جو بوؤ گے وہی کاٹو گے۔",
    "زندگی ایک سفر ہے، منزل نہیں۔",
    "عمل سے زندگی بنتی ہے جنت بھی جہنم بھی۔",
    "ہمت کرے انسان تو کیا ہو نہیں سکتا۔",
    "اتفاق میں برکت ہے۔",
    "تجربہ بہترین استاد ہے۔"
]

# --- Streamlit App ---

st.set_page_config(layout="wide")

# Title of the app
st.title("اردو کہاوت جنریٹر")
st.subheader("Random Urdu Quote Generator")


# Custom CSS to embed Urdu font and style the output
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

body {
    direction: rtl;
}

.urdu-quote-container {
    direction: rtl;
    font-family: 'Noto Nastaliq Urdu', serif;
    background-color: #f0f2f6;
    border-radius: 15px;
    padding: 30px;
    margin: 20px 0;
    text-align: center;
    border: 2px solid #e0e0e0;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.urdu-quote-container:hover {
    transform: scale(1.02);
}

.urdu-quote-text {
    font-size: 2.8em;
    color: #2c3e50;
    font-weight: bold;
    line-height: 1.8;
}

/* Style for the button */
.stButton>button {
    font-size: 1.2em;
    font-weight: bold;
    padding: 10px 25px;
    border-radius: 10px;
    border: 2px solid #2980b9;
    background-color: #3498db;
    color: white;
}
.stButton>button:hover {
    background-color: #2980b9;
    color: white;
    border-color: #2980b9;
}
</style>
""", unsafe_allow_html=True)


# --- App Logic ---

# Initialize session state to store the quote
if 'quote' not in st.session_state:
    st.session_state.quote = "ایک خوبصورت اردو کہاوت کے لیے بٹن دبائیں۔" # "Press the button for a beautiful Urdu quote."

# Generate Quote Button
if st.button("نئی کہاوت حاصل کریں"): # "Get a new quote"
    # Select a random quote that is different from the current one
    new_quote = st.session_state.quote
    while new_quote == st.session_state.quote:
        new_quote = random.choice(urdu_quotes)
    st.session_state.quote = new_quote

# Display the quote in a styled container
st.markdown(f'<div class="urdu-quote-container"><p class="urdu-quote-text">{st.session_state.quote}</p></div>', unsafe_allow_html=True)

