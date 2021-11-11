FROM    debian:stable
 
MAINTAINER MyName <me@wherever.com>
 
# Build dependencies
RUN apt-get -y update

# Install some common tools needed.
RUN apt-get install -y -q curl git-core apt-utils sudo libwww-perl vim htop wget
 
# Setup timezone, notice in this example, we 
# perform multiple operations within the same
# RUN by ending the lines with \, this ensures
# You create a single build step for this operation.
RUN \
  cp /usr/share/zoneinfo/America/Chicago /etc/localtime && \
  echo "America/Chicago" > /etc/timezone;
 
# Bash / sh link
RUN ln -sf /bin/bash /bin/sh;

# Say you want a file with predefines set,
# like for a file in /etc, you can do it like so.
RUN echo moo > /tmp/moo

# When the container is run, which directory do 
# you want it dropped into?
WORKDIR  /opt/
 
# Now we are going to set the command executed when 
# the container is run.
CMD ["/bin/bash"]
