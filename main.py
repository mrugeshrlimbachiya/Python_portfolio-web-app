import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mrugesh Limbachiya")
    content = """
    Currently pursuing a major in Computer Engineering with a focus on Cybersecurity 
    from Mumbai University. Actively engaged in the final year of study, honing 
    skills in essential software development tools and languages. Committed to 
    continuous learning and growth, with a keen interest in gaining practical experience
    in the field. Open to collaboration with industry professionals to further enhance my
    knowledge and contribute to meaningful projects.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build
"""
st.write(content2)
