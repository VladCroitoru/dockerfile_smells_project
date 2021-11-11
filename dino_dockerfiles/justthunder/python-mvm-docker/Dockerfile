# VERSION 0.3.0

# The Google App Engine python runtime is Debian Jessie with Python installed
# and various os-level packages to allow installation of popular Python
# libraries.
FROM gcr.io/google_appengine/python-compat-multicore

MAINTAINER Eric Higgins <erichiggins@gmail.com>

# Create a virtualenv for the application dependencies.
# If you want to use Python 3, add the -p python3.4 flag.
RUN apt-get -q update && \
  apt-get install --no-install-recommends -y -q \
    build-essential \
    python2.7 python2.7-dev python-pip \
    git mercurial \
    unzip \
    python-numpy && \
#  pip install -U pip && \
#  pip install virtualenv && \
#  virtualenv /env -p python2.7 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Install dependencies.
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt
