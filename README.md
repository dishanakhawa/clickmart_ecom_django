ClickMart is a full-stack, production-ready e-commerce platform designed with a decoupled architecture. The backend is built on Django REST Framework (DRF) and PostgreSQL, serving structured RESTful APIs secured via JWT authentication. The frontend is built with React (Vite), featuring modular component composition and state management. The entire stack is fully containerized using Docker and Docker Compose for consistent deployment across environments.

                          +-----------------------------------+
                          |     Client / Browser (React)      |
                          +-----------------+-----------------+
                                            |
                                    HTTP / REST APIs
                                            |
                                            v
                          +-----------------+-----------------+
                          |  Gunicorn WSGI / DRF Backend      |
                          |      (Django REST Framework)      |
                          +--------+----------------+---------+
                                   |                |
                          ORM Queries         Media Storage
                                   |                |
                                   v                v
                  +----------------+--+   +---------+---------+
                  | PostgreSQL Server |   |Local/Docker Volume|
                  +-------------------+   +-------------------+

📂 Directory Architecture
django_clickmart_/
├── backend-drf/                # Django REST Framework Backend
│   ├── clickmart_main/         # WSGI & Core Settings
│   ├── products/               # Products & Serializers Module
│   ├── Dockerfile              # Backend Container File
│   └── requirements.txt        # Python Dependencies
│
├── frontend-react/             # React Workspace
│   └── frontend/               # Active React (Vite) Application
│       ├── src/                # Components & UI
│       ├── package.json        # Dependencies
│       └── Dockerfile          # Frontend Container File
│
├── docker-compose.yml          # Local Container Orchestration
└── README.md                   # Project Documentation


🚀 Quick Start with Docker
Prerequisites
Docker Desktop installed and running.

Run the Application
Clone the repository:

Bash
git clone https://github.com/dishanakhawa/clickmart_ecom_django.git
cd clickmart_ecom_django
Build and start containers:

Bash
docker compose up --build
Access the services:

Frontend App: http://localhost:5173

Backend API: http://localhost:8000/api/v1/

Django Admin: http://localhost:8000/admin/

Create Admin Superuser (Optional):

Bash
docker compose exec backend python manage.py createsuperuser
🔌 Core API Endpoints
Method	Endpoint	Description
POST	/api/v1/auth/token/	Obtain JWT token pair
GET	/api/v1/products/	List all e-commerce products
GET	/api/v1/products/<id>/	Get details for a single product
GET/POST	/api/v1/cart/	Retrieve or update cart contents
POST	/api/v1/orders/	Create and place a new order


👤 Author
Disha Nakhawa – GitHub | LinkedIn

                  
