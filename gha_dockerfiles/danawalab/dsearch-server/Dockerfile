FROM openjdk:8

ENV TZ=Asia/Seoul

RUN apt-get update -y
RUN apt-get install rsync -y
WORKDIR /data
WORKDIR /data/indexFile

WORKDIR /app

#COPY target/dsearch-server-1.2.0.jar dsearch-server.jar
#COPY lib/elastic-apm-agent.jar elastic-apm-agent.jar

# 클라우드
#CMD ["/bin/bash", "-c", "java -javaagent:elastic-apm-agent.jar -Delastic.apm.service_name=dsearch-server-local-docker -Delastic.apm.server_urls=https://358e572549c745de9727eec8ca7d309d.apm.eastus2.azure.elastic-cloud.com:443 -Delastic.apm.verify_server_cert=false -Delastic.apm.secret_token=WBuuvwbepWaB0sfgqs -Delastic.apm.environment=production -jar dsearch-server.jar"]

# 로컬
#CMD ["/bin/bash", "-c", "java -javaagent:elastic-apm-agent.jar -Delastic.apm.service_name=dsearch-server-local -Delastic.apm.application_packages=com.danawa -Delastic.apm.secret_token=WBuuvwbepWaB0sfgqs -Delastic.apm.server_url=https://proto-type.apm.eastus2.azure.elastic-cloud.com -jar dsearch-server.jar"]

# 도커 실행 커맨드
# docker build -t server .
# docker run -d -p 8080:8080 --name server server
# docker stop server ; docker rm server
# docker logs -f server