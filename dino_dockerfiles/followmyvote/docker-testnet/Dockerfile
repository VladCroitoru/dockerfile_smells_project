FROM followmyvote/docker-graphene
MAINTAINER Nathan Hourt <nathan@followmyvote.com>

ADD build.sh .
RUN ./build.sh

ADD skeleton.tar /var/
EXPOSE 8080 8090 9001 17073 37073
VOLUME /var/fmv/backend_data /var/fmv/witness_data /var/fmv/supervisor
ENTRYPOINT ["supervisord", "-c", "/var/fmv/supervisor/supervisord.conf"]
