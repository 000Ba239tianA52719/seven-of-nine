import sqlite3

def init_db():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS votes (
                    message_id TEXT PRIMARY KEY,
                    question TEXT,
                    agree INTEGER DEFAULT 0,
                    disagree INTEGER DEFAULT 0
                )''')
    conn.commit()
    conn.close()

def record_vote(message_id, vote_type):
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    column = "agree" if vote_type == "agree" else "disagree"
    c.execute(f'''UPDATE votes SET {column} = {column} + 1 WHERE message_id = ?''', (message_id,))
    conn.commit()
    conn.close()

def save_vote(message_id, question):
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO votes (message_id, question) VALUES (?, ?)", (message_id, question))
    conn.commit()
    conn.close()

def get_results(message_id):
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute("SELECT agree, disagree FROM votes WHERE message_id = ?", (message_id,))
    result = c.fetchone()
    conn.close()
    return result if result else (0, 0)
