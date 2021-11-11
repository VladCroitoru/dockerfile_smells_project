# Image installs with latest Java 8 OpenJDK on Alpine Linux
FROM openjdk:8-jdk-alpine

# Update and upgrade then install 
# curl, Maven, Git, Docker, and Docker Compose
RUN apk update && \
	apk upgrade && \
	apk --no-cache add curl && \
	apk --no-cache add maven && \
	apk --no-cache add git && \
	apk --no-cache add docker && \
	apk --no-cache add py-pip && \
	pip install docker-compose