FROM ubuntu:latest

# Dependencies
RUN apt-get update
RUN apt-get -y install python2.7 ca-certificates git-core make xdg-utils gcc gdb

# Get hopper
RUN mkdir -p /opt/hopper-download
ADD getHopper.py /opt/hopper-download/getHopper.py
RUN python2.7 /opt/hopper-download/getHopper.py
RUN mkdir -p /usr/share/desktop-directories/
RUN apt-get -y install /opt/hopper-download/*.deb
RUN apt-get -y remove python2.7

# Add hopper user
RUN useradd hopper

WORKDIR /home/hopper
RUN mkdir /var/sharedFolder

RUN chown -R hopper:hopper /var/sharedFolder
RUN chown -R hopper:hopper /home/hopper/
USER hopper

ENTRYPOINT /opt/hopper-v4/bin/Hopper
