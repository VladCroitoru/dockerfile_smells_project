FROM cpswan/node-red:latest

MAINTAINER Oliver Lorenz <mail@oliverlorenz.com>

RUN npm install -g node-red-contrib-admin node-red-contrib-nmap node-red-contrib-ui
RUN apt-get update && apt-get install -y cron nmap

EXPOSE 1880

CMD ["/usr/local/bin/node-red"]
