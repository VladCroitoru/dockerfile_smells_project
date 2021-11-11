# set the base image
FROM python:3.9-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn --chdir SchoolApp/ SchoolApp.wsgi --bind 0.0.0.0:8000 --workers 3
