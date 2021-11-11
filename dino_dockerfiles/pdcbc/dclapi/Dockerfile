# Dockerfile for the PDC's DCLAPI service
#
#
# Drug Class Lookup API used by the PDC's Hub API (HAPI).
#
# Example:
# sudo docker pull pdcbc/dclapi
# sudo docker run -d --name=dclapi -h dclapi --restart=always pdcbc/dclapi
#
# External port (for testing)
# - DCLAPI: -p <hostPort>:3007
#
#
FROM phusion/passenger-nodejs
MAINTAINER derek.roberts@gmail.com


# Prepare /app/ folder
#
WORKDIR /app/
COPY . .
RUN chown -R app:app /app/; \
    /sbin/setuser app npm install


# Create startup script and make it executable
#
RUN mkdir -p /etc/service/app/; \
    ( \
      echo "#!/bin/bash"; \
      echo ""; \
      echo ""; \
      echo "# Start service"; \
      echo "#"; \
      echo "cd /app/"; \
      echo "exec /sbin/setuser app npm start"; \
    )  \
      >> /etc/service/app/run; \
    chmod +x /etc/service/app/run


# Run Command
#
CMD ["/sbin/my_init"]


# Ports and volumes
#
EXPOSE 3007
