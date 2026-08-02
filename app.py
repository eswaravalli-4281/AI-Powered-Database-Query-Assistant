from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in .env file.")
    st.stop()

genai.configure(api_key=api_key)

# ==========================
# Gemini Function
# ==========================
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-flash-latest")

        response = model.generate_content(
            [prompt[0], question]
        )

        sql = (
            response.text
            .replace("```sql", "")
            .replace("```", "")
            .strip()
        )

        return sql

    except Exception as e:
        st.error(f"Gemini Error:\n\n{e}")
        return None


# ==========================
# SQLite Function
# ==========================
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        conn.close()

        return rows

    except sqlite3.Error as e:
        st.error(f"SQLite Error:\n\n{e}")
        return None


# ==========================
# Prompt
# ==========================
prompt = [
"""
You are an expert in converting English questions into SQL queries.

The database contains one table named STUDENT.

Columns:
- NAME
- CLASS
- SECTION
- MARKS

Examples:

Question:
How many entries of records are present?

SQL:
SELECT COUNT(*) FROM STUDENT;

Question:
Tell me all the students studying in Data Science class.

SQL:
SELECT * FROM STUDENT
WHERE CLASS='Data Science';

Rules:
1. Return ONLY the SQL query.
2. Do NOT return explanations.
3. Do NOT use markdown.
4. Output must be valid SQLite SQL.
"""
]

# ==========================
# Streamlit UI
# ==========================
st.set_page_config(page_title="Gemini SQL Query App")

st.title("🤖 Gemini SQL Query Generator")

question = st.text_input("Ask your question")

if st.button("Generate SQL"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    sql_query = get_gemini_response(question, prompt)

    if sql_query:

        st.subheader("Generated SQL Query")

        st.code(sql_query, language="sql")

        data = read_sql_query(sql_query, "student.db")

        st.subheader("Query Result")

        if data is None:
            pass
        elif len(data) == 0:
            st.info("No records found.")
        else:
            for row in data:
                st.write(row)
