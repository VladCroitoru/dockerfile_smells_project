FROM python:2.7

# Pull code from Github
RUN cd $HOME

# Get SDK from Aldebaran
RUN wget https://community-static.aldebaran.com/resources/2.5.5/sdk-python/pynaoqi-python2.7-2.5.5.5-linux64.tar.gz

# Extract file
RUN tar -xvzf pynaoqi-python2.7-2.5.5.5-linux64.tar.gz && rm -R pynaoqi-python2.7-2.5.5.5-linux64.tar.gz

# Set environment variable
ENV PYTHONPATH=${PYTHONPATH}:/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages

# Install vim
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]