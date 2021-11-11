FROM ubuntu:16.04

MAINTAINER Bob Adolf <rdadolf@gmail.com>

RUN apt-get update && apt-get install -y \
  python \
  python-pip \
  git

RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt /tmp/
RUN pip install --upgrade -r /tmp/requirements.txt

# Install model dependencies
COPY models/*/*_requirements.txt /tmp/
RUN cat /tmp/*_requirements.txt > /tmp/modelrequirements.txt
RUN pip install --upgrade -r /tmp/modelrequirements.txt

# Add Dnnamo
ADD . /dnnamo
RUN chmod -R a+rw /dnnamo
