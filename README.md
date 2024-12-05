# Assignment06
# Development of a Property Management System Using Django

Development of a geospatially-enabled Property Management System using Django and PostgreSQL with PostGIS.

## Table of Contents
- [Description](#description)
- [Git Clone Instructions](#git-clone-instructions)
- [Access the Application](#access_the_application)
- [Sitemap Generation](#sitemap_generation)
- [Test](#test)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Code Coverage](#code_coverage)
- [Schema](#schema)
- [Authorization Rules](#authorization_rules)
- [Dependencies](#dependencies)
- [Remember](#remember)


## Description

The project aims to create a robust Django-based Property Management System with advanced data handling capabilities. It integrates PostgreSQL with PostGIS to manage geospatial property data and includes a well-structured admin interface for property management tasks.

## Git Clone Instructions

To clone this project to your local machine, follow these steps:

1. **Open terminal (Command Prompt, PowerShell, or Terminal)**

2. **Clone the repository**:
   
         git clone https://github.com/M-E-U-E/Assignment_6.git or git clone git@github.com:M-E-U-E/Assignment_6.git
   
    Go to the Directory:
    ```bash
    cd Assignment_6
    ```
4. **Set Up Virtual Environment**
   
    ```bash
    # Create virtual environment On macOS/Linux:
       python -m venv env
       source venv/bin/activate
       pip install django
    # Activate virtual environment
    # Create virtual environment On Windows:
       python -m venv env
       venv\Scripts\activate
       pip install django
    
    ```
    Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
    If requirements.txt is missing, install these packages:
    ```bash
    pip install Django==4.2
    pip install psycopg2-binary
    pip install gunicorn==21.0.1
    pip install django-postgres-extensions==0.9.3
    pip install django-import-export

    ```
5. **Docker Instructions**

    To run the project using Docker, follow these steps:

    Build and Run Docker Containers Ensure you have Docker and Docker Compose installed. Then, use the following commands to build and run the containers:
  ```
      docker compose build
      docker compose up
   ```

   This will start both the PostgreSQL/PostGIS container and the Django application container.
   
   Apply Migrations in Docker After the containers are up, run the migrations inside the Django container:
   ```
   docker exec -it django_web python manage.py makemigrations
   docker exec -it django_web python manage.py migrate
   ```
   
   Create a Superuser in Docker Create a superuser to access the admin panel:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```
   then create superuser
   ```
      Username (leave blank to use 'root'): 
      Email address: 
      Password: 
      Password (again): 
   ```
## Access the Application

      The Django application will be available at http://127.0.0.1:8000.
      The admin panel can be accessed at http://127.0.0.1:8000/admin.
      The Signup panel can be accessed at http://127.0.0.1:8000/signup.
      The Login panel can be accessed at http://127.0.0.1:8000/login.

## Sitemap Generation
   Add locations through json file:
   ```
   docker-compose exec web python manage.py loaddata locations_fixture.json
   ```
   then generate the sitemap
   
   Run this code:
   ```
      docker-compose exec web python manage.py generate_sitemap
   ```
   This will create a sitemap.json containing all property locations.
   
   #### After this we can import or export csv file, json file.


## Test
  Run the testing file:
   ```
      docker-compose run web coverage run manage.py test
   ```
  Run the testing html:
   ```
      docker-compose run web coverage html
   ```
  See the testig html:
   ```
      xdg-open htmlcov/index.html
   ```
    

## Project Structure
```
Assignment_6/           # Root Django project directory
├── inventory_management/       # Django project module
│   ├── __pycache__/            # Compiled Python files
│   ├── __init__.py             # Module initializer
│   ├── asgi.py                 # ASGI configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Project URL configuration
│   ├── wsgi.py                 # WSGI configuration
├── properties/                 # Django application module
│   ├── management/commands/    # Custom Django management commands
│   ├── migrations/             # Database migration files
│   │   ├── __init__.py         # Migration module initializer
│   ├── __pycache__/            # Compiled Python files
│   ├── admin.py                # Admin interface customization
│   ├── apps.py                 # App configuration
│   ├── models.py               # Database models
│   ├── tests.py                # Unit tests for the app
│   ├── views.py                # Application views
├── static/                     # Static files (CSS, JavaScript, Images)
│   ├── css/                    # Stylesheets
│   ├── images/                 # Images
│   ├── js/                     # JavaScript files
├── templates/                  # HTML templates
│   ├── activation.html         # Activation page template
│   ├── base.html               # Base layout template
│   ├── login.html              # Login page template
│   ├── owner_signup.html       # Owner signup template
│   ├── signup.html             # User signup template
├── .coverage                   # Coverage report file
├── .env                        # Environment variables
├── .gitignore                  # Git ignore rules
├── accommodations_fixture.json # Accommodation fixture data
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Dockerfile for containerizing the project
├── init.sql                    # SQL initialization script
├── locations_fixture.json      # Location fixture data
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── sitemap.json                # Sitemap configuration
├── README.md 
```
## Technologies Used

- **Backend Framework: Django (Python web framework for rapid development and clean design)
- **Authentication: Django's built-in authentication system for user management and session handling
- **Database: PostgreSQL with PostGIS extension for geospatial data handling and relational database management
- **Admin Interface: Django Admin for managing properties, users, and data
- **Data Import/Export: Django Import-Export for handling data uploads and downloads in the admin interface
- **Templates: HTML, CSS, JavaScript for frontend design and integration
- **Containerization: Docker and Docker Compose for creating isolated development and production environments
- **Testing Frameworks: Django Test Framework and pytest for unit and integration tests
- **Geospatial Data: PostGIS for location-based data queries and spatial indexing
- **Environment Management: .env file for securely storing and managing environment variables
- **Dependency Management: Pip with requirements.txt for managing Python libraries
- **Version Control: Git for tracking changes and collaboration
- **Fixtures: JSON files for preloading test and initial data into the database
- **Code Coverage: Coverage.py for tracking test coverage of the project
  
## Code Coverage  
      Coverage report: 97%
      - Files
        - inventory_management/__init__.py
        - inventory_management/settings.py
        - inventory_management/urls.py
        - manage.py
        - properties/__init__.py
        - properties/admin.py
        - properties/apps.py
        - properties/migrations/__init__.py
        - properties/migrations/0001_initial.py
        - properties/migrations/0002_propertyowner_user.py
        - properties/models.py
        - properties/tests.py
        - properties/views.py
      - Functions
      - Classes


## Schema
  Database Schema (In-Memory):
  ```
  Users Table:
  +----------+-----------+----------+-------+
  | id       | username  | email    | role  |
  +----------+-----------+----------+-------+
  | string   | string    | string   | string|
  +----------+-----------+----------+-------+

  Accommodations Table:
  +----------+----------+---------------+--------+--------+-------------+----------+----------+------------+------------+
  | id       | feed     | title         | country_code | bedroom_count | review_score | usd_rate | center     | user_id    | published |
  +----------+----------+---------------+--------+--------+-------------+----------+----------+------------+------------+
  | string   | int      | string        | string | int     | decimal     | decimal  | PointField | ForeignKey | bool      |
  +----------+----------+---------------+--------+--------+-------------+----------+----------+------------+------------+

  LocalizeAccommodations Table:
  +----------+---------------+----------+-------------+--------+
  | id       | property_id   | language | description | policy |
  +----------+---------------+----------+-------------+--------+
  | int      | ForeignKey    | string   | text        | JSON   |
  +----------+---------------+----------+-------------+--------+

  Locations Table:
  +----------+--------+-------------+----------+----------------+-------------+----------+----------+------------+------------+
  | id       | title  | center      | parent_id| location_type  | country_code| state_abbr| city     | created_at | updated_at |
  +----------+--------+-------------+----------+----------------+-------------+----------+----------+------------+------------+
  | string   | string | PointField  | ForeignKey| string         | string      | string   | string   | datetime   | datetime   |
  +----------+--------+-------------+----------+----------------+-------------+----------+----------+------------+------------+

  PropertyOwners Table:
  +----------+--------+----------+----------+-------------+------------+
  | id       | name   | email    | phone    | address     | created_at |
  +----------+--------+----------+----------+-------------+------------+
  | string   | string | string   | string   | text        | datetime   |
  +----------+--------+----------+----------+-------------+------------+
```
  
  ## Authorization Rules:
   ```
     Role Permissions:
      ├── Admin
      │   ├── View all Locations
      │   ├── Create, Update, and Delete Locations
      │   ├── View all Accommodations
      │   ├── Create, Update, and Delete Accommodations
      │   ├── View all LocalizeAccommodations
      │   ├── Create, Update, and Delete LocalizeAccommodations
      │   ├── View all Users
      │   └── Create, Update, and Delete Users
      └── User
       ├── View Locations
       ├── View Accommodations
       ├── Create, Update, and Delete their own LocalizeAccommodations
       ├── View their own User profile
       └── Update their own User profilee
   ```
 ## Dependencies
    Django: Web framework for building scalable and robust backend applications.
    PostgreSQL: Relational database system with PostGIS extension for geospatial support.
    django-import-export: For importing and exporting data via the Django admin interface.
    psycopg2: PostgreSQL adapter for Python, required for database integration with Django.
    PostGIS: Extension for PostgreSQL to handle geospatial data and queries.
    pytest: Python testing framework for writing and executing test cases.
    pytest-django: Extension of pytest for testing Django applications.
    coverage.py: Code coverage measurement tool for tracking test coverage.
    django-cors-headers: For handling Cross-Origin Resource Sharing (CORS) in the project.
    django-environ: For managing environment variables securely in the project.
    Docker: For containerizing the application and creating isolated environments.
    Flake8: Python linting tool for enforcing coding style and standards.
    gunicorn: Python WSGI HTTP server for deploying the Django application.
 ### Remember:
    Database Configuration:
    
    Ensure PostgreSQL is set up and connected to Django.
    Enable PostGIS extension for geospatial capabilities.
    Environment Variables:
    
    Store sensitive information like SECRET_KEY and database credentials securely using .env files or other secure methods.
    Testing:
    
    Write unit tests for models, views, and API endpoints.
    Use pytest and pytest-django for tests.
    Track code coverage using coverage.py.
    Code Formatting:
    
    Follow consistent code style and standards.
    Use tools like Flake8 for readability and maintainability.
    Security:
    
    Use secure password handling and authentication methods.
    Enable HTTPS for production environments.
    Configure CORS headers properly for API security.
    Docker Deployment:
    
    Set up Docker and Docker Compose for containerization.
    Ensure portability across different environments.
    Documentation:
    
    Provide clear setup documentation, including database configuration, Docker setup, and environment variable management.
    Use tools like Swagger/OpenAPI for API documentation.
    Version Control:
    
    Keep the Git repository updated with meaningful commit messages.
    Ensure .gitignore excludes unnecessary files like __pycache__, .env, and temporary files.
    Migrations:
    
    Create and apply migrations for database schema changes.
    Version control migrations with the repository.
    Geospatial Data Handling:
    
    Properly handle and store geospatial data using PostGIS in PostgreSQL.
