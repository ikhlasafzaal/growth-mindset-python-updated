import streamlit as st

# Page configuration
st.set_page_config(page_title="Unlock Your Growth Mindset Challenge 🚀", page_icon="🔑")
st.title("🔓 Unlock Your Growth Mindset Challenge")

# Basic CSS styling
st.markdown("""
<style>
body {
    background-color: #f9f9f9;
}
h1 {
    color: #FF6347;
}
h2 {
    color: #4682B4;
}
p {
    color: #333333;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Welcome Section
st.header("✨ Unlock Your Potential!")
st.write("Welcome to your daily dose of growth and reflection. Every challenge is a stepping stone to success!")

# Motivational Quote 
st.header("💬 Today's Growth Mindset Quote")
st.write("> \"Growth isn’t about being the best, it’s about getting better every day.\"")

# Challenge Section
st.header("🔥 What's Your Growth Challenge Today?")
user_input = st.text_input("Describe a challenge you're currently facing:")

if user_input:
    st.success(f"You're tackling: **{user_input}**. Growth happens outside the comfort zone! Keep pushing forward! 🚀")
else:
    st.warning("Share a challenge to kickstart your growth journey!")

# Reflection Section
st.header("🔍 Reflect & Grow")
reflection = st.text_area("What did you learn from your challenge today?")

if reflection:
    st.success(f"Great insight! Your reflection: **{reflection}** is a step towards mastery! 🌟")
else:
    st.info("Self-reflection fuels personal growth. Take a moment to jot down your learnings!")

# Achievement Section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_area("Share something you're proud of achieving:")

if achievement:
    st.success(f"Fantastic! Acknowledge your progress: **{achievement}** 🎉 Keep striving!")
else:
    st.info("Big or small, every win counts. Recognize your success today!")

# Footer 
st.markdown("---")
st.write("🌟 Keep unlocking new possibilities and growing every day!")
st.write("© 2025 Created By Fiza Asif")
