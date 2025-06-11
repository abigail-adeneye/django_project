# django_project
A Django application that creates employee-related models, seed the database with dummy data, expose API endpoints using Django REST Framework, visualize employee analytics via charts (optional) and documents my work properly.  ---

# Company Management API
A Django-based REST API system for managing departments, employees, attendance, and performance within a company. It also includes JWT authentication and visual charts using DRF and Chart.js.

## 📁 Table of Contents
* Project Description
* Features
* Installation
* Running the Project
* API Usage Guide
* Swagger Documentation
* Credits
* Licence
* Contributing


---

## Project Description
This project serves as a backend management tool to:

* Create and manage departments and employees.
* Track employee attendance and performance.
* Generate visual reports and statistics using chart views.
* Provide secure access using JWT authentication.
* Support API documentation via Swagger and Redoc.

---

## Features
* CRUD operations for departments, employees, attendance, and performance.
* Token-based authentication via JWT.
* Visual charts: employees per department and monthly attendance.
* Interactive API documentation with Swagger and Redoc.
* Modular and extensible architecture using Django REST Framework.

---

##  Installation
1. **Clone the repository**

```bash
git clone https://github.com/abigail-adeneye/django_project.git
cd django_project
```
2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```
4. **Apply migrations**

```bash
python manage.py migrate
```
5. **Create a superuser (optional)**

```bash
python manage.py createsuperuser
```
6. **Run the development server**

```bash
python manage.py runserver
```

---

##  Running the Project

Once the server is running, navigate to:

* http://127.0.0.1:8000/swagger/ — Swagger API docs
* http://127.0.0.1:8000/redoc/ — Redoc API docs
* http://127.0.0.1:8000/api/charts/ — Chart page

---

##  API Usage Guide

### Authentication (JWT)
* `POST /api/token/` – Obtain token
* `POST /api/token/refresh/` – Refresh token

### Endpoints

* `/api/departments/` – CRUD for departments
* `/api/employees/` – CRUD for employees
* `/api/attendance/` – CRUD for attendance
* `/api/performance/` – CRUD for performance

### 📊 Charts

* `/api/charts/` – Main chart dashboard
* `/api/charts/employees-per-department/` – Employee distribution
* `/api/charts/monthly-attendance/` – Monthly attendance stats

---

## 📚 Swagger Documentation

Interactive API documentation available at:

* http://127.0.0.1:8000/swagger/
* http://127.0.0.1:8000/redoc/

---

##  Credits

* **Developer**: Adeneye Abigail
* **Libraries**: Django, Django REST Framework, Simple JWT, drf-yasg

---
## License

This project is licensed under the MIT License. See LICENSE for details.




##  Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---


