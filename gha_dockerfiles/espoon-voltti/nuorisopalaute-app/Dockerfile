# NOTE: Copied from "espoon-voltti/kulta-service", mainly serves as an example,
# an is not currently directly usable!

# Example Dockerfile for use in local development

ARG BASE_IMAGE=307238562370.dkr.ecr.eu-west-1.amazonaws.com/voltti/flyway
# NOTE: There is no guarantee that latest is actually the latest image in the registry. Thus, remember to always
# override BASE_IMAGE_VERSION with a commit hash in the voltti-dockerfiles repository.
ARG BASE_IMAGE_VERSION=latest

# Pull Voltti's OpenJDK base image
FROM ${BASE_IMAGE}:${BASE_IMAGE_VERSION}

ENV USERNAME voltti
ENV SOURCE_DIR /usr/src/app
# Specifies the Gradle user home directory where Gradle stores, e.g., the caches
ENV GRADLE_USER_HOME ${SOURCE_DIR}/.gradle_user_home

WORKDIR ${SOURCE_DIR}

USER root

# Install bash, as the entrypoint.sh requires that. Also, install sudo and
# supervisor for running gradle's continuous build as a separate process.
RUN set -eux \
    && apt-get update && apt-get -y install \
       sudo \
       supervisor \
    && rm -rf /var/lib/apt/lists/*

# Create log directories for gradle's continuous build and supervisor
RUN mkdir -p /var/log/gradle && \
    mkdir -p /var/log/supervisor

# Copy the sudoers file so that we can run supervisor with sudo
COPY ./docker/local/sudoers /etc/sudoers.local
RUN echo "#include /etc/sudoers.local" >> /etc/sudoers

# Copy the supervisor conf which configures gradle's continuous build to be managed by supervisor
COPY ./docker/local/supervisord.conf /etc/supervisord.conf

USER ${USERNAME}

# Copy entrypoint to the parent directory, so that we can change its permissions
COPY --chown=voltti:voltti entrypoint.sh ..
RUN chmod +x ../entrypoint.sh

# Expose Spring Boot's embedded server
EXPOSE 8080

ENTRYPOINT ["/usr/src/entrypoint.sh"]

# Command line parameters to be passed to the gradlew entrypoint
CMD ["bootRun"]
