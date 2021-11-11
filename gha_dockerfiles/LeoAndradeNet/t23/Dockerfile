FROM alpine:3.12.0 as maven_builder
WORKDIR /app
ADD . /app
RUN apk add --no-cache --update-cache maven openjdk11 && mvn dependency:go-offline -B
ENV TIER DEV
ENV CONTEXT_USE true
# Sobre o valor TIER, veja https://docs.cronapp.io - Parâmetros para gerar .war
RUN mvn clean && mvn package -X -Dcronapp.profile=${TIER} -Dcronapp.useContext=${CONTEXT_USE}

FROM tomcat:9.0.17-jre11
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=maven_builder /app/target/*.war /usr/local/tomcat/webapps/ROOT.war