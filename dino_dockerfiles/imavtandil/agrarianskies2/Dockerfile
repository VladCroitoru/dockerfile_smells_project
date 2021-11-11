FROM alpine:3.3
RUN apk update
RUN apk --update add openjdk7-jre wget unzip


RUN     mkdir /server
RUN wget -q https://minecraft.curseforge.com/projects/agrarian-skies-2/files/2261980/download -O /server/pack.zip
RUN wget -q https://minecraft.curseforge.com/projects/agrarian-skies-2-official-maps/files/2234903/download -O /server/map.zip

RUN	cd /server && unzip pack.zip && rm pack.zip
RUN unzip map.zip && rm map.zip && mv "SMP Template" world
RUN echo "eula=true" > ./eula.txt
EXPOSE	25565
EXPOSE	8123
CMD java  -Xmx1024M -Xms1024M -jar ./minecraft_server.1.7.10.jar 
