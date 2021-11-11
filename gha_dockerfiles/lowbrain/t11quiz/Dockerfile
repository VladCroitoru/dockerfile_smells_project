ARG VARIANT="11"
ARG GRADLE_VERSION="7.2"
ARG BUILD_PATH="/workspace"
ARG JAR_FILEPATH="${BUILD_PATH}/build/libs/quiz.jar"

#--------------------------------------------------------------------------------
# Development Container
#--------------------------------------------------------------------------------
# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.191.0/containers/java/.devcontainer/base.Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/java:0-${VARIANT} AS quizdev
ARG GRADLE_VERSION

RUN su vscode -c "umask 0002 && . /usr/local/sdkman/bin/sdkman-init.sh && sdk install gradle \"${GRADLE_VERSION}\""

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

#--------------------------------------------------------------------------------
# Build Container
#--------------------------------------------------------------------------------
FROM quizdev As quizbuilder
ARG BUILD_PATH
ARG JAR_FILEPATH

# QUIZ APP Build
COPY --chown=vscode:sdkman ./ "${BUILD_PATH}"
RUN su - vscode -c "cd ${BUILD_PATH} && gradle --no-daemon bootJar"

# QUIZ APP Run
USER vscode
WORKDIR ${BUILD_PATH}
CMD ["java", "-jar", "${JAR_FILEPATH}"]

#--------------------------------------------------------------------------------
# Production Container
#--------------------------------------------------------------------------------
FROM openjdk:${VARIANT}-jdk-buster AS quiz
ARG JAR_FILEPATH

# QUIZ APP Deploy
RUN addgroup --system app && adduser --system --ingroup app app
COPY --from=quizbuilder --chown=app:app "${JAR_FILEPATH}" /app.jar

# QUIZ APP Run
USER app
ENTRYPOINT ["java","-jar","/app.jar"]
