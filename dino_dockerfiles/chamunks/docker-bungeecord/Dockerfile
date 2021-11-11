## Initial Dockerfile for Cubedcon 2015's Bungeecord
FROM java:8-jdk
MAINTAINER Oliver and Chamunks [chamunks@gmail.com] [oliversomething@gmail.com]

ADD config.yml /app/config.yml
ADD http://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar /app/BungeeCord.jar
ADD http://mcping.net/api/build.cubedcon.com/favicon.png /app/server-icon.png
EXPOSE 25565

WORKDIR /app/
CMD ["java", "-Xmx2G", "-Xincgc", "-jar", "BungeeCord.jar"]
