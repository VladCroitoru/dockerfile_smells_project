FROM kawayu168/debian-kafka:stretch
#
#
#
MAINTAINER Haruki Yukawa

# Install packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install pubnub
ADD run.sh /run.sh
ADD pubnub-subscribe.py /pubnub-subscribe.py
RUN chmod +x /run.sh && \
    chmod ugo+rx /pubnub-subscribe.py

CMD ["/run.sh"]
