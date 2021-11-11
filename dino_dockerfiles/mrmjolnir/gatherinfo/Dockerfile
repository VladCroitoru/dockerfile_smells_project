# ficherin dockerfile de ejemplo
# --> docker build -t nacho/imagen:1.0 .
# cada RUN es un commit, mucha tela, mejor agregar los comandos

FROM centos:7
#RUN apt-get update && apt-get install -y vim curl openjdk-7-jdk
#RUN apt-get install vim
#CMD ["ping", "127.0.0.1", "-c", "30"]
#ENTRYPOINT ["ping"] # después le pasamos al comando docker run los parametros del ping y los ejecuta....
#VOLUME /ccv/app/slv3567v /ccv/data/slv3567v
# good for sharing data between containers

# los conatainers tienen ip y red privada.
#EXPOSE 80 443
#CMD ["nginx", "-g", "daemon off;"]
# linking containers: app.srv --> db.srv

COPY gatherinfo.sh .
CMD ["/bin/bash", "gatherinfo.sh"]

