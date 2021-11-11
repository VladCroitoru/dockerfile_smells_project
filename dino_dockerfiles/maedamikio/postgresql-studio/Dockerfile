FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    unzip \
    wget \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN wget http://downloads.postgresqlstudio.org/2.0/pgstudio_2.0-bin.zip
RUN unzip pgstudio_2.0-bin.zip

EXPOSE 8080

CMD /pgstudio_2.0-bin/bin/startup.sh && tail -f /dev/null
