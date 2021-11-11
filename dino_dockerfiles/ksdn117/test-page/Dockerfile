FROM nginx:latest
MAINTAINER	ksdn117 <ksdn117@gmail.com>

RUN apt-get -y update
RUN apt-get install -y wget

RUN echo "<!DOCTYPE html> \
            <html lang="ja"> \
            <meta charset="utf-8"> \
            <title>Running!</title> \
	    <style type="text/css"> \
	    body { \
	    width: 100%; \
	    min-height: 100%; \
	    background: linear-gradient(to bottom,#fff 0,#b8edff 50%,#83dfff 100%); \
	    background-attachment: fixed; \
	    } \
	    </style> \
            </head> \
            <body> \
            <div align="center"> \
            <h1>Your container is running!</h1> \
            <img src="./docker.png" alt="docker logo"> \
            </div> \
            </body> \
            </html>" \
            > /usr/share/nginx/html/index.html

RUN wget https://d3oypxn00j2a10.cloudfront.net/0.15.4/img/homepage/docker-whale-home-logo.png -O /usr/share/nginx/html/docker.png
RUN chmod 644 /usr/share/nginx/html/index.html
RUN chmod 644 /usr/share/nginx/html/docker.png

EXPOSE 80 443
