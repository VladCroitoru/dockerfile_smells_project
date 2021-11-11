FROM ubuntu:14.04

MAINTAINER Allan Costa "allaninocencio@yahoo.com.br"

# Install Docker
RUN apt-get update
RUN apt-get install -y docker.io
RUN ln -sf /usr/bin/docker.io /usr/local/bin/docker
RUN sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io

# Add source code to container
ADD . /usr/local/src/gantryd/

# Install system dependencies
RUN cat /usr/local/src/gantryd/requirements.system | xargs sudo apt-get install -y

# Install python dependencies
RUN pip install -r /usr/local/src/gantryd/requirements.txt

# Add gantryd dir to path
ENV PATH $PATH:/usr/local/src/gantryd/

# Set working dir
WORKDIR /usr/local/src/gantryd/

CMD ["./gantry_server.py"]