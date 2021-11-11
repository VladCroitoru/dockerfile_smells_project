FROM ubuntu:trusty

RUN apt-get update && apt-get install -y -qq wget unzip ant git openjdk-7-jdk && apt-get clean

RUN wget https://storage.googleapis.com/appengine-sdks/featured/appengine-java-sdk-1.9.24.zip && unzip appengine-java-sdk-1.9.24.zip && rm appengine-java-sdk-1.9.24.zip

WORKDIR appengine-java-sdk-1.9.24/demos/

RUN git clone https://github.com/google/firing-range

WORKDIR firing-range/

EXPOSE 8080 5050

CMD ["ant","-Daddress=0.0.0.0","runserver"]

