FROM openjdk:8-jre

# 1.12.2: current build
# b1618 December 27, 2019

ARG PAPER_URL=https://yivesmirror.com/files/paper/Paper-1.12.2-b1618.jar

WORKDIR /data
ADD "${PAPER_URL}" /srv/paper.jar
RUN cd /srv && \
    chmod 444 /srv/paper.jar

ADD runPaper.sh /usr/local/bin/paper
RUN chmod +x /usr/local/bin/paper

ENV JAVA_ARGS ""
ENV SPIGOT_ARGS ""
ENV PAPER_ARGS ""

VOLUME "/data"

CMD ["paper"]
