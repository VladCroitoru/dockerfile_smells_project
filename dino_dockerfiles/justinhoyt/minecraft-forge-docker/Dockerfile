# docker run -d -p 25565:25565 -t minecraft-forge-docker
FROM library/java:latest
RUN mkdir /mc
RUN mkdir -p /mc/mods
WORKDIR /mc
ADD \
  banned-ips.json \
  banned-players.json \
  config \
  docker-compose.yml \
  eula.txt \
  forge-1.12.1-14.22.1.2478-installer.jar \
  forge-1.12.1-14.22.1.2478-installer.jar.log \
  forge-1.12.1-14.22.1.2478-universal.jar \
  libraries \
  local \
  logs \
  minecraft_server.1.12.1.jar \
  mods \
  ops.json \
  server.properties \
  usercache.json \
  usernamecache.json \
  whitelist.json \
  ./

ADD mods/* /mc/mods/

EXPOSE 25565
RUN ["java", "-jar", "forge-1.12.1-14.22.1.2478-installer.jar","-installServer"]
RUN ["rm","forge-1.12.1-14.22.1.2478-installer.jar"]
RUN ["rm","forge-1.12.1-14.22.1.2478-installer.jar.log"]

CMD ["java", "-jar", "forge-1.12.1-14.22.1.2478-universal.jar","nogui"]
