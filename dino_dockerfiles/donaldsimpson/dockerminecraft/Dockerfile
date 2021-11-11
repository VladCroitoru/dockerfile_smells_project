FROM ubuntu

# install apt packages and update
RUN apt update
RUN apt install -y default-jre

###########


# EXPOSE ports
EXPOSE 25565 25575

# copy files over
RUN mkdir /minecraftserver
COPY server.jar /minecraftserver/
COPY server.properties /minecraftserver/
COPY eula.txt /minecraftserver/
COPY startminecraft.sh /minecraftserver/
# - minecraft server jar
# - startminecraft script
# - tini

# EXPOSE volume
VOLUME /minecraftserver

### Entry Point
# tini run startminecraft.sh

# Add Tini
ENV TINI_VERSION v0.10.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Run Minecraft script under Tini
CMD ["/minecraftserver/startminecraft.sh"]
