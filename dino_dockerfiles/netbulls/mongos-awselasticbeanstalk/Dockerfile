FROM mongo:3.2

EXPOSE 27017
CMD ["/bin/bash", "-c", "mongos --configdb $CONFIG_SERVERS"]
