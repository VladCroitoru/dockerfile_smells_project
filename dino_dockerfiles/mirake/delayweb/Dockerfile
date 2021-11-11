FROM ubuntu:latest
MAINTAINER mirake mirake@docker.com

RUN apt-get update && \
    apt-get install -y vim curl wget python python-pip

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN mkdir -p /app

# Define working directory.
WORKDIR /app

# Expose ports.
EXPOSE 80

ADD run.sh  /run.sh
ADD server.py  /app/server.py
ADD alauda.jpg  /app/alauda.jpg
RUN chmod 755 /run.sh


# Define default command.
CMD ["/run.sh"]
