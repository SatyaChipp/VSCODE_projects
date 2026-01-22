# Storefront 🛒

A Django-based backend project demonstrating clean project structure, REST-style APIs, and modern Python tooling.
Basic CRUD operations

## 🚀 Features

- Django 5.x project setup
- Modular app structure (`api`, `playground`, etc.)
- User CRUD-style API endpoints
- SQLite database (easy local setup)
- Ready for extension with Django REST Framework
- Virtual environment managed via Pipenv

---

## 🧰 Tech Stack

- **Python**: 3.11
- **Django**: 5.2+
- **Database**: SQLite3
- **Package Manager**: Pipenv
- **OS**: macOS / Linux / Windows

---

## 📁 Project Structure
torefront/
│
├── api/
│ ├── urls.py
│ ├── views.py
│ └── models.py
│
├── playground/
│ ├── urls.py
│ └── views.py
│
├── storefront/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── Pipfile
├── Pipfile.lock
├── manage.py
└── README.md

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/storefront.git
cd storefront
#install dependencies
pipenv install
pipenv shell
#run migrations
python manage.py migrate
#start dev server
python manage.py runserver
```
Method	Endpoint	Description
GET	/api/users/	List users
POST	/api/users/create/	Create a user
GET	/api/users/<id>/	Get user details
