FROM vitalcode/events-model
MAINTAINER vitalcode

ADD . /data
WORKDIR /data
RUN sbt clean compile

EXPOSE 9000

ENTRYPOINT ["sbt"]
CMD ["run"]
