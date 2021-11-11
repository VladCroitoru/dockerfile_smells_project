FROM java:8

MAINTAINER XiNGRZ <xxx@oxo.ooo>

# Version of Minecraft Server
ENV VERSION latest

COPY install.sh /install
COPY launch.sh /launch

COPY server.properties /server.properties

RUN /install

RUN mkdir /data
VOLUME ["/data"]
WORKDIR /data

EXPOSE 25565

CMD [ "/launch" ]
