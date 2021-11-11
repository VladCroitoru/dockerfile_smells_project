FROM ubuntu:16.04

LABEL maintainer "coveo"

# Create puppet user and group with defined UID and GID
RUN useradd -u 1000 -U puppet

# Get laset version
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Install requirements
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    wget \
    cron \ 
    python \
    puppet \
    python-setuptools \
    python-dev build-essential \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    libffi-dev

RUN easy_install pip

RUN service puppet stop && systemctl disable puppet

# Create install dir and clean apt cache
RUN mkdir /install && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    touch /var/log/cron.log
COPY files/install /install

RUN pip install -r /install/requirements.txt

RUN chmod +x /install/entrypoint.sh

CMD ["/install/entrypoint.sh"]
