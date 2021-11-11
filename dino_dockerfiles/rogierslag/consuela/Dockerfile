FROM node:10.16.0
MAINTAINER Rogier Slag

RUN mkdir /opt/consuela

# Install dumb-init
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64.deb
RUN dpkg -i dumb-init_*.deb

# Set the exposed stuff
VOLUME /opt/consuela/config
EXPOSE 8543

# install dependencies
ADD package.json /opt/consuela/package.json
ADD yarn.lock /opt/consuela/yarn.lock
ADD .babelrc /opt/consuela/.babelrc
ADD .eslintrc /opt/consuela/.eslintrc
RUN cd /opt/consuela && yarn install

# Copy source
COPY src /opt/consuela/src/

WORKDIR /opt/consuela
# Build output
RUN yarn build

# Start it!
CMD ["dumb-init", "node", "out/server.js"]

