# shadowsocks-net-speeder

FROM ubuntu:14.04.3
MAINTAINER lowid <lowid@outlook.com>
RUN apt-get update && \
    apt-get install -y python-pip libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev git swaks jq curl
#RUN curl -SLk http://www.jetmore.org/john/code/swaks/files/swaks-20130209.0/swaks -o swaks \
#    && chmod +x swaks \
#    && mv swaks /usr/bin
RUN pip install shadowsocks==2.8.2

RUN git clone https://github.com/snooda/net-speeder.git net-speeder
WORKDIR net-speeder
RUN sh build.sh

RUN mv net_speeder /usr/local/bin/
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/net_speeder

#RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
#RUN apt-get install -y nodejs
# Configure container to run as an executable
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
