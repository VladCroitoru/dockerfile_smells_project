FROM debian:latest
MAINTAINER Henry Hoang <henry.hoang@j2.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq apt-utils
RUN DEBIAN_FRONTEND==noninteractive apt-get install -yq htop
RUN apt-get clean

CMD ["htop"]
CMD ["ls", "-l"]

WORKDIR /root
ENV DZ version1

#ADD run.sh /root/run.sh
#CMD ["./run.sh"]

#ENTRYPOINT ["./run.sh"]
#CMD ["arg1"]
