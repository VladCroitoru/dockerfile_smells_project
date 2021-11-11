from debian:9

RUN apt update && apt upgrade -y && apt install -y
RUN apt install openjdk-8-jre -y

RUN apt install wget -y

RUN mkdir /workdir
WORKDIR /workdir

RUN wget --verbose \
https://oss.sonatype.org/content/repositories/snapshots/io/swagger/swagger-codegen-cli/3.0.0-SNAPSHOT/swagger-codegen-cli-3.0.0-20170727.135949-1.jar \
--output-document swagger-codegen-cli-3.jar

ENTRYPOINT ["java", \
"-jar", "swagger-codegen-cli-3.jar"]
#"-Dio.swagger.parser.util.RemoteUrl.trustAll=true"]

CMD ["help"]
