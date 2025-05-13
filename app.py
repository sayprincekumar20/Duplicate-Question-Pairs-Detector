
# import streamlit as st
# import helper
# import pickle

# model = pickle.load(open('model.pkl','rb'))

# st.title('Duplicate Question Pairs Detector')
# # 💡 Add your repo link here
# st.markdown("[🔗 View Repository](https://github.com/sayprincekumar20/Duplicate-Question-Pairs-Detector)")
# st.markdown("""
# This is a **Duplicate Question Detector** web application built with **Streamlit**.  
# It takes two questions as input and uses a trained machine learning model to determine if the questions are semantically similar (i.e., duplicates of each other).

# Such systems are commonly used in platforms like **Quora** or **Stack Overflow** to detect and merge similar questions to avoid redundancy and improve search results.
# """)

# st.markdown("Enter two questions to check if they are semantically similar (i.e., duplicates).")

# # Add example questions
# examples = [
#     ("How do I learn Python?", "What is the best way to learn Python?"),
#     ("What is AI?", "Explain artificial intelligence."),
#     ("How to make a website?", "Steps to create a website."),
#     ("Where is Mount Everest?", "What is the location of Mount Everest?"),
#     ("How do I reset my password?", "I forgot my password. How to reset?")
# ]

# selected_example = st.selectbox(
#     "Or choose an example pair:",
#     options=[""] + [f"Q1: {q1} | Q2: {q2}" for q1, q2 in examples],
#     index=0
# )

# # Initialize inputs
# q1 = ""
# q2 = ""

# # Pre-fill inputs if an example is selected
# if selected_example != "":
#     index = [f"Q1: {q1} | Q2: {q2}" for q1, q2 in examples].index(selected_example)
#     q1, q2 = examples[index]

# q1 = st.text_input('Enter Question 1', value=q1)
# q2 = st.text_input('Enter Question 2', value=q2)

# if st.button('Find'):
#     if q1.strip() == "" or q2.strip() == "":
#         st.warning("Please enter both questions.")
#     else:
#         query = helper.query_point_creator(q1, q2)
#         result = model.predict(query)[0]

#         if result:
#             st.error('❌ The questions are **Duplicate**.')
#         else:
#             st.success('✅ The questions are **Not Duplicate**.')

import streamlit as st
import helper
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# ---- Main Title ----
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🤖 Duplicate Question Pairs Detector</h1>", unsafe_allow_html=True)

# ---- Repository Link ----
st.markdown(
    "<p style='text-align: center;'>"
    "<a href='https://github.com/sayprincekumar20/Duplicate-Question-Pairs-Detector' target='_blank'>🔗 View Project Repository on GitHub</a>"
    "</p>",
    unsafe_allow_html=True
)

# ---- Description ----
with st.expander("📘 What does this app do?"):
    st.markdown("""
    This is a **Duplicate Question Detector** web application built with **Streamlit**.  
    It allows users to input two questions and uses a trained machine learning model to check whether the questions are semantically similar (i.e., duplicates).

    Such systems are commonly used in platforms like **Quora** or **Stack Overflow** to identify and merge similar questions, avoiding redundancy and improving user experience.
    """)

st.markdown("### ✍️ Enter your questions or choose an example pair:")

# ---- Example Questions ----
examples = [
    ("How do I learn Python?", "What is the best way to learn Python?"),
    ("What is AI?", "Explain artificial intelligence."),
    ("How to make a website?", "Steps to create a website."),
    ("Where is Mount Everest?", "What is the location of Mount Everest?"),
    ("How do I reset my password?", "I forgot my password. How to reset?")
]

selected_example = st.selectbox(
    "📌 Example Pairs:",
    options=[""] + [f"Q1: {q1} | Q2: {q2}" for q1, q2 in examples],
    index=0
)

# ---- Input Section ----
q1 = ""
q2 = ""

# Pre-fill if example selected
if selected_example:
    index = [f"Q1: {q1} | Q2: {q2}" for q1, q2 in examples].index(selected_example)
    q1, q2 = examples[index]

col1, col2 = st.columns(2)
with col1:
    q1 = st.text_area("🔍 Question 1", value=q1, height=100)
with col2:
    q2 = st.text_area("🔎 Question 2", value=q2, height=100)

# ---- Prediction Button ----
if st.button("🚀 Check Similarity"):
    if not q1.strip() or not q2.strip():
        st.warning("⚠️ Please enter both questions.")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        st.markdown("---")
        if result:
            st.success('✅ These questions are **Duplicate**.')
        else:
            st.error('❌ These questions are **Not Duplicate**.')

# ---- Footer ----
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with ❤️ by Prince Kumar</p>", unsafe_allow_html=True)
