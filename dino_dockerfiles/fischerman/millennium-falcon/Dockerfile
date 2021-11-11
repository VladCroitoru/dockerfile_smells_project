FROM haproxy:1.6.4-alpine
RUN apk --update add nodejs curl letsencrypt
RUN touch /haproxy.cfg && mkdir /certs && mkdir /routes && openssl req -x509 -newkey rsa:2048 -keyout /tmp/key.pem -out /tmp/cert.pem -days 1000 -nodes -subj "/C=DE/ST=Any/L=Any/O=OrgName/OU=IT Department/CN=example.com" && cat /tmp/cert.pem /tmp/key.pem > /certs/combined.pem
ADD src/package.json /src/
WORKDIR /src/
RUN npm install
ADD src/ /src/
CMD ["node", "/src/main.js"]