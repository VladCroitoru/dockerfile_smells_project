FROM openjdk:alpine

ENV SBT_VERSION=0.13.8
ENV SBT_HOME=/usr/local/bin/sbt
ENV PATH=${PATH}:${SBT_HOME}/bin

RUN apk update
RUN apk add --quiet --no-cache bash ca-certificates
RUN apk update ca-certificates
RUN apk add openssl
RUN wget -O sbt-${SBT_VERSION}.zip -q "https://bintray.com/sbt/native-packages/download_file?file_path=sbt%2F${SBT_VERSION}%2Fsbt-${SBT_VERSION}.zip"
RUN unzip -qq sbt-${SBT_VERSION}.zip
RUN cp -rf sbt/* /usr/local
RUN rm -rf sbt
RUN echo -ne "- with sbt ${SBT_VERSION}\n" >> /root/.built

RUN sbt update
RUN sbt about

CMD echo 'DONE!'

