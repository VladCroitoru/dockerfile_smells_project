# Use an official Python runtime as a parent image
FROM python:latest

#HELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /app/
RUN pipenv install 


# Add the rest of the code
COPY . /app

WORKDIR /app

COPY ./entrypoint.sh /app/entrypoint.sh

#RUN dos2unix /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

RUN useradd -m m5no0p
USER m5no0p

ENTRYPOINT ["/app/entrypoint.sh"]

EXPOSE $PORT

#CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
