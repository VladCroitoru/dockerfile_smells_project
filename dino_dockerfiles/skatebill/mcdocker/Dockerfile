FROM tomcat

WORKDIR /app

ADD ./data/ /app
#RUN rm /etc/apt/sources.list
#RUN cp /app/sources.list /etc/apt
#RUN apt-get update && apt-get install apache2

# Make port 80 available to the world outside this container
EXPOSE 8080
EXPOSE 25565
#/usr/local/tomcat/webapps/ROOT

#RUN rm -rf /usr/local/tomcat/webapps/ROOT
#RUN mkdir /usr/local/tomcat/webapps/ROOT
#RUN tar cf client.tar .minecraft HMCL-2.7.8.42.jar
#RUN mv client.tar /usr/local/tomcat/webapps/ROOT/
#RUN rm -rf .minecraft
#RUN rm HMCL-2.7.8.42.jar
#RUN tar xf mcserver.tar
#RUN chmod +x run.sh
RUN bash build_nomods.sh
CMD ["bash","run.sh"]