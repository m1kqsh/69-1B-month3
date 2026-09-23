CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT
);
"""

SELECT_USER = """
SELECT user_id, username, first_name FROM users WHERE user_id = ?;
"""

INSERT_USER = """
INSERT INTO users (user_id, username, first_name) VALUES (?, ?, ?);
"""

SELECT_ALL_USERS = """
SELECT user_id, username, first_name FROM users;
"""

DELETE_USER = """
DELETE FROM users WHERE user_id = ?;
"""