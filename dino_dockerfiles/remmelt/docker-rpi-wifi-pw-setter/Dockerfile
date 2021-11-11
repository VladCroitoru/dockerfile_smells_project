FROM debian

MAINTAINER Remmelt Pit <remmelt@gmail.com>

VOLUME ["/images"]

ADD set_pw.sh /usr/local/bin/set_pw.sh

ENTRYPOINT ["set_pw.sh", "image.img"]
