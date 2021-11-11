FROM google/cloud-sdk:alpine
RUN apk --update add openjdk8
RUN gcloud components install app-engine-java kubectl

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
