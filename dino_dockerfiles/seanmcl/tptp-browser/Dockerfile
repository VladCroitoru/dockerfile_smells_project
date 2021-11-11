FROM ubuntu:14.04

RUN apt-get -y update && apt-get -y install build-essential curl python
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
RUN apt-get install -y nodejs
RUN npm install -g http-server
RUN mkdir -p /opt/tptp-browser/public \
    && ln -s /opt/tptp /opt/tptp-browser/public/problems
# Just add package.json so we can avoid running the expensive 'npm install'
# on every file change.
ADD tptp-browser/package.json /opt/tptp-browser/package.json
WORKDIR /opt/tptp-browser
RUN npm install
EXPOSE 8080
# Now add all the files.
ADD tptp-browser /opt/tptp-browser
RUN npm run compile
CMD npm run serve
