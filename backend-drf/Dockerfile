# Purpose: A Dockerfile is a step-by-step instruction file that tells Docker how to build and run our application.
FROM python:3.10-slim
# lighteweight version of python, which is smaller in size and faster to run. It is a lightweight version of python.

ENV PYTHONUNBUFFERED=1
# used for debugging, it tells python to not buffer the output and to print it to the console immediately. This is useful for debugging because we can see the output of our application in real-time.
ENV PYTHONDONTWRITEBYTECODE=1
# avoid py to create unnecessary .pyc files, which are compiled python files that are not needed for our application to run. This is useful because it reduces the size of our docker image and makes it faster to build and run.

WORKDIR /app
# Set the working directory for the application inside the container. All subsequent commands will be run from this directory.

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
    # linux packages that are needed for our application to run. gcc is a compiler that is needed to compile some of the python packages that we are using in our application. libpq-dev is a library that is needed to connect to a PostgreSQL database.

COPY requirements.txt .
# source n destination
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# . - copy source files
# . - put inside the destination

EXPOSE 8000

# gunicorn = production server, clickmart_main.wsgi:application = Django entry point, --bind 0.0.0.0:8000 = external traffic. Reminaing: tuning options
# A worker is just one instance of your Django app running inside Gunicorn.
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn clickmart_main.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 1 --timeout 120"]