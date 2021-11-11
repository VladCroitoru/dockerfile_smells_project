FROM  node:alpine
MAINTAINER cowpanda<ynw506@gmail.com>
RUN npm install -g pm2@latest

COPY pm2_init /pm2_init
RUN chmod 755 /pm2_init
VOLUME ["/app"]
EXPOSE 80
EXPOSE 443

CMD ["/pm2_init"]
