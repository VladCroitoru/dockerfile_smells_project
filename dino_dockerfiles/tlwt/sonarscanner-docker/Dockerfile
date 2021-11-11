FROM openjdk:8

LABEL maintainer="Till Witt <mail@tillwitt.de"
#https://github.com/newtmitch/docker-sonar-scanner

RUN apt-get update
RUN apt-get install -y curl git tmux htop maven

# Set timezone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /root

RUN curl --insecure -o ./sonarscanner.zip -L https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip
RUN unzip sonarscanner.zip
RUN rm sonarscanner.zip

ENV SONAR_RUNNER_HOME=/root/sonar-scanner-3.0.3.778-linux
ENV PATH $PATH:/root/sonar-scanner-3.0.3.778-linux/bin

CMD sonar-scanner -Dsonar.host.url=${SONARHOST} -Dsonar.projectBaseDir=${SONARPROJECTBASEDIR}  -Dsonar.projectKey=${SONARPROJECTKEY}  -Dsonar.projectName=${SONARPROJECTNAME} -Dsonar.projectVersion=${SONARPROJECTVERSION}  -Dsonar.sources=${SONARSOURCES}
