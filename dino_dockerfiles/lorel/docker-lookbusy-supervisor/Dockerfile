FROM lorel/docker-lookbusy

MAINTAINER aurelien@derniercri.io

RUN apk add --update supervisor

ADD build_files/start.sh /home/start.sh

ENTRYPOINT ["/home/start.sh"]

CMD ["--help"]
