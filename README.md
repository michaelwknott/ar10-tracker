# ar10-tracker

## About the Project
A web app to collect, store and visualise 10m Air Rifle Training and Competition Data.

The web app provides the following functionality:
+ Create, Read, Update and Delete 10m Air Rifle Competition and Training data
+ View a summary of the Competition and Training data in the main dashboard
+ Import and export data in csv format for compatibility with existing data analysis workflows

### Built With
+ [Django](https://www.djangoproject.com/)
+ [Postgres](https://www.postgresql.org/)
+ [Bootstrap5](https://getbootstrap.com/)
+ [Chart.js](https://www.chartjs.org/)

## Getting Started

### Prerequisites
+ Python version >= 3.11.0

### Installation

1. Clone the repo
    ```
    git clone git@github.com:michaelwknott/ar10-tracker.git
    ```

2. Create a virtual environment
   ```
   python -m venv .venv --prompt .
   ```

3. Activate your virtual environment
   ```
   .venv/bin/activate
   ```

4. Install requirements
   ```
   python -m pip install requirements.txt
   ```

5. Install Postgres. See the following link for installing on [Linux](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart)

6. Create a Postgres database. See the following [blog post](https://michaelwknott.github.io/using-postgresql-with-django.html)

7. Rename `.env_template`
   ```
   mv .env_template .env
   ```

8. Update `.env` file with required environment variables. Example environment variables are used below. Ensure you update with your own variables 
   ```
   SECRET_KEY="django-insecure-z_)j=_h=5fmfob9l#vm)p)(#w7-w-v!p57eh^=36-jfmcoaf7t"
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1
   DATABASE_URL=postgres://myuser:mypassword@127:0.0.1:5432/ar10_tracker
   ```

9. Run Django migrations
   ```
   python manage.py migrate
   ```

10. Create Django superuser
  ```
python manage.py createsuperuser
```

11. Optional: Populate database with dummy data
  ```
  python manage.py dbtestdata
```

12. Run the web app locally
  ```
  python manage.py runserver
```
## Roadmap

- [ ] Add demo to README.md
- [ ] Add htmx to avoid fullpage reload on delete

## License
Distributed under the MIT License. See `LICENSE` for more information.
