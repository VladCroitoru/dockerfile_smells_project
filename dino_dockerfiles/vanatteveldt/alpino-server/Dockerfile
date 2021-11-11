FROM rugcompling/alpino:latest
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)
EXPOSE 5002

RUN apt-get -qq update && apt-get install -y python3-flask python3-pip python3-lxml openjdk-8-jdk maven git

# Build NERC
RUN git clone https://github.com/ixa-ehu/ixa-pipe-nerc --branch 1.5.4 && (cd ixa-pipe-nerc && mvn clean package)

# Get and unpack NERC models
RUN curl http://i.amcat.nl/nerc-models-1.5.4-nl.tgz | tar xz
RUN pip3 install alpinonaf>=0.4  git+https://github.com/antske/coref_draft.git

ENV NERC_MODEL=nerc-models-1.5.4/nl/nl-6-class-clusters-sonar.bin NERC_JAR=ixa-pipe-nerc/target/ixa-pipe-nerc-1.5.4.jar

COPY alpinoserver.py .

CMD python3 alpinoserver.py --host 0.0.0.0 --port 5002 --debug
