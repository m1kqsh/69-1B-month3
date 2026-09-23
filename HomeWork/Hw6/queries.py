CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT
);
"""

CREATE_TABLE_RESULTS = """
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    score INTEGER,
    total_questions INTEGER,
    completed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
"""

SELECT_USER = "SELECT user_id, username, first_name FROM users WHERE user_id = ?;"
INSERT_USER = "INSERT INTO users (user_id, username, first_name) VALUES (?, ?, ?);"
SELECT_ALL_USERS = "SELECT user_id, username, first_name FROM users;"
DELETE_USER = "DELETE FROM users WHERE user_id = ?;"

INSERT_RESULT = "INSERT INTO results (user_id, score, total_questions) VALUES (?, ?, ?);"
SELECT_USER_RESULTS = "SELECT score, total_questions, completed_at FROM results WHERE user_id = ?;"

SELECT_ALL_RESULTS_WITH_USERS = """
SELECT users.first_name, users.username, results.score, results.total_questions, results.completed_at
FROM results
INNER JOIN users ON results.user_id = users.user_id;
"""