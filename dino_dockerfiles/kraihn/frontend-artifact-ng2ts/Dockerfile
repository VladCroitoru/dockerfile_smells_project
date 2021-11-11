FROM node:argon
MAINTAINER Jared Dickson <code@jareddickson.com>

# Update npm to 3.x latest and then install Angular CLI and Typings
RUN npm install -g npm@3 \
  && npm install -g angular-cli typings \
  && npm cache clean

CMD ["bash"]
