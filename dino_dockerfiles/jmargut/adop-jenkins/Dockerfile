FROM jenkins:1.609.1

MAINTAINER Nick Griffin, <nicholas.griffin>

ENV GERRIT_HOST_NAME gerrit
ENV GERRIT_PORT 8080
ENV GERRIT_JENKINS_USERNAME="" GERRIT_JENKINS_PASSWORD=""

# Copy in configuration files push test trigger build 1.11
COPY resources/plugins.txt /usr/share/jenkins/ref/
COPY resources/init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/
COPY resources/scripts/ /usr/share/jenkins/ref/adop_scripts/
COPY resources/jobs/ /usr/share/jenkins/ref/jobs/
COPY resources/scriptler/ /usr/share/jenkins/ref/scriptler/scripts/
COPY resources/views/ /usr/share/jenkins/ref/init.groovy.d/
COPY resources/m2/ /usr/share/jenkins/ref/.m2
COPY resources/entrypoint.sh /entrypoint.sh
COPY resources/scriptApproval.xml /usr/share/jenkins/ref/

# Reprotect
USER root
RUN chmod +x -R /usr/share/jenkins/ref/adop_scripts/ && chmod +x /entrypoint.sh
#USER jenkins

# Environment variables
ENV ADOP_LDAP_ENABLED=true ADOP_SONAR_ENABLED=true ADOP_ANT_ENABLED=true ADOP_MAVEN_ENABLED=true ADOP_NODEJS_ENABLED=true ADOP_GERRIT_ENABLED=true

ENV LDAP_GROUP_NAME_ADMIN=""

RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt

# Path
ENV PATH $PATH:${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:${GRADLE_HOME}/bin

# Dependencies
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -yq libstdc++6:i386 zlib1g:i386 libncurses5:i386 
#ant maven --no-install-recommends
ENV GRADLE_URL http://services.gradle.org/distributions/gradle-2.2.1-all.zip
RUN curl -L ${GRADLE_URL} -o /tmp/gradle-2.2.1-all.zip && unzip /tmp/gradle-2.2.1-all.zip -d /usr/local && rm /tmp/gradle-2.2.1-all.zip
ENV GRADLE_HOME /usr/local/gradle-2.2.1

# Download and untar SDK
ENV ANDROID_SDK android-sdk_r24.4.1-linux.tgz
RUN wget https://dl.google.com/android/${ANDROID_SDK} && tar -xvzf ${ANDROID_SDK} \
&& mv android-sdk-linux /usr/local/android-sdk-linux \
&& rm ${ANDROID_SDK} 
ENV ANDROID_HOME /usr/local/android-sdk-linux

# Install Android SDK components
ENV ANDROID_SDK_COMPONENTS platform-tools,build-tools-24.0.0,android-23,android-24,build-tools-23.0.2,extra-android-support
RUN echo y | ${ANDROID_HOME}/tools/android update sdk --no-ui --all --filter "${ANDROID_SDK_COMPONENTS}" \
&& ${ANDROID_HOME}/tools/android update sdk --filter 21 --no-ui

ENTRYPOINT ["/entrypoint.sh"]
