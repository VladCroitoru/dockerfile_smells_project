FROM java:8

ENV PORT=8080 \
    GRADLE_HOME=/usr/bin/gradle-2.9 \
    PATH=$PATH:/usr/bin/gradle-2.9/bin:/meta/.cli

EXPOSE 8080

ADD . /meta

WORKDIR /usr/bin

RUN wget -q https://services.gradle.org/distributions/gradle-2.9-bin.zip -O gradle.zip \
    && unzip -q gradle.zip \
    && rm gradle.zip \
    && wget -q https://github.com/concourse/concourse/releases/download/v2.5.1/fly_linux_amd64 -O fly \
    && chmod +x /usr/bin/fly \
    && wget https://nodejs.org/dist/v4.5.0/node-v4.5.0-linux-x64.tar.gz \
    && tar -xzf "node-v4.5.0-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
    && rm "node-v4.5.0-linux-x64.tar.gz" \
    && apt-get update --assume-yes\
    && apt-get install build-essential --assume-yes\
    && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/unlimited_jce_policy.zip "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" \
    && unzip -jo -d ${JAVA_HOME}/jre/lib/security /tmp/unlimited_jce_policy.zip \
    && wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-6.2.zip \
    && unzip -q sonarqube-6.2.zip \
    && wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-2.8.zip \
    && unzip -q sonar-scanner-2.8.zip \
    && cd /meta \
    && gradle build \
    && gradle test \
    && npm install npm@latest -g \
    && npm install -g bower gulp karma \
    && npm install -g newman \
    && npm install -g git \
    && git config --global user.name CI-BuildBot \
    && git config --global user.email svc_DMSBUILD \
    && tar -xzf cf-cli*.tgz -C /usr/bin/ \
    && cd spring_1_3_0_sample \
    && gradle build \
    && gradle test \
    && cd ../spring_1_3_3_sample \
    && gradle build \
    && gradle test
