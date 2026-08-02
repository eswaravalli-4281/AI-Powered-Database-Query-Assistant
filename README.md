# 🤖 AI-Powered Database Query Assistant

An AI-powered application that converts natural language questions into SQL queries using **Google Gemini**, executes them on a **SQLite** database, and displays the results through an interactive **Streamlit** interface.

---

## 🚀 Features

- Convert natural language into SQL queries using Google Gemini.
- Execute AI-generated SQL queries on a SQLite database.
- Display the generated SQL query before execution.
- Interactive Streamlit web interface.
- Supports SQL operations like `SELECT`, `COUNT`, `AVG`, `WHERE`, and more.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- Prompt Engineering
- python-dotenv

---

## 📂 Project Structure

```text
AI-Powered-Database-Query-Assistant/
│── app.py
│── sql.py
│── requirements.txt
│── README.md
└── images/
    ├── average_marks.png
    └── student_names.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Powered-Database-Query-Assistant.git
```

Navigate to the project:

```bash
cd AI-Powered-Database-Query-Assistant
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

### Average Marks Query

![Average Marks](images/average_marks.png)

### Student Names Query

![Student Names](images/student_names.png)

---

## 💬 Sample Queries

- Show all student names.
- Count the total number of students.
- Show the average marks of all students.
- Display students with marks greater than 90.
- List students studying in Data Analytics.

---

## 🎯 Learning Outcomes

- Integrated Google Gemini API with Python.
- Applied prompt engineering for natural language to SQL conversion.
- Executed AI-generated SQL queries on a SQLite database.
- Built an interactive web application using Streamlit.
- Connected AI with relational database querying.

---

## 👤 Author

**Eswara Valli**
