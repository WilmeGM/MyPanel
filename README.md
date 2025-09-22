# 📋 MyPanel
<img width="700" height="500" alt="home" src="https://github.com/user-attachments/assets/742f1949-d9b1-4092-aaeb-168c3d7c27a5" />

Personal panel app built in Ignition Perspective (8.1) with user authentication, profile, settings, and task management (CRUD).
It is a **personal panel app** where a user can register, log in, manage settings, see and update profile data and manage tasks through a web interface.

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
  
  <img width="600" height="500" alt="home" src="https://github.com/user-attachments/assets/43dd4eaf-bc7a-4596-b688-494f00cce187" />

- **Register**: user registration with validations and password encryption (SHA-256).
  
  <img width="500" height="400" alt="register" src="https://github.com/user-attachments/assets/40470201-dd4b-41c6-a0e4-3ff80ce6059e" />

- **Login**: user login with database validation.
  
<img width="500" height="400" alt="log in" src="https://github.com/user-attachments/assets/be79ac40-6ba4-4ead-aab8-bca6e61ba534" />
  
- **Logout**: manual session termination.
  
<img width="500" height="400" alt="log out" src="https://github.com/user-attachments/assets/a7d6deec-3214-47df-aa8a-e5b824dd0771" />
<img width="500" height="400" alt="log out2" src="https://github.com/user-attachments/assets/3ffc4abf-8a30-4061-bfdd-fb14ee728294" />

- **Profile Screen**: update username, email, and password.

<img width="500" height="400" alt="profile" src="https://github.com/user-attachments/assets/9c4bc7e4-e5b9-4c73-a79a-99241b43c36b" />
  
- **Settings Screen**: placeholder for user preferences.

<img width="500" height="400" alt="setting" src="https://github.com/user-attachments/assets/b6122063-d7d5-40f7-bc2d-cd00658101e2" />

- **Tasks Screen (CRUD)**:  
  - Add new tasks.  
  - View user tasks.  
  - Edit task title or description.  
  - Mark tasks as completed with a checkbox.  
  - Delete tasks.

<img width="500" height="400" alt="crud" src="https://github.com/user-attachments/assets/a33c6fba-5d6e-444d-9bd2-ad949a961376" />

- **Basic authorization**:

<img width="500" height="400" alt="auth" src="https://github.com/user-attachments/assets/383144ab-ee19-43cb-89b2-4c3e8f9a410f" />

  - Pages require a valid user session (manual validation using `session.custom`).  
  - If no session exists, access is denied from the UI.

## 🔒 Security Notes

- Authentication and authorization are implemented **manually** with scripting (`session.custom`).  
- This approach is fine for practice but **not recommended for production use**.
