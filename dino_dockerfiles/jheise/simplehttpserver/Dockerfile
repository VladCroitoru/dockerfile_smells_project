FROM ubuntu:14.04
RUN apt-get update
RUN apt-get -y install python
RUN mkdir /data
ENV DATADIR /data
ENV PORT 8080
EXPOSE ${PORT}
WORKDIR ${DATADIR}
CMD python -m SimpleHTTPServer ${PORT}
