PROJECT_DIR="/Users/jonathan.cachat/Documents/AbracaDATA_Confluence/chat-w-confluence_app"

cd "$PROJECT_DIR"
pip install -r requirements.txt

export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
export STREAMLIT_RUNONSSAVE=True
streamlit run app.py --server.port 8787 --browser.serverAddress localhost
