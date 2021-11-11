FROM alpine:3.8

# Directory where to deploy
RUN \
  # Upgrade all packages
  apk --no-cache -U upgrade && \
  # Install OS dependencies
  apk --no-cache -U add python2 && \
  apk --no-cache -U add --virtual .build-deps \
    git \
    gcc \
    linux-headers \
    python2-dev \
    musl-dev \
    libxml2-dev \
    libxslt-dev \
    && \
  # Python2 PIP
  python -m ensurepip && \
  pip install --no-cache-dir --upgrade pip setuptools 

COPY requirements.txt /tmp/requirements.txt

RUN pip install wheel && \
  pip install --no-cache-dir --upgrade -r /tmp/requirements.txt 

RUN rm -rf \ 
	/tmp/* && \
  apk --no-cache del .build-deps

RUN mkdir -p /app/pingrr /opt /config

# Config volume
VOLUME /config

# Pingrr config file
ENV PINGRR_CONFIG=/config/config.json
# Pingrr log file
ENV PINGRR_LOGFILE=/config/pingrr.log
# Blacklist file
ENV PINGRR_BLACKLIST=/config/blacklist.json

COPY ./pingrr /app/pingrr
COPY ./pingrr.py /app/

WORKDIR /app/

# Entrypoint
ENTRYPOINT ["python2", "pingrr.py"]
