# Stack Exchange Cross-Tag Analysis

FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY app/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app/* /usr/src/app/

# Prepare the volume for the static visualization files
VOLUME /var/www

# Make the folder structure compatible with the dev environment
RUN ln -s /var/www /usr/src/www

# Serve the static visualization files
WORKDIR /var/www
CMD ["python", "-m", "http.server", "8000"]
