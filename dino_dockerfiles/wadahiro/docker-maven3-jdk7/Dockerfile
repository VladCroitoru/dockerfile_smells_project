FROM maven:3.3.9-jdk-7

RUN apt-get update && apt-get install -y zip patch && rm -rf /var/lib/apt/lists/*

CMD [ "mvn" ]