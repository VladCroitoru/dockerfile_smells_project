#
# Ubuntu Dockerfile
#
# https://github.com/dockerfile/ubuntu
#
# Pull base image.
FROM ubuntu:14.04
# Install stuff
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential
RUN apt-get install -y software-properties-common
RUN apt-get install -y byobu curl git htop man unzip vim wget
RUN wget -O- http://neuro.debian.net/lists/trusty.de-m.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
RUN apt-get install -y gcc make cmake pkg-config python python-dev python-pip python-virtualenv libopencv-dev
RUN apt-get install -y libopenblas-dev python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose python-opencv
RUN apt-get install -y libfreetype6-dev libpng-dev
RUN apt-get install -y imagemagick graphicsmagick
RUN rm -rf /var/lib/apt/lists/*
# pip requirements
RUN pip install cv2
RUN pip install docopt
# Install Node.js
RUN wget -qO- https://deb.nodesource.com/setup_4.x | sudo bash -
RUN apt-get install -y nodejs
ADD . /app
# Set environment variables.
ENV HOME /root
# Define working directory.
WORKDIR /app
# Install app dependencies
RUN cd /app && npm install
# Note: ln -s /dev/null /dev/raw1394 is to prevent error on python's
#   cv2 during import: "libdc1394 error: Failed to initialize libdc1394"
#   So, if you want to run another command, just update your CMD to start
#   with this script, followed by whatever you want. (Not cute, but works)
RUN ln /dev/null /dev/raw1394
RUN sh -c 'ln -s /dev/null /dev/raw1394'; bash
# Link the sails binary to be able to use Sails CLI
RUN ln -s /app/node_modules/sails/bin/sails.js /bin/sails
# Expose Sails port
EXPOSE 1337
# Bring up sails app
RUN npm install
CMD ["/app/node_modules/sails/bin/sails.js", "lift"]