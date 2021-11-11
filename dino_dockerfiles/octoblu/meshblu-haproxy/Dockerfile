FROM haproxy:1.6

EXPOSE 80
EXPOSE 1883

ADD run.sh .
ADD haproxy.cfg .
CMD ["./run.sh"]
