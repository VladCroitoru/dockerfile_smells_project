FROM java:8-alpine


WORKDIR /data
ADD "https://github.com/OwnageTechGeek/docker-paper/raw/master/spigot.jar" /srv/paper.jar
RUN cd /srv &&\
	java -jar paper.jar --version &&\
	chmod 444 /srv/paper.jar

ADD start.sh /usr/local/bin/paper
RUN chmod +x /usr/local/bin/paper

ENV JAVA_ARGS "-Xmx1G"
ENV SPIGOT_ARGS ""
ENV PAPER_ARGS ""

VOLUME "/data"

CMD ["paper"]
