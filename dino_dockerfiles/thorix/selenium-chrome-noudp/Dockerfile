FROM selenium/standalone-chrome-debug

USER root

RUN apt-get update && apt-get install -y iptables

COPY iptables.blockudp.sh /

USER seluser

ENTRYPOINT ["/bin/bash"]
CMD ["/iptables.blockudp.sh"]

#CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

