FROM python:2.7

# Create the folder to work in
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Grab the requirements folder, then install production
COPY requirements /usr/src/app/requirements
RUN pip install --no-cache-dir -r requirements/production.txt

# Bring over the rest of the app
COPY . /usr/src/app

# Let Django know we're using production settings
ENV DJANGO_SETTINGS_MODULE emission_events.settings.production
ENV SECRET_KEY quux

# Expose the port for Docker
EXPOSE 8000

# Production runs gunicorn served on port 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
