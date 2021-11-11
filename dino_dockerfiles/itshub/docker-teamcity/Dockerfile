FROM ubuntu:16.04

ENV TEAM_CITY_VERSION 2017.2
ENV TEAMCITY_DATA_PATH /opt/teamcity-data
ENV JDBC_NAME postgresql-9.3-1102.jdbc41.jar

RUN apt-get update
RUN apt-get install -y wget default-jre
RUN mkdir /opt/teamcity
RUN wget -q -O - https://download-cf.jetbrains.com/teamcity/TeamCity-$TEAM_CITY_VERSION.tar.gz | tar xzf - -C /opt/teamcity
RUN wget -q http://jdbc.postgresql.org/download/$JDBC_NAME -P /tmp

ADD run.sh /run.sh
RUN chmod +x /run.sh

VOLUME ["/opt/teamcity-data"]
EXPOSE 8111
CMD /run.sh
