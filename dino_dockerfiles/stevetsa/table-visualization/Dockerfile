FROM ubuntu:latest
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>
RUN apt-get update

RUN apt-get install --yes \
build-essential \
git-all \
python \
python-dev \
python-distribute \
python-pip \
wget

ENV SRC /opt
COPY Dockerfile /opt/Dockerfile

WORKDIR $SRC
RUN git clone https://github.com/stevetsa/table-visualization
WORKDIR table-visualization

RUN pip install -r requirements.txt
# Expose ports
EXPOSE 8000

RUN apt-get install -y nano

# Set the default command to execute
CMD ["python", "wsgi.py"]


