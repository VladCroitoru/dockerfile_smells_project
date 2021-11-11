FROM node:4-onbuild

EXPOSE 8080 10000-20000

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64 \
 && chmod +x /usr/local/bin/dumb-init

CMD ["/usr/local/bin/dumb-init", "./bin/index.js"]
