# Dockerfile

# Start with the latest python 2.x version
FROM python:2.7.13

# Build App
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY upstream/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY upstream/ /usr/src/app
COPY upstream/reset_db.sh /reset_db.sh
# Get the "built" version of runapp.sh
COPY upstream/runapp.sh /runapp.sh

# Initialize app database
RUN ["/reset_db.sh"]

# Add Cloud One Application Security
RUN pip install trend_app_protect


EXPOSE 8000

CMD ["/runapp.sh"]
