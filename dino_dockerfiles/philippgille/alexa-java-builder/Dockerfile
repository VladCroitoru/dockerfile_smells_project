FROM maven:3.3-jdk-8

LABEL name="philippgille/alexa-java-builder:debian"
LABEL description="Docker image that contains all Alexa Skills Kit Java SDK and sample dependencies"
LABEL usage="docker run --rm -v /path/to/pom-dir:/usr/src/mymaven philippgille/alexa-java-builder:debian"
LABEL maintainer "Philipp Gillé - https://hub.docker.com/u/philippgille/"

RUN curl -L https://github.com/amzn/alexa-skills-kit-java/archive/master.zip --output alexa-skills-kit-java.zip \
    && unzip alexa-skills-kit-java.zip \
    && mvn -B -f alexa-skills-kit-java-master/pom.xml -s /usr/share/maven/ref/settings-docker.xml assembly:assembly -DdescriptorId=jar-with-dependencies \
    && mvn -B -f alexa-skills-kit-java-master/samples/pom.xml -s /usr/share/maven/ref/settings-docker.xml assembly:assembly -DdescriptorId=jar-with-dependencies \
    && rm alexa-skills-kit-java.zip \
    && rm -r alexa-skills-kit-java-master

WORKDIR /usr/src/mymaven

CMD ["mvn", "-B", "-s", "/usr/share/maven/ref/settings-docker.xml", "assembly:assembly", "-DdescriptorId=jar-with-dependencies"]