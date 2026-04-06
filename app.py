import streamlit as st
from ocr_pipline import extract_text_pipeline
from llm_analysis import analyze_with_llm
from vin import extract_vin
from vin_api import fetch_vehicle_details
from chatbot import contract_chatbot

# CONFIG
st.set_page_config(
    page_title="Contract Intelligence Console",
    layout="wide"
)

#CSS 
st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #1b1f2a, #0b0e14);
}
.glass {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(14px);
    border-radius: 16px;
    padding: 18px;
    border: 1px solid rgba(255,255,255,0.08);
}
.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    background: #ff4b4b;
    color: white;
}
h1,h2,h3 {
    color: #f8fafc;
}
</style>
""", unsafe_allow_html=True)

# header
st.markdown("""
<h1> Contract Intelligence Console</h1>
<p style="opacity:0.7">
AI-powered system for car lease risk analysis & negotiation support
</p>
""", unsafe_allow_html=True)

# state
if "text" not in st.session_state:
    st.session_state.text = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None
if "vin" not in st.session_state:
    st.session_state.vin = None

# upload
with st.container():
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload Contract (PDF / Image)",
        type=["pdf","jpg","jpeg","png"]
    )
    run = st.button("▶ Run Intelligence Pipeline")
    st.markdown("</div>", unsafe_allow_html=True)

if uploaded_file and run:
    with open(uploaded_file.name,"wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Running OCR..."):
        st.session_state.text = extract_text_pipeline(uploaded_file.name)

    with st.spinner("Running AI Analysis..."):
        st.session_state.analysis = analyze_with_llm(st.session_state.text)
        st.session_state.vin = extract_vin(st.session_state.text)

# main dashboard
if st.session_state.text:

    left, center, right = st.columns([1.2, 2, 1.3])

    # left flow
    with left:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.subheader(" Document Flow")
        st.markdown("• Uploaded ")
        st.markdown("• OCR Completed ")
        st.markdown("• VIN Extracted ")
        st.markdown("</div>", unsafe_allow_html=True)

    # center ai
    with center:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.subheader(" Contract Intelligence")

        with st.expander("AI Summary & Risk Analysis", expanded=True):
            st.write(st.session_state.analysis)

        if st.session_state.vin:
            with st.expander(" VIN Inspector"):
                vin_data = fetch_vehicle_details(st.session_state.vin)
                st.json(vin_data)
    
        st.markdown("</div>", unsafe_allow_html=True)

    # right chat bot
    with right:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.subheader(" AI Negotiation Assistant")

        q = st.text_input("Ask about clauses, risks, negotiation")
        if q:
            with st.spinner("Thinking..."):
                ans = contract_chatbot(st.session_state.text, q)
            st.markdown(f"**You:** {q}")
            st.markdown(f"**AI:** {ans}")

        st.markdown("</div>", unsafe_allow_html=True)
