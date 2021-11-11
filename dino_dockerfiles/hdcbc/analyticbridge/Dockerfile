# Dockerfile for the HDC's Analytic Bridge service
#
#
# Example:
# sudo docker pull healthdatacoalition/analyticbridge
# sudo docker run -d --name=bridge -h bridge --restart=always healthdatacoalition/analyticbridge
#
#
FROM phusion/passenger-nodejs
MAINTAINER derek.roberts@gmail.com


# Prepare /app/ folder
#
WORKDIR /app/
COPY . .
RUN sed -i -e 's/localhost:27017/composerdb:27017/' lib/executions.js; \
    npm install


# Create startup script and make it executable
#
RUN ( \
      echo "#!/bin/bash"; \
      echo "#"; \
      echo "set -e -o nounset"; \
      echo ""; \
      echo ""; \
      echo "# Wait, then run app"; \
      echo "#"; \
      echo "sleep 10"; \
      echo "cd /app/"; \
      echo "node index.js"; \
    )  \
      >> /app/run; \
    chmod +x /app/run


# Run Command
#
CMD ["/app/run"]


# Volume for config
#
VOLUME /app/config/
VOLUME /app/scorecards/
