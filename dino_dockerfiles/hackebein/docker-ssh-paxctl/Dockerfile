FROM jeroenpeeters/docker-ssh

RUN apk update \
	&& apk add paxctl \
	&& paxctl -cm `which node`
	