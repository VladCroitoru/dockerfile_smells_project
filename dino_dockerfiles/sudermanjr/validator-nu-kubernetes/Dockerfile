FROM openjdk:8

# Mostly inspired by: https://github.com/sitevalidator/validator-nu-docker/blob/master/Dockerfile

ADD https://github.com/validator/validator/releases/download/17.7.0/vnu.jar_17.7.0.zip /opt
RUN unzip -d /opt /opt/vnu.jar_17.7.0.zip

USER nobody
WORKDIR /opt/dist

CMD ["java", "-cp", "vnu.jar", "nu.validator.servlet.Main","8888"]
