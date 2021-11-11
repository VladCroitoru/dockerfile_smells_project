FROM circleci/android:api-28-node8-alpha

MAINTAINER Okode <info@okode.com>

# Install Cordova and Ionic
RUN sudo npm update -g
RUN sudo npm install -g ionic cordova
RUN cordova telemetry off
RUN CI=true ionic config set -g daemon.updates false
RUN ionic config set -g telemetry false

# Install Fastlane
RUN gem install fastlane -NV

# Install Gradle
ARG GRADLE_VERSION=4.10.2
RUN sudo curl https://downloads.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip > /tmp/gradle-$GRADLE_VERSION-bin.zip
RUN sudo unzip /tmp/gradle-$GRADLE_VERSION-bin.zip -d /tmp && rm /tmp/gradle-$GRADLE_VERSION-bin.zip
RUN sudo mv /tmp/gradle-$GRADLE_VERSION /opt/gradle
ENV PATH="/opt/gradle/bin:${PATH}"

# Install GitHub Release Utility
RUN sudo mkdir -p /opt/github-release
RUN sudo curl -L https://github.com/aktau/github-release/releases/download/v0.7.2/linux-amd64-github-release.tar.bz2 | sudo tar -xjC /opt/github-release
ENV PATH="/opt/github-release/bin/linux/amd64:${PATH}"

# Install SonarQube Scanner
ARG SONARQUBE_SCANNER_VERSION=3.2.0.1227
RUN sudo curl -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SONARQUBE_SCANNER_VERSION.zip > /tmp/sonar-scanner-cli-$SONARQUBE_SCANNER_VERSION.zip
RUN sudo unzip /tmp/sonar-scanner-cli-$SONARQUBE_SCANNER_VERSION.zip -d /tmp && rm /tmp/sonar-scanner-cli-$SONARQUBE_SCANNER_VERSION.zip
RUN sudo mv /tmp/sonar-scanner-$SONARQUBE_SCANNER_VERSION /opt/sonar-scanner
ENV PATH="/opt/sonar-scanner/bin:${PATH}"

# Copy Crashlytics Dev Tools
COPY resources/crashlytics-devtools.jar /opt/crashlytics/

