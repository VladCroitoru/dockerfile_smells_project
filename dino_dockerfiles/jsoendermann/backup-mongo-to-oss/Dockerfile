FROM mongo:latest
LABEL maintainer="Jan Soendermann <jan.soendermann+git@gmail.com>"

RUN apt-get update && \
  apt-get install -y cron curl bzip2 file openssl && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /scripts

ADD backup.sh .
ADD entrypoint.sh .
RUN chmod +x ./*

VOLUME /tmp-dir

ENTRYPOINT [ "./entrypoint.sh" ]
