FROM maven:3-jdk-8-slim
WORKDIR /usr/src/mymaven
RUN apt-get update && apt-get install -y locales locales-all
RUN locale-gen ru_RU && locale-gen ru_RU.UTF-8 && update-locale 
ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8
CMD mvn clean verify -e -s settings/settings.xml
