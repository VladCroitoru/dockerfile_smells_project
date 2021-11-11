FROM java

MAINTAINER Alexander Ilyin <alexander@ilyin.eu>

# TEAMCITY INTERNAL ENVIRONMENT VARIABLES
ENV TEAMCITY_DATA_PATH /root/.BuildServer
ENV TEAMCITY_SERVER_MEM_OPTS -Xmx750m -XX:MaxPermSize=270m
ENV TEAMCITY_SERVER_OPTS -Dteamcity.git.fetch.separate.process=false

# TEMPORARY ENVIRONMENT VARIABLES
ENV VERSION 9.1.6

VOLUME ${TEAMCITY_DATA_PATH}
EXPOSE 8111

RUN curl -LSs http://download.jetbrains.com/teamcity/TeamCity-${VERSION}.tar.gz | tar xzv -C /opt/

WORKDIR /opt/TeamCity/bin

ENTRYPOINT ["./teamcity-server.sh"]

CMD  ["run"]
