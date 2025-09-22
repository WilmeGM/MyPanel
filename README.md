# 📋 MyPanel
Personal panel app built in Ignition Perspective (8.1) with user authentication, profile, settings, and task management (CRUD).
It is a **personal panel app** where a user can register, log in, manage settings, view and update profile data and manage tasks through a web interface.

## 📦 Requirements

- Ignition 8.1+ installed on your system.  
- A SQLite database configured in Ignition (`MyPanelDB` was used in this project).  
- Basic knowledge of Ignition Designer to import projects.

## 🚀 Installation

1. Clone this repository or download the ZIP file.  
2. From **Ignition Designer**:  
   - Menu: `File > Import Project...`  
   - Select the exported MyPanel project file (`MyPanel.zip`).  
   - Assign a project name (e.g., `MyPanel`).  
3. Make sure the `MyPanelDB` database connection is configured.  
   - Create the following tables:

```sql
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    bio TEXT
);

CREATE TABLE IF NOT EXISTS Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    is_completed INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
```

## ✨ Main Features

- **Home Screen**: shows a random app quote when you click a button, that is consuming an API.  
- **Register**: user registration with validations and password encryption (SHA-256).  
- **Login**: user login with database validation.  
- **Logout**: manual session termination.  
- **Profile Screen**: update username, email, and password.  
- **Settings Screen**: placeholder for user preferences.  
- **Tasks Screen (CRUD)**:  
  - Add new tasks.  
  - View user tasks.  
  - Edit task title or description.  
  - Mark tasks as completed with a checkbox.  
  - Delete tasks.  
- **Basic authorization**:  
  - Pages require a valid user session (manual validation using `session.custom`).  
  - If no session exists, access is denied from the UI.

## 🔒 Security Notes

- Authentication and authorization are implemented **manually** with scripting (`session.custom`).  
- This approach is fine for practice but **not recommended for production use**.
