
FROM java:8

RUN curl -L https://services.gradle.org/distributions/gradle-4.1-bin.zip -o gradle-4.1-bin.zip
RUN apt-get install -y unzip
RUN unzip gradle-4.1-bin.zip

ENV GRADLE_HOME=/gradle-4.1
ENV PATH=$PATH:$GRADLE_HOME/bin

RUN ["gradle", "build"]

RUN echo $HOME

RUN echo $PATH

RUN echo $GRADLE_HOME

#docker build -t gradle

EXPOSE 8080

RUN mkdir -p /app/

#ADD /build/libs/sixth-block-demo.jar /app/sixth-block-demo.jar

ENTRYPOINT ["java", "-jar", "/app/sixth-block-demo.jar"]
