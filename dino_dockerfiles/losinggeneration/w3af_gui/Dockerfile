FROM ubuntu:trusty
MAINTAINER Harley Laue <losinggeneration@gmail.com>

# Some environment variables to make things nicer
ENV USER w3af
ENV HOME /home/$USER

# We need the local apt database up-to-date
RUN apt-get update -y

# Generally needed packages
RUN apt-get install -y python-dev git python-lxml python-pip

# Setup a user to run w3af
RUN useradd -m $USER
USER $USER
WORKDIR $HOME

# Get w3af
RUN git clone --depth 1 https://github.com/andresriancho/w3af.git
WORKDIR $HOME/w3af
# We expect w3af_gui to fail as it builds the required dependencies
RUN ./w3af_gui; true

# Instal the dependencies
USER root
RUN sed 's/sudo apt-get/apt-get -y/g' -i /tmp/w3af_dependency_install.sh
RUN /tmp/w3af_dependency_install.sh

