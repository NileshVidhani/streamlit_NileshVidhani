import streamlit as st
st.cache_data.clear()
from PIL import Image

# === PAGE CONFIG ===
st.set_page_config(page_title="My Resume", layout="centered")

# === HEADER ===
st.image(image, width=150)
st.title("Nilesh Vidhani")
st.subheader("Final Year BCA Student | Python Developer | Data Enthusiast")
st.markdown("---")

# === CONTACT SECTION ===
st.markdown(" **Email:** nilesh@example.com")
st.markdown(" **GitHub:** [github.com/nileshvidhani](https://github.com/nileshvidhani)")
st.markdown(" **Location:** Mumbai, India")
st.markdown("---")

# === EDUCATION ===
st.header(" Education")
st.markdown("""
**Bachelor of Computer Applications (BCA)**  
Christ University, Bangalore  
2022 – 2025  
CGPA: 8.6  
""")

# === SKILLS ===
st.header(" Skills")
st.markdown("""
- Python, Streamlit, Flask
- SQL, Pandas, NumPy
- Git & GitHub
- Web Scraping
""")

# === PROJECTS ===
st.header(" Projects")
st.markdown("""
**Auto-Learner AI App**  
A Google Classroom–like application that allows students to upload assignments and get instant AI-based evaluation.  

**Housing.com Web Scraper**  
A Python-based scraper to extract real-estate data with user-defined city input and save structured output.  
""")

# === ADDITIONAL SECTION (Optional) ===
st.header(" Achievements & Certifications")
st.markdown("""
- Python for Everybody – Coursera  
- Web Development Internship at XYZ Pvt Ltd  
""")

st.markdown("---")
st.success("Thank you for viewing my resume!")

