
# https://hub.docker.com/_/python
FROM python:3.9-slim-buster

# allow log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# copy local code to the container
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run the gunicorn server
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 index:app
