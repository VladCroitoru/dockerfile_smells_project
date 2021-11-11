# A basic web server. To use either add or bind mount content under /var/www
FROM ubuntu:16.04

MAINTAINER Steve Mayne version: 0.1

RUN apt-get update && apt-get install -y python

EXPOSE 8000

RUN groupadd -r httpuser && useradd -r -g httpuser httpuser

RUN mkdir /webroot
ADD index.html /webroot/index.html
RUN chown -R httpuser:httpuser /webroot

WORKDIR /webroot
USER httpuser
CMD ["python","-m","SimpleHTTPServer"]
