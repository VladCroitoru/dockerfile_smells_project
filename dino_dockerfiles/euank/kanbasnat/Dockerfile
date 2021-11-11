FROM node:5
RUN wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64 && chmod +x /usr/bin/dumb-init
COPY ./index.js ./package.json ./LICENSE ./
RUN npm install && mkdir -p /var/lib/kanbasnat/
VOLUME /var/lib/kanbasnat/
ENTRYPOINT ["dumb-init", "node", "index.js"]
