FROM node:latest

RUN apt-get update

WORKDIR /website

ADD simpleapp/ /website/simpleapp

# Hack to report vulnerabilities
# include ssl libraries that have vulnerabilities
COPY ./vulnerable-ssl-libs/*.* /usr/tempv/

EXPOSE 8888
CMD ["/usr/local/bin/node", "simpleapp/index.js"]

LABEL x="a"
