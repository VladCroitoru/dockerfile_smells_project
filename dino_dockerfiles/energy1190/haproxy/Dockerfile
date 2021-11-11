FROM haproxy:1.7

ADD start.sh /start.sh
ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

RUN chmod +x /start.sh 
EXPOSE 3306 8080

ENTRYPOINT ["/start.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
