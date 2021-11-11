FROM hakobera/locust

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install python-pip libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME /locust/tests
WORKDIR /locust

COPY requirements.txt /locust/requirements.txt
RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "--no-cache-dir", "install", "--upgrade", "nose"]
RUN ["pip", "--no-cache-dir", "install", "-r", "requirements.txt"]

