FROM ubuntu:16.04

MAINTAINER Steve Mayne version: 0.1

RUN apt-get update && apt-get install -y python

EXPOSE 8000

RUN groupadd -r httpuser && useradd -r -g httpuser httpuser

RUN mkdir /webroot
ADD webfiles/ /webroot/
RUN chown -R httpuser:httpuser /webroot

WORKDIR /webroot
USER httpuser
CMD ["python", "-m", "SimpleHTTPServer"]
