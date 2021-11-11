FROM benchflow/base-images:dns-java8_dev

MAINTAINER Vincenzo FERME <info@vincenzoferme.it>

ENV DOCKER_COMPOSE_VERSION 1.8.0-rc2
ENV BENCHFLOW_DEPLOYMENT_MANAGER_VERSION v-dev

#Install docker-compose
RUN apk --update add curl && \
    curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-Linux-x86_64 > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
	# Get benchflow-deployment-manager
    wget -q --no-check-certificate -O /app/benchflow-deployment-manager.jar https://github.com/benchflow/deployment-manager/releases/download/$BENCHFLOW_DEPLOYMENT_MANAGER_VERSION/benchflow-deployment-manager.jar && \
	# Clean up
	apk del --purge curl && \
    rm -rf /var/cache/apk/*

COPY configuration.yml /app/

COPY ./services/300-deployment-manager.conf /apps/chaperone.d/300-deployment-manager.conf
 
EXPOSE 8080
