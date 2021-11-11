FROM google/python

RUN apt-get install wget
RUN wget -O - http://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN wget -O /etc/apt/sources.list.d/mopidy.list http://apt.mopidy.com/mopidy.list
RUN apt-get update || true
RUN apt-get install mopidy -yq --force-yes
