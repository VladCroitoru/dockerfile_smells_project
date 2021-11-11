FROM ubuntu:latest

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update -y && \
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    apt-get install -y tzdata && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    apt-get install unzip curl python3 python3-pip \
                    python3-dev libssl-dev \
                    virtualenv libpq-dev -y && \
    apt-get upgrade -y
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install nodejs -y
RUN pip install sphinx

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip3 install -r requirements.txt

EXPOSE 8081

ARG FOO
COPY . /opt/app

ENTRYPOINT [ "/opt/app/build.sh", "init-all-run" ]
