FROM certbot/certbot:latest
WORKDIR /root
RUN apk add --update nodejs
COPY package.json /root/
RUN npm install
COPY auth.js /root/
COPY auth.sh /root/
COPY renew.sh /root/
COPY cleanup.js /root/
RUN mkdir -p /etc/certs
ENTRYPOINT ["sh"]
CMD ["renew.sh"]
