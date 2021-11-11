FROM ubuntu
MAINTAINER Kaha Team
LABEL Description="Image for kaha: quick relief lookup for nepal earthquake"

# install node
ADD http://nodejs.org/dist/v0.12.2/node-v0.12.2-linux-x64.tar.gz /tmp/
RUN cd /tmp && tar --strip-components 1 -xzf node-v0.12.2-linux-x64.tar.gz -C /usr/local

# copy the npm package file first and then install the modules, so that we cache it
ADD package.json /kaha/package.json
WORKDIR /kaha
RUN npm install

# now add the app source
ADD . /kaha

EXPOSE 3000

# provides remote db for quick setup
ENV NODE_ENV stage

#CMD ["npm", "start"]
CMD ["npm", "run", "build-dev-watch"]
