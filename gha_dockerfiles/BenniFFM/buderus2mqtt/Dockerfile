FROM alpine:3.12.7

RUN apk upgrade --no-cache -U && apk add --no-cache curl nodejs npm yarn

RUN apk add --no-cache python3 build-base libmcrypt-dev

WORKDIR /root/app

# install node packages
RUN npm set progress=false && npm config set depth 0
RUN npm install mcrypt async buffertrim cli-table mqtt npm-check-updates request require-yaml yalm yargs --only=production

# copy app sources
COPY package.json .
COPY config.js .
COPY km200mqtt.js .
COPY scan.js .
VOLUME ["/data"]
CMD ./km200mqtt.js 
