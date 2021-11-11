FROM alpine:3.6


ENV DOCKER_VERSION=17.05.0-ce \
    DOCKER_COMPOSE_VERSION=1.13.0 \
    ENTRYKIT_VERSION=0.4.0 \
    S3CMD_VERSION=2.0.0 \
    MARATHON_DEPLOY_VERSION=0.1.55

RUN apk update && apk add make ruby ruby-json ruby-rdoc ruby-dev ruby-irb git bash
RUN gem install marathon_deploy -v $MARATHON_DEPLOY_VERSION



# Install sbt from edge/testing
RUN apk add sbt --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

# Install Docker and Docker Compose
RUN apk --update --no-cache \
    add curl device-mapper py-pip iptables make ruby ruby-json ruby-rdoc ruby-dev ruby-irb && \
    rm -rf /var/cache/apk/* && \
    curl https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz | tar zx && \
    mv /docker/* /bin/ && chmod +x /bin/docker* && \
    pip install docker-compose==${DOCKER_COMPOSE_VERSION}

# Install entrykit
RUN curl -L https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz | tar zx && \
    chmod +x entrykit && \
    mv entrykit /bin/entrykit && \
    entrykit --symlink

# Include useful functions to start/stop docker daemon in garden-runc containers in Concourse CI.
# Example: source /docker-lib.sh && start_docker
COPY docker-lib.sh /docker-lib.sh

ENTRYPOINT [ \
	"switch", \
		"shell=/bin/sh", "--", \
	"codep", \
		"/bin/docker daemon" \
]
