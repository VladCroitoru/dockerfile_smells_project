FROM openjdk:8
MAINTAINER Matthew Poletin, "contact@matthewpoletin.com"

# set variables
ENV GRADLE_VERSION 4.3
ENV GRADLE_HOME /opt/gradle
ENV PATH $PATH:$GRADLE_HOME/gradle-$GRADLE_VERSION/bin

# update tools
RUN apt-get update && apt-get install -q -y \
	wget \
	unzip \
	openjdk-8-jdk \
	git

# install gradle
RUN wget --no-check-certificate "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" -O gradle.zip && \
    mkdir $GRADLE_HOME && \
    unzip -d $GRADLE_HOME gradle.zip && \
    rm gradle.zip

# build project
CMD ["gralde", "build"]

# move file
ADD build/libs/levonke-Community-0.0.1.jar levonke-Community.jar

# listen on port
EXPOSE 8442

# run service
ENTRYPOINT ["java", "-jar", "levonke-Community.jar"]
