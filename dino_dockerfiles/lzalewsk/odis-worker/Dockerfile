FROM debian:jessie
MAINTAINER luka <lzalewsk@gmail.com>

# Get and install required packages.
RUN apt-get update && apt-get install -y -q \
    build-essential \
    python-dev \
    python-pip \
  && rm -rf /var/lib/apt/lists/*

# Install required dependencies (includes Flask and uWSGI)
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Create a place to deploy the application
ENV APP_DIR /app

RUN mkdir -p $APP_DIR
COPY odisworker.py $APP_DIR

ADD ssl /ssl
ADD conf /conf
WORKDIR $APP_DIR

CMD ["python","odisworker.py"]
#CMD ["/bin/bash"]
