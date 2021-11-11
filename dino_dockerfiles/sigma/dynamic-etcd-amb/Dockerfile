FROM golang:1.2

RUN mkdir /opt/nsproxy
RUN git clone https://github.com/sigma/nsproxy.git /opt/nsproxy
RUN cd /opt/nsproxy && ./build

ADD proxy-amb.sh /usr/bin/proxy-amb.sh

ENTRYPOINT ["/usr/bin/proxy-amb.sh"]
