FROM nginx:1.10-alpine
MAINTAINER Shane Osbourne "shane.osbourne8@gmail.com"

COPY start.sh /
COPY nginx.conf /etc/nginx/
COPY nginx-secure.conf /etc/nginx/

COPY dhparams.pem /etc/ssl/private/
CMD /start.sh
