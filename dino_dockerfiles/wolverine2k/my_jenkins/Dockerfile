FROM jenkins:2.7.1
MAINTAINER Naresh Mehta <naresh.mehta@gmail.com>

# Install python-setuptools, python-dev and build-essential
USER root
RUN apt-get update && apt-get install -y python-setuptools python-dev build-essential

# Make sure we install pip as well for future use
RUN easy_install pip

# Install some more python modules that we generally need
RUN python -m pip install pymongo pygerrit

# drop back to the regular jenkins user - good practice
USER jenkins
