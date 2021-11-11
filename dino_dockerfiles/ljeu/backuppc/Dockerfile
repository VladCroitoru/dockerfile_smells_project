FROM adferrand/backuppc:4.3.0-3

RUN apk update && apk upgrade && apk --no-cache --update add dcron

COPY /docker-cmd.sh /

CMD ["/docker-cmd.sh"]

