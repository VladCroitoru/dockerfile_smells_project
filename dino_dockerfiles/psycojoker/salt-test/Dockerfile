FROM psycojoker/base
MAINTAINER Laurent Peuch "cortex@worlddomination.be"

RUN apt-get install -y python-software-properties
RUN add-apt-repository -y ppa:saltstack/salt

RUN apt-get update
RUN apt-get install -y salt-minion
RUN apt-get install -y python-pip
RUN apt-get install -y git
RUN pip install git+https://github.com/Psycojoker/cellar.git

RUN mkdir /srv/salt -p
RUN mkdir /srv/pillar -p
