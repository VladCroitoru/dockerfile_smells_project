FROM python:3.6

LABEL maintainer "Michael Hahn <mhahn.dev@gmail.com>"

RUN rm /dev/random && ln -s /dev/urandom /dev/random

# Copy all app files
COPY . /usr/local/bin/hdtapps-prototype
WORKDIR /usr/local/bin/hdtapps-prototype

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the HTTP server port
EXPOSE 8080

# Run the app
CMD python -m run

#
# Manually build by running:
#
#   docker build -t trade4chor/hdtapps-framework .
#
# 

