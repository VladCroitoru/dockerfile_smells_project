FROM alpine
LABEL maintainer="SameDocker"
WORKDIR /working_directory

RUN echo "syncthing:x:1000:1000::/home/syncthing:/sbin/nologin" >> /etc/passwd
RUN echo "syncthing:!::0:::::" >> /etc/shadow
RUN mkdir /home/syncthing
RUN chown syncthing /home/syncthing
RUN apk add --no-cache syncthing ca-certificates

USER syncthing
ENTRYPOINT ["syncthing", "-home", "/home/syncthing/config", "-gui-address", "0.0.0.0:8384"]

EXPOSE 8384
EXPOSE 22000
EXPOSE 22020