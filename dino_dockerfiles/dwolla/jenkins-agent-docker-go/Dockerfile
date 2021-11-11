FROM dwolla/jenkins-agent-core
MAINTAINER Dwolla Dev <dev+jenkins-go@dwolla.com>
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/jenkins-agent-docker-go"

USER root

RUN apk add --no-cache go make nodejs-npm && \
		npm install -g serverless

USER jenkins
