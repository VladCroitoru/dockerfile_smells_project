FROM registry.access.redhat.com/ubi8/python-38

LABEL author="eduardomcerqueira@gmail.com"
LABEL maintainer="eduardomcerqueira@gmail.com"
LABEL description="seeker for new code snippets"

ENV GITHUB_TOKEN=${GITHUB_TOKEN:-""}
ENV GITHUB_USERNAME=${GITHUB_USERNAME:-"eduardocerqueira"}
ENV GITHUB_EMAIL=${GITHUB_EMAIL:-"eduardomcerqueira@gmail.com"}
ARG SEEKER_RUN=${SEEKER_RUN:-""}

RUN env | grep -e SEEKER_RUN -e GITHUB -e GITHUB_TOKEN

RUN git config --global user.name $GITHUB_USERNAME
RUN git config --global user.email $GITHUB_EMAIL
RUN git config --global http.sslVerify false

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir devpi-client
RUN pip install --no-cache-dir -U pip setuptools setuptools_scm wheel

# install from repo/
RUN git clone https://github.com/eduardocerqueira/seeker.git
# install from local, for debug and troubleshooting
#ADD . seeker
WORKDIR seeker
COPY ops/scripts/docker_entrypoint.sh seeker/docker_entrypoint.sh

USER root
RUN chmod +x seeker/docker_entrypoint.sh
RUN chown -R 1001:0 .
RUN chmod -R 755 .

USER 1001
RUN pip install --no-cache-dir -e .
RUN pip freeze |grep seeker

# check on build
WORKDIR seeker
RUN seeker $SEEKER_RUN

# on running
ENTRYPOINT ./docker_entrypoint.sh
