FROM node:wheezy

RUN apt-get update -y && apt-get install --no-install-recommends -y -q unzip
WORKDIR /app/openhybrid
ADD https://github.com/realityeditor/server/archive/master.zip /app/openhybrid/v1.7.0.zip
RUN unzip -u /app/openhybrid/v1.7.0.zip -d /app/openhybrid
RUN cd /app/openhybrid/server-master && npm install --no-optional
ADD https://github.com/JoeTalbot/objects/archive/master.zip /app/openhybrid/objects.zip
RUN unzip -u /app/openhybrid/objects.zip -d /app/openhybrid/
RUN rm -rf /app/openhybrid/server-master/objects
RUN mv /app/openhybrid/objects-master /app/openhybrid/server-master/objects

EXPOSE 8080
CMD ["npm", "start"]
ENTRYPOINT ["/usr/local/bin/node", "/app/openhybrid/server-master/server.js", "> server.log"]
