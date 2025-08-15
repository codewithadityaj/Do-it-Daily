# Do It Daily – Django Backend

This is the backend for **Do It Daily**, a habit tracking and productivity application.  
It is built with **Django** and **Django REST Framework**, providing APIs for user authentication, habit management, and analytics.


## 📂 Project Structure
```
.
├── .vscode/ # VS Code workspace settings
├── bin/ # Virtual environment binaries
├── did/ # Django project source code
├── lib/python3.10/site-packages/ # Installed Python packages (venv)
├── .gitignore # Git ignored files
├── pyvenv.cfg # Virtual environment configuration
```

> **Note:** The `major project front end` folder is not part of this backend setup.

## 🚀 Features
```
- **User Authentication** – Signup, login, logout, JWT token-based authentication
- **Habit Management** – Create, update, delete, and track habits
- **Analytics** – View progress and habit statistics
- **Modular Apps** – Separate apps for accounts, habits, analytics, and more
```

## 🛠️ Tech Stack
```
- **Python 3.10+**
- **Django 4+**
- **Django REST Framework**
- **SQLite / PostgreSQL** (configurable)
- **Virtual Environment** for dependencies
```
## 📦 Installation

1. **Clone the repository**
   ```
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
2. **Activate Virtual Environment**
```
source bin/activate   # Linux/Mac
.\Scripts\activate    # Windows
```

3. **Install Dependencies**

```
pip install -r requirements.txt
```

4. **Run Migrations**

```
python manage.py makemigrations
python manage.py migrate
```

5. **Run Development Server**

```
python manage.py runserver

```

🔑 API Endpoints (Example)

```
Method	        Endpoint	                 Description
POST	    /api/accounts/signup/       Register a new user
POST	    /api/accounts/login/	     Login and get JWT token
GET	        /api/habits/	              List all habits
POST	      /api/habits/	             Create a new habit
PUT	      /api/habits/<id>/	            Update a habit
DELETE	  /api/habits/<id>/	              Delete a habit
```
