# 🇱🇧 Lebanon Economic Intelligence Platform

An interactive analytical web application built with Streamlit and Python to track, visualize, and query macroeconomic indicators during Lebanon's economic crisis (2009–2025)[cite: 1].

## 📂 Project Structure

This project is modularized into clean, independent components:
* **`app.py`**: The main Streamlit web interface containing tabs for data visualizations and the interactive query assistant.
* **`utils.py`**: The backend logic module responsible for loading the dataset, generating custom Matplotlib charts, and executing programmatic queries.
* **`data.json`**: The core dataset containing annual inflation rates (CPI YoY %) and exchange rates (LBP per USD)[cite: 1].

---

## 🚀 How to Run the Project

This application requires **no external API keys** and runs completely self-contained on any machine.

### Step 1: Install Dependencies
Open your terminal in the project directory and install the required Python packages using this command:
```bash
pip install streamlit pandas matplotlib
### Step 2: run the code
python -m streamlit run app.py