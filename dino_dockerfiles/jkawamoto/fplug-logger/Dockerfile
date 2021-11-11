#
# Dockerfile
#
# Copyright (c) 2015 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
#----------------------------------------------------------
# to run fplug-logger as a container
#
FROM ubuntu
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

# Install a dependent library.
RUN apt-get update && apt-get install -y git python-pip && \
    apt-get upgrade -y && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/
RUN pip install -U pip pip-tools

ADD ./requirements.in ./
RUN pip-compile && pip install -r requirements.txt && \
    rm requirements.in requirements.txt

# Change the working directory.
WORKDIR /root

# Import a dependent library from GitHub.
RUN git clone https://github.com/hasegaw/pyfplug.git
ENV PYTHONPATH pyfplug

# Add the main script.
ADD bin .

ENTRYPOINT ["./entrypoint.sh"]
