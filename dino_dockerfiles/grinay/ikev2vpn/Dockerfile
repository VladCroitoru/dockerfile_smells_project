FROM debian:latest
MAINTAINER grinay@demoupwork.com

RUN apt-get update && apt-get install -y strongswan curl kmod 

ADD ipsec.conf /etc/
ADD ipsec.secrets /etc/
ADD checkconn.sh /root
RUN chmod +x /root/checkconn.sh

ENTRYPOINT ["/bin/bash","./root/checkconn.sh"]
