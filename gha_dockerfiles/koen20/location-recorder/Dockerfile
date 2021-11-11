FROM openjdk:8-jre-alpine

RUN mkdir /recorder
WORKDIR /recorder
RUN wget https://github.com/koen20/location-recorder-recorder/releases/download/V1.0/location-recorder-1.0.zip
RUN unzip location-recorder-1.0.zip
CMD /recorder/location-recorder-1.0/bin/location-recorder
