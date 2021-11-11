FROM java:openjdk-7

MAINTAINER Jentsch <d.jentsch@fu-berlin.de>

RUN git clone https://jentsch@github.com/Jentsch/scaml-play-example.git /opt/scaml-play-example/

WORKDIR /opt/scaml-play-example/

# Download SBT, dependencies and typesafe activator
RUN ./activator scalaVersion compile
RUN ./activator -Dactivator.timeout=2s ui

EXPOSE 8888 9000

CMD ["./activator", "-Dactivator.timeout=8h", "-Dhttp.address=0.0.0.0", "ui"]

