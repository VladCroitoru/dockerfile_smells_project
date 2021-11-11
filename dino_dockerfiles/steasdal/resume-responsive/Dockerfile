# Best practices for running nodejs in docker in production:
# https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md
# https://nodesource.com/blog/8-protips-to-start-killing-it-when-dockerizing-node-js/

FROM node:8.1.2
MAINTAINER Sam Teasdale

# Install Tini
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Switch to the node user so that we're not running nodejs as root.
USER node
RUN mkdir -p /home/node
WORKDIR /home/node

COPY package.json .
RUN npm install node-static && npm install

COPY app.js .
COPY /content ./content

EXPOSE 8080

# Start the server (with tini)
CMD ["node", "app.js"]
