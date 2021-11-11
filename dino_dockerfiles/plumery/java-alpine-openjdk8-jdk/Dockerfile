FROM fabric8/java-alpine-openjdk8-jdk:1.2.5
RUN apk add --update bash && rm -rf /var/cache/apk/*
ADD wait-for-it.sh /
RUN chmod +x /wait-for-it.sh
