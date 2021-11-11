FROM java:8-jdk-alpine

RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk upgrade --update-cache --available
RUN apk add --update python py-pip iproute2 jo wget supervisor bash bind-tools
ADD ape-cage /ape-cage
RUN wget --no-check-certificate https://github.com/msoap/shell2http/releases/download/1.10/shell2http-1.10.linux.386.tar.gz -O /tmp/shell2http.tar.gz
RUN tar -xvzf /tmp/shell2http.tar.gz -C /ape-cage/bin/ shell2http
RUN rm -f /tmp/shell2http.tar.gz
RUN wget http://central.maven.org/maven2/de/codecentric/spring-boot-admin-sample/1.2.4/spring-boot-admin-sample-1.2.4.jar -O /sample-app.jar
RUN pip install supervisor-logstash-notifier
RUN sed -i s/enp0s8/eth0/g /ape-cage/etc/*
ADD supervisor.d /etc/supervisor.d
ADD supervisord.conf /etc/supervisord.conf
ADD consul-cli /usr/bin/consul-cli
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
