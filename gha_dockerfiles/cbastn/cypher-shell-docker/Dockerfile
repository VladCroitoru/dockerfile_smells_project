# Container image that runs your code
FROM ubuntu:20.04
#update apt
RUN apt-get update -y
#install curl
RUN apt install curl -y
#install jdk 
RUN apt install openjdk-17-jre-headless -y
#curl cypher-shell 
RUN curl --url https://dist.neo4j.org/cypher-shell/cypher-shell_4.3.0_all.deb --output /tmp/cypher-shell.deb
#install cypher-shell
RUN dpkg -i /tmp/cypher-shell.deb

EXPOSE 7687

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]