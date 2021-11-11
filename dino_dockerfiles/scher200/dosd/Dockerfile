FROM dockerswarm/dind:18.02.0-ce

ARG DOCKER_VERSION=18.02.0-ce

RUN VERSION=$DOCKER_VERSION ./get_docker.sh

ADD setup.sh setup.sh

ENTRYPOINT ["/bin/bash"]

CMD ["setup.sh"]
