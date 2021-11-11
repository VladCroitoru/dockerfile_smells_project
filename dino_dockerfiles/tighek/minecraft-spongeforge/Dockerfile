#
# Dockerfile to build SpongeForge
#

FROM java:8
MAINTAINER Tighe Kuykendall, http://github.com/TigheK

RUN mkdir /srv/minecraft

ADD ./eula.txt /srv/
RUN cp /srv/eula.txt /srv/minecraft/

ADD ./start_sponge /srv/
RUN chmod 775 /srv/start_sponge
RUN cp /srv/start_sponge /srv/minecraft/

ADD https://repo.spongepowered.org/maven/org/spongepowered/spongeforge/1.12.2-2655-7.1.0-BETA-3070/spongeforge-1.12.2-2655-7.1.0-BETA-3070.jar /srv/spongeforge.jar
RUN ln -s /srv/spongevanilla.jar /srv/minecraft/spongevanilla.jar

RUN touch /srv/spongeforge_1.12.2-2655-7.1.0-BETA-3070

WORKDIR /srv/minecraft
VOLUME ["/srv/minecraft"]

EXPOSE 25565
EXPOSE 25565/udp

CMD [""]

ENTRYPOINT /srv/start_sponge 
