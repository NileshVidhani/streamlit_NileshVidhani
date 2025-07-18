import streamlit as st
st.cache_data.clear()
from PIL import Image

# === PAGE CONFIG ===
st.set_page_config(page_title="My Resume", layout="centered")

# === HEADER ===
st.title("Nilesh Vidhani")
st.subheader("Final Year BCA Student ")
st.subheader("Analyst | Data Analyst | Business Analyst | Financial Analyst ")
st.markdown("---")

# === CONTACT SECTION ===
st.markdown(" **Email:** vidhanin810@gmail.com.com")
st.markdown(" **GitHub:** [github.com/nileshvidhani](https://github.com/nileshvidhani)")
st.markdown(" **Location:** Bengaluru, India")
st.markdown(" **LinkedIn:** [nileshvidhani](https://www.linkedin.com/in/nilesh-vidhani/)")
st.markdown("---")

# === EDUCATION ===
st.header(" Education")
st.markdown("""
**Bachelor of Computer Applications (BCA)**  
Christ University, Bangalore  
2022 – 2026  
CGPA: 7.4  
""")

st.markdown("---")

# === SKILLS ===
st.header(" Hard Skills")
st.markdown("""
- Python, Streamlit, Flask
- SQL, Pandas, NumPy
- Git & GitHub
- Web Scraping
- Excel
- MySql
- Mongodb
""")

st.markdown("---")

st.header(" Soft Skills")
st.markdown("""
- Time Management
- Team Building
- Leadership
- Attention to Detail
- Creativity
""")

st.markdown("---")

# === PROJECTS ===
st.header(" Projects")
st.markdown("""
**Auto-Learner AI App**  
A Google Classroom–like application that allows students to upload assignments and get instant AI-based evaluation.  

**Housing.com Web Scraper**  
A Python-based scraper to extract real-estate data with user-defined city input and save structured output.  
""")

st.markdown("---")

# === ADDITIONAL SECTION (Optional) ===
st.header("Certifications")
st.markdown("""
- Python for Data Science – Infosys Springboard  
-   
""")

st.markdown("---")
st.success("Thank you for viewing my resume!")

