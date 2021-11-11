FROM python:3
WORKDIR /usr/src/app
EXPOSE 8000

# Install poetry and deps
# Exporting to requirements.txt will avoid hassle with poetry venv
COPY pyproject.toml ./
COPY poetry.lock ./
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY manage.py manage.py
COPY ds ds
COPY dayliostats dayliostats

# Collect static files, pass dummy DS_SECRET_KEY
# or else ./manage.py will fail
# since DS_SECRET_KEY is not available during the build step
RUN DS_SECRET_KEY=dummy ./manage.py collectstatic

# Run server
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "dayliostats.wsgi" ]
