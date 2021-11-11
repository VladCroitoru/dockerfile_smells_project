# Dockerfile for the PDC's Visualizer service
#
#
# Visualizer for PDC-collected aggregate data. Link to Auth and HAPI.
#
# Example:
# sudo docker pull pdcbc/viz
# sudo docker run -d  --name=viz -h viz --restart=always \
#   --link auth:auth \
#   --link hapi:hapi \
#    -p 443:3004 \
#    -p 80:3008 \
#    pdcbc/viz
#
# Linked containers
# - Auth:           --link auth:auth
# - HAPI:           --link hapi:hapi
#
# External ports
# - https:          -p <hostPort(443)>:3004
# - http:           -p <hostPort(80)>:3008
#
# Modify default settings
# - Node secret:    -e NODE_SECRET=<string>
# - Reject non-CA
#    certificates?: -e REJECT_NONCA_CERTS=<0/1>
#
#
FROM phusion/passenger-nodejs
MAINTAINER derek.roberts@gmail.com


# Packages
#
RUN apt-get update; \
    apt-get install -y \
      python2.7; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Prepare /app/ folder
#
WORKDIR /app/
COPY . .
RUN chown -R app:app /app/; \
    /sbin/setuser app npm config set python /usr/bin/python2.7; \
    /sbin/setuser app npm install


# Create startup script and make it executable
#
RUN mkdir -p /etc/service/app/; \
    ( \
      echo "#!/bin/bash"; \
      echo "#"; \
      echo "set -e -o nounset"; \
      echo ""; \
      echo ""; \
      echo "# Environment variables"; \
      echo "#"; \
      echo "export PORT=\${PORT_VIZ:-3004}"; \
      echo "export PORT_VIZ_HTTP=\${PORT_VIZ:-3008}"; \
      echo "export AUTH_MAIN_URL=https://auth:\${PORT_AUTH_M:-3005}"; \
      echo "export AUTH_CONTROL_URL=https://auth:\${PORT_AUTH_C:-3006}"; \
      echo "export CALLBACK_URL=https://auth:\${PORT_AUTH_C:-3006}/auth/callback"; \
      echo "export HUBAPI_URL=https://hapi:\${PORT_HAPI:-3003}"; \
      echo "export NODE_TLS_REJECT_UNAUTHORIZED=\${REJECT_NONCA_CERTS:-0}"; \
      echo "export SECRET=\${NODE_SECRET:-notVerySecret}"; \
      echo "#"; \
      echo "export MODE=PROD"; \
      echo "export DACS=/etc/dacs"; \
      echo ""; \
      echo ""; \
      echo "# Start service"; \
      echo "#"; \
      echo "cd /app/"; \
      echo "/sbin/setuser app npm start"; \
    )  \
      >> /etc/service/app/run; \
    chmod +x /etc/service/app/run


# Run Command
#
CMD ["/sbin/my_init"]


# Ports and volumes
#
EXPOSE 3004
EXPOSE 3008
