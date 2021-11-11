FROM gitlab/gitlab-runner:alpine-v12.5.0
LABEL maintainer="Waldemar Reusch<waldemar.reusch@googlemail.com>"

ENV REGISTER_LOCKED false
ENV REGISTER_NON_INTERACTIVE true
ENV RUNNER_EXECUTOR docker
ENV DOCKER_IMAGE docker:latest
ENV DOCKER_VOLUMES /var/run/docker.sock:/var/run/docker.sock

COPY runner /
RUN chmod +x /runner

ENTRYPOINT ["/runner"]
