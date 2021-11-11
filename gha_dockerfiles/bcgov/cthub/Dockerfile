# This is for Heroku deployment
# Somewhat based on https://github.com/cfranklin11/docker-django-react
FROM python:3.9.1

# Install Node and npm
RUN apt-get -y install curl \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash \
  && apt-get install nodejs \
  && curl -L https://www.npmjs.com/install.sh | sh

WORKDIR /app/backend

# Install Python Libraries
COPY ./django/requirements.txt /app/backend/
RUN pip3 install --upgrade pip -r requirements.txt

COPY ./django/ /app/backend

# Install Package.json
WORKDIR /app/frontend

COPY ./react/package.json /app/frontend/
RUN npm install --force

# Copy the frontend code
COPY ./react/ /app/frontend

# Build frontend files
RUN npm run build

# Move the static files up one level
WORKDIR /app/frontend/public

RUN mv static/* /app/frontend/public
# RUN mv static/bundle.js.map /app/frontend/public

# Prepare the environment variables
WORKDIR /app/backend

RUN mkdir /app/backend/staticfiles
ENV DATABASE_URL=$DATABASE_URL
EXPOSE $PORT

# Run the server (saving the old one for reference)
# CMD ["sh", "-c", "python3 backend/manage.py migrate && python3 backend/manage.py runserver 0.0.0.0:$PORT"]
CMD ["sh", "-c", "python3 manage.py migrate api && gunicorn api.wsgi:application --bind 0.0.0.0:$PORT"]
