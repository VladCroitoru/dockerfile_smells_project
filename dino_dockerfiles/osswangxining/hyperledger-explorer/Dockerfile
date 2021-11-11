# Dockerfile for Hyperledger Explorer Docker Image
FROM node:6-wheezy
MAINTAINER Xi Ning Wang <osswangxining.github.com>

# install maintain tools
#RUN npm install bower grunt-cli graceful-fs@4.1.5 minimatch@3.0.2 -g

# clone latest code from github
RUN git clone --single-branch -b master --depth 1 https://github.com/osswangxining/blockchain-explorer.git

WORKDIR /blockchain-explorer

#RUN echo '{ "allow_root": true }' > .bowerrc

# Modify config.json to update the value of pg host, username, password details.
# If you are building your code for production
# RUN npm install --only=production
RUN npm install && cd client/ && npm install \
     && npm test -- -u --coverage && npm run build
#VOLUME /blockchain-explorer
EXPOSE 8080
CMD ["node", "main.js"]
