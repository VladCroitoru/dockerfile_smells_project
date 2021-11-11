FROM psiag/oracle-java

MAINTAINER cubesky

ADD Server.tar /mcserver

EXPOSE 25565
EXPOSE 80

WORKDIR /mcserver/
VOLUME /mcserver/world
VOLUME /mcserver/nucleus
VOLUME /mcserver/mods
VOLUME /mcserver/config
CMD ["/usr/bin/java","-Xms7680M","-Xmx7680M","-jar","forge-1.10.2-12.18.3.2221-universal.jar","nogui"]