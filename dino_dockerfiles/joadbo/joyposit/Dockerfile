FROM node:0.12-slim
MAINTAINER Joy Borsutzki

#------
# Umgebungsvariablen
#ENV HUBOT_NAME NTTBOT
#ENV HUBOT_SLACK_TOKEN false
#ENV HUBOT_AUTH_ADMIN myself

#------
# Pre-Install
#RUN useradd -m -g hubot hubot
WORKDIR /opt
ADD /build /opt
#USER hubot
#WORKDIR opt/
RUN echo ["HUBOT START"]


#-----
# Install
RUN npm install --production
#RUN npm install coffee-script --production

#-----
# Post-install
EXPOSE 8080
<<<<<<< HEAD
VOLUME /opt/scripts
CMD ["/opt/bin/hubot", "--name", "Doerte"]

=======
VOLUME /scripts/
RUN echo ["HUBOT BOOT"]
CMD ["/opt/bin/hubot"]
#ENTRYPOINT ["bin/hubot", "--adapter shell"]
>>>>>>> betterscript
