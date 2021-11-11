FROM alpine:latest

# bash
RUN apk -Uuv add coreutils bash bash-doc bash-completion

# AWS CLI
RUN \
	mkdir -p /aws && \
	apk -Uuv add groff less python py-pip && \
	pip install awscli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*

WORKDIR /aws

COPY app/* ./

ENTRYPOINT ["./check-ecs-service.sh"]
CMD ['']
