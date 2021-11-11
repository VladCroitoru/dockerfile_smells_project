#
# Python3/bottle web server Dockerfile
#
# This image demonstrates how to set up a Python3/bottle web application using
# the base image pablosan/bottle-py3 as a starting point.
#
# https://github.com/Pablosan/hello-bottlepy
#

# Pull base image
FROM pablosan/bottle-py3

# Install the app
ADD hello-bottlepy /opt/hello-bottlepy
ADD requirements.txt /opt/config/

# Install python packages
RUN pip3 install -r /opt/config/requirements.txt

# Expose ports
EXPOSE 80

# Define default command
ENTRYPOINT /usr/bin/python3 /opt/hello-bottlepy/server.py
