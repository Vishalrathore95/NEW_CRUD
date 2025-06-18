# Django Function-Based View CRUD Application

This is a simple **CRUD (Create, Read, Update, Delete)** web application built using **Django** with **Function-Based Views (FBVs)** and **ModelForms**. The app manages student records and displays them in a styled HTML template.

## 🧰 Tech Stack

- **Backend**: Django
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (default with Django)

---

## 📁 Project Structure

crud/
├── crud/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── testapp/
│ ├── migrations/
│ ├── templates/
│ │ ├── index.html
│ │ └── update.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── db.sqlite3
└── manage.py



---

## ⚙️ Setup Instructions

1. **Clone the Repository**  
```bash
[git clone https://github.com/your-username/your-repo-name.git](https://github.com/Vishalrathore95/NEW_CRUD)

Create Virtual Environment

\
python -m venv venv
venv\Scripts\activate   # For Windows
# OR
source venv/bin/activate  # For Linux/macOS
Install Dependencies

pip install django
Run Migrations

python manage.py makemigrations
python manage.py migrate
Run Development Server

python manage.py runserver
Open your browser and visit:

http://127.0.0.1:8000/
🧩 Features
Create new student entries with name, email, and password.

Display all stored records in a dynamic table.

Update any existing record using a separate edit page.

Delete student entries directly from the table.

Beautiful and responsive frontend using CSS.

🔍 File Highlights
models.py
Defines a Testbook model with fields:

python
Copy
Edit
name = models.CharField(max_length=100)
email = models.EmailField(max_length=100)
password = models.CharField(max_length=50)
views.py
Includes function-based views:

create(request) — handles data submission and display.

update_data(request, id) — updates a selected student.

delete_data(request, id) — deletes a selected student.

show_data(request) — displays all data.

index.html
Form for data entry.

Table to show student records with Edit and Delete options.

Styled using custom CSS.

🔗 URLs
Add the following to your urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('update/<int:id>/', views.update_data, name='update_data'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
]
📸 Screenshots

🙌 Contribution
Feel free to fork the repository, raise issues, or open pull requests.

📜 License
This project is licensed under the MIT License.

💡 Author
Vishal Rathore
📧 vishalrathore203@gmail.com


