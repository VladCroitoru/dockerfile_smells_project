FROM anapsix/alpine-java:8_server-jre
COPY "./" "/home/mct1-server"
VOLUME ["/home/mct1-server/plugins"]
EXPOSE 25565
WORKDIR /home/mct1-server
ENTRYPOINT ["java", "-Xmx1G", "-Xms1G", "-jar", "paperclip.jar"]

