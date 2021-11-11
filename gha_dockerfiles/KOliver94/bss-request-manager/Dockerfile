# Stage 1 - Build Frontend

# Pull base image
FROM node:14-alpine AS react-build

# Build args
ARG API_URL
ARG AUTHSCH_CLIENT_ID
ARG FACEBOOK_CLIENT_ID
ARG GOOGLE_CLIENT_ID
ARG RECAPTCHA_SITE_KEY
ARG SENTRY_URL

# Environment vars
ENV REACT_APP_API_URL=$API_URL
ENV REACT_APP_AUTHSCH_CLIENT_ID=$AUTHSCH_CLIENT_ID
ENV REACT_APP_FACEBOOK_CLIENT_ID=$FACEBOOK_CLIENT_ID
ENV REACT_APP_GOOGLE_CLIENT_ID=$GOOGLE_CLIENT_ID
ENV REACT_APP_RECAPTCHA_SITE_KEY=$RECAPTCHA_SITE_KEY
ENV REACT_APP_SENTRY_URL=$SENTRY_URL

# Set work directory
WORKDIR /app/frontend

# Copy package.json and package-lock.json to Docker environment
COPY ./frontend/package*.json /app/frontend/

# Install all required node packages
RUN npm install --silent

# Copy everything over to Docker environment
COPY ./frontend /app/frontend

# Build the frontend
RUN npm run build

##################################################

# Stage 2 - The Production Environment

# Pull base image
FROM python:3.9-alpine AS request-manager

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/backend

# Create the app user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy Pipfile and Pipfile.lock to Docker environment
COPY ./backend/Pipfile* /app/backend/

# Install dependencies
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev cargo openldap-dev build-base \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy --clear \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps \
    && pip uninstall pipenv -y

# Copy everything over to Docker environment
COPY ./backend /app/backend

# Copy built frontend assets
RUN mkdir -p /app/frontend/build
COPY --from=react-build /app/frontend/build /app/frontend/build

# Have to move all static files other than index.html to root/ for whitenoise middleware
WORKDIR /app/frontend/build
RUN mkdir root && mv *.ico *.json *.js *.txt root || :

# Change the owner of all files to the app user
RUN chown -R appuser:appgroup /app

# Change to the app user
USER appuser

# Collect static files
WORKDIR /app/backend
RUN python manage.py collectstatic --no-input --clear --settings=core.settings.common

# Open port
EXPOSE 8000

# Copy and run entrypoint.sh
COPY --chown=appuser:appgroup ./docker-entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Set health check
HEALTHCHECK --start-period=10s --interval=5m \
    CMD python manage.py health_check

# Start the server
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--workers=5", "--threads=2", "core.wsgi"]
