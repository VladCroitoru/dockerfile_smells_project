FROM node:6

RUN npm install -g npm-proxy-cache@">=0.4.2 <1.0.0"

EXPOSE 8080

CMD ["npm-proxy-cache", "-h", "0.0.0.0", "-t", "86400", "-f"]
