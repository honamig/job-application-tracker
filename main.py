import sqlite3

connection = sqlite3.connect("applications.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        application_date TEXT,
        status TEXT,
        notes TEXT
        )
        """)

connection.commit()

# cursor.execute("""
#     INSERT INTO applications
#     (company, position, application_date, status, notes)
#     VALUES (?, ?, ?, ?, ?)
# """, (
#     "Example Tech",
#     "Software Engineer",
#     "2026-11-09",
#     "Applied",
#     "Online application"
# ))

# connection.commit()

print("Job application added successfully")

# Update the application status
cursor.execute("""
    UPDATE applications
    SET status = ?
    WHERE id = ?
""", ("Interview", 1))

connection.commit()

print("Application status updated successfully")

# Get all job applications
cursor.execute("SELECT * FROM applications")

# Fetch all records
applications = cursor.fetchall()

# Display applications
print("\n=== Job Applications ===")

for application in applications:
    print(application)

connection.close()