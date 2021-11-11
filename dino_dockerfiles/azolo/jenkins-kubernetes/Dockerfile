FROM jenkins/jenkins:lts-alpine-jdk11

COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1 -XshowSettings:vm"
ENV TRY_UPGRADE_IF_NO_MARKER=true

COPY plugins.txt .

RUN /usr/local/bin/install-plugins.sh $(cat plugins.txt)
RUN git lfs install
