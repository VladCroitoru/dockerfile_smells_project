FROM maven:3.6.3-jdk-8

RUN apt-get install git -y

RUN git clone https://github.com/CalculatorApps/Addition.git

WORKDIR Addition

RUN mvn -B clean install -DreleaseVersion=1.0

CMD ["java", "-jar", "target/Addition-1.0.0.jar"]
