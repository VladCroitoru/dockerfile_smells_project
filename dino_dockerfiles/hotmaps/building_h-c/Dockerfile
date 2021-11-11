#
# hotmaps/toolbox-backend image Dockerfile
#
#

# docker container prune
# docker image prune
# http://192.168.99.100:9006/api/

FROM ubuntu:16.04

MAINTAINER Daniel Hunacek <daniel.hunacek@hevs.ch>

# setup volume 
RUN mkdir -p /data
VOLUME /data


# Build commands
RUN apt-get update && apt-get dist-upgrade -y && apt-get autoremove -y

# Install required softwarerequirements

RUN apt-get install -y \
	software-properties-common \
    wget\
    bzip2

RUN ln -sf /usr/bin/python3 /usr/bin/python

RUN apt-get install -y python3-pip

RUN ln -sf /usr/bin/pip3 /usr/bin/pip

RUN python --version
RUN python3 --version
RUN pip --version
RUN pip3 --version

# add gdal path for further pip install gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

## Sara: Try to install OSGEO (https://stackoverflow.com/questions/37294127/python-gdal-2-1-installation-on-ubuntu-16-04):
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
RUN apt-get update
RUN apt-get install -y gdal-bin python-gdal python3-gdal

# Setup app server
RUN mkdir -p /data
COPY gunicorn-config.py /data/gunicorn-config.py
RUN pip3 install gunicorn

# Install required python modules
COPY requirements.txt /data/requirements.txt
RUN pip3 install -r /data/requirements.txt

# Copy app source app
COPY app /data

WORKDIR /data

EXPOSE 80

# Start server
CMD ["gunicorn", "--config", "/data/gunicorn-config.py", "--log-config", "/data/logging.conf", "wsgi:application"]
