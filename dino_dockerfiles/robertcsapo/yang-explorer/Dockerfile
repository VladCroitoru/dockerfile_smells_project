FROM python:2
MAINTAINER Robert (robert@nigma.org)

RUN DEBIAN_FRONTEND=noninteractive git clone https://github.com/robertcsapo/yang-explorer.git

WORKDIR /yang-explorer/
RUN bash setup.sh -y
CMD bash start.sh
