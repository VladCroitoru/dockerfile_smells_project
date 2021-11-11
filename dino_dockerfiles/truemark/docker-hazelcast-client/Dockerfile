FROM hazelcast/hazelcast:3.9.2

ADD client.sh /$HZ_HOME/client.sh
RUN chmod +x /$HZ_HOME/client.sh
CMD ["./client.sh"]
