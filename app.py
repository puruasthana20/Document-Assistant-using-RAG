import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"
UPLOAD_URL = "http://127.0.0.1:8000/upload"

st.set_page_config(page_title="RAG Assistant", layout="wide")

st.title("🧠 RAG Chat Assistant")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = False
    st.session_state.file_name = ""

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📄 Upload a document (PDF)", type=["pdf"])

if uploaded_file and not st.session_state.file_uploaded:
    with st.spinner("Processing document..."):
        try:
            response = requests.post(
                UPLOAD_URL,
                files={"file": (uploaded_file.name, uploaded_file.getvalue())}
            )

            if response.status_code == 200:
                st.session_state.file_uploaded = True
                st.session_state.file_name = uploaded_file.name
                st.session_state.messages = []
                st.success(f"✅ Uploaded: {uploaded_file.name}")
            else:
                st.error("❌ Upload failed")

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Settings")

    mode = st.selectbox("Response Mode", ["normal", "mcq"])

    if st.session_state.file_uploaded:
        st.markdown(f"📄 **Current File:** {st.session_state.file_name}")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []

    if st.button("🔄 Upload New Document"):
        st.session_state.file_uploaded = False
        st.session_state.messages = []

# ---------------- CHAT HISTORY ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- INPUT CONTROL ----------------
if not st.session_state.file_uploaded:
    st.info("📂 Please upload a document to start chatting.")
    user_input = None
else:
    user_input = st.chat_input("Ask something...")

# ---------------- CHAT LOGIC ----------------
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        try:
            response = requests.post(API_URL, json={
                "question": user_input,
                "mode": mode
            })

            result = response.json()

            answer = result.get("answer", "No answer")
            sources = result.get("sources", [])

        except Exception as e:
            answer = f"Error: {e}"
            sources = []

    with st.chat_message("assistant"):
        st.write(answer[:1000] + "..." if len(answer) > 1000 else answer)

        if sources:
            with st.expander("📄 Sources"):
                for i, src in enumerate(sources):
                    st.markdown(f"**Source {i+1}:**")
                    st.write(src[:400] + "...")

    st.session_state.messages.append({"role": "assistant", "content": answer})