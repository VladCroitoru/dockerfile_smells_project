# To build and run with Docker:
#
#  $ docker build -t portal .
#  $ docker run -it --rm -p 3000:3000 -p 3001:3001 portal

FROM node:latest

RUN mkdir -p /portal /home/nodejs && \
    groupadd -r nodejs && \
    useradd -r -g nodejs -d /home/nodejs -s /sbin/nologin nodejs && \
    chown -R nodejs:nodejs /home/nodejs

WORKDIR /portal
COPY package.json typings.json /portal/
RUN npm install --unsafe-perm=true

COPY . /portal
RUN chown -R nodejs:nodejs /portal
USER nodejs

CMD npm start
