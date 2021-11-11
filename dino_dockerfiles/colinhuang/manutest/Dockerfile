FROM manuchen/ubt-gcc
MAINTAINER Manu Chen

# need /mysrc be mounted as the source volume

RUN apt-get update && apt-get install -y make libssl-dev libhdhomerun-dev liburiparser-dev libdbus-1-dev && mkdir /root/Videos
ADD install /usr/local/bin/install
ADD install_quick /usr/local/bin/install_quick

CMD ["/mysrc/install.sh"]

