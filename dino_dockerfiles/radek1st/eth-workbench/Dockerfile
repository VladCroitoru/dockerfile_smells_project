FROM node:alpine
RUN apk add -t .gyp --no-cache git python g++ make nano curl
RUN npm install -g truffle solc truffle-config truffle-expect ethereumjs-testrpc
RUN git config --global url."https://github.com/".insteadOf git@github.com: 
RUN git config --global url."https://".insteadOf git://
RUN mkdir -p /code
VOLUME /code
WORKDIR /code
CMD sh
