FROM haproxy:1.6.3

RUN mkdir /home/haproxy

WORKDIR /home/haproxy

ADD generateConfig.sh /home/haproxy/

RUN chmod +x /home/haproxy/generateConfig.sh

EXPOSE 80

CMD /home/haproxy/generateConfig.sh > /home/haproxy/haproxy.cfg  && cat /home/haproxy/haproxy.cfg && haproxy -d -f /home/haproxy/haproxy.cfg -c && haproxy -f /home/haproxy/haproxy.cfg -db
