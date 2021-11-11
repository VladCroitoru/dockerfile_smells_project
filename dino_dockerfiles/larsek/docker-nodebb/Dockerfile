# The base image is the latest 4.x node (LTS) on jessie (debian)
# -onbuild will install the node dependencies found in the project package.json
# and copy its content in /usr/src/app, its WORKDIR
FROM node:4.2
ENV NODE_ENV production

EXPOSE 4567

RUN mkdir /src
RUN git clone https://github.com/NodeBB/NodeBB.git /src
WORKDIR /src

RUN npm install --yes --production
RUN node app --setup
CMD node app.js