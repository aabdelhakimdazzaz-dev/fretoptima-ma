import gradio as gr
import sqlite3
import pandas as pd
from datetime import datetime

# Kan-creeiw database ila ma kantch
def init_db():
    conn = sqlite3.connect('fretoptima.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, 
                  nom TEXT, 
                  email TEXT UNIQUE, 
                  password TEXT, 
                  role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS demandes
                 (id INTEGER PRIMARY KEY, 
                  client_id INTEGER, 
                  origine TEXT, 
                  destination TEXT, 
                  poids REAL, 
                  date_ch TEXT, 
                  statut TEXT DEFAULT 'ouvert',
                  created_at TEXT)''')
    conn.commit()
    conn.close()

init_db()

with gr.Blocks(title="FretOptima MA") as app:
    gr.Markdown("# 🚚 FretOptima MA")
    gr.Markdown("### Plateforme d'optimisation des retours à vide")
    
    with gr.Tab("Test"):
        gr.Markdown("✅ Step 1 khdam! Database tsaybat.")

app.launch()
