# 📊 WhatsApp Chat Analyzer

A **WhatsApp Chat Analyzer** built using **Python** and **Streamlit**. This tool helps you explore and visualize chat data from WhatsApp — whether it's a group or personal conversation.

---

### 🧠 Features

- 📈 **Chat Statistics**: total messages, words, media, links
- 👥 **Most Active Users**: in group chats
- ☁️ **Word Cloud**: most commonly used words
- 💬 **Common Words**: with frequency counts
- 😂 **Emoji Analysis**: top emojis used
- 📅 **Timelines**: monthly, daily, weekly message trends
- 🔥 **Activity Heatmap**: see when people are most active

---

### 🧾 How to Use

1. Export a WhatsApp chat (without media) from your phone
2. Upload the `.txt` file into the app
3. Select a user or "Overall"
4. View all the statistics and visualizations!

---

### 🛠️ Tech Stack

- Python 🐍
- Streamlit 🚀
- Pandas 📊
- Matplotlib & Seaborn 📈

---

### 🚀 Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Akky7684/chat-analyzer.git
   cd chat-analyzer
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

### 📂 Files in This Project

- `app.py` – Main Streamlit app
- `helper.py` – Helper functions for analysis
- `preprocessor.py` – Prepares and cleans raw chat data
- `requirements.txt` – List of dependencies
- `stop_hinglish_comma_separated.txt` – Custom stopwords (if any)

---

### 🙋‍♂️ Made by

**Achintya Singh (Akky7684)**  
Project for learning data visualization with Python & Streamlit
