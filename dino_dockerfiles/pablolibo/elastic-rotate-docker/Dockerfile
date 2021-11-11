FROM ubuntu:16.04
MAINTAINER Pablo J. Villarruel <pablolibo@gmail.com>

#Git: https://github.com/anabadce/rotate-elasticsearch-index
ADD https://raw.githubusercontent.com/anabadce/rotate-elasticsearch-index/master/rotate-elasticsearch-index.sh /bin/rotate.sh
RUN chmod +x /bin/rotate.sh
#Tool

RUN apt-get update && apt-get install curl -y
