FROM iojs:slim

# Bundle app source
COPY index.js /app/index.js
COPY package.json /app/package.json

RUN cd /app; npm install

ENV NODE_PORT 8080

EXPOSE 8080

ENTRYPOINT ["node", "/app/index.js"]