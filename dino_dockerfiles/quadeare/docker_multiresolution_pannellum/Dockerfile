FROM phusion/baseimage:0.9.18
MAINTAINER LACRAMPE Florian <lacrampe.florian@gmail.com>

# UTF-8 Environment
ENV LC_ALL C.UTF-8

# Install dependencies
RUN apt-get update
RUN apt-get install -y python-dev python-setuptools
RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
RUN apt-get install -y hugin

# Clean apt-get
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Pillow
RUN easy_install pip
RUN pip install pillow

# Add python script
ADD ./generate.py /opt/generate.py
RUN mkdir -p /opt/output

WORKDIR /opt/output

ENTRYPOINT ["python", "/opt/generate.py", "-n", "/usr/bin/nona"]
