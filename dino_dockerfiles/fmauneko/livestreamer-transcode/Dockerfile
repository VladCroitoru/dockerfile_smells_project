FROM ubuntu:xenial
MAINTAINER Florian Maunier fmauneko@dissidence.ovh

EXPOSE 8080

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y livestreamer vlc-nox

COPY . /app/
WORKDIR /app/

RUN useradd livestreamer && echo "livestreamer:livestreamer" | chpasswd
RUN chown -R livestreamer:livestreamer /app
USER livestreamer

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["help"]
