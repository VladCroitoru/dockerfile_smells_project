FROM sameersbn/ubuntu:14.04.20170228
MAINTAINER Jan Unsleber <j.unsleber@wwu.de>

ENV GITLAB_RUNNER_VERSION=10.1.0 \
    GITLAB_RUNNER_USER=gitlab_runner \
    GITLAB_RUNNER_HOME_DIR="/home/gitlab_runner"
ENV GITLAB_RUNNER_DATA_DIR="${GITLAB_RUNNER_HOME_DIR}/data"

ENV CA_CERTIFICATES_PATH=''
ENV RUNNER_CONCURRENT=''
ENV CI_SERVER_URL=''
ENV RUNNER_TOKEN=''
ENV RUNNER_EXECUTOR='shell'
ENV RUNNER_DESCRIPTION=latex
ENV RUNNER_TAG_LIST=latex
ENV RUNNER_LIMIT=1

ENV RUNNER_DOCKER_MODE='socket'
ENV RUNNER_DOCKER_PRIVATE_REGISTRY_URL=''
ENV RUNNER_DOCKER_PRIVATE_REGISTRY_TOKEN=''
ENV RUNNER_DOCKER_ADDITIONAL_VOLUME=''
ENV RUNNER_OUTPUT_LIMIT='4096'
ENV RUNNER_AUTOUNREGISTER='false'

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E1DD270288B4E6030699E45FA1715D88E1DF1F24 \
 && echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >> /etc/apt/sources.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      git-core openssh-client curl libapparmor1 \
 && wget -O /usr/local/bin/gitlab-runner \
      https://gitlab-runner-downloads.s3.amazonaws.com/v${GITLAB_RUNNER_VERSION}/binaries/gitlab-runner-linux-amd64 \
 && chmod 0755 /usr/local/bin/gitlab-runner \
 && adduser --disabled-login --gecos 'GitLab CI Runner' ${GITLAB_RUNNER_USER} \
 && sudo -HEu ${GITLAB_RUNNER_USER} ln -sf ${GITLAB_RUNNER_DATA_DIR}/.ssh ${GITLAB_RUNNER_HOME_DIR}/.ssh \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

VOLUME ["${GITLAB_RUNNER_DATA_DIR}"]
WORKDIR "${GITLAB_RUNNER_HOME_DIR}"
ENTRYPOINT ["/sbin/entrypoint.sh"]

# include additional repos
RUN apt-get update -q
RUN apt-get install -qy texlive-full 
RUN apt-get install -qy python-pygments 
RUN apt-get install -qy gnuplot
RUN apt-get install -qy biber

RUN chown -R ${GITLAB_RUNNER_USER}:${GITLAB_RUNNER_USER} ${GITLAB_RUNNER_HOME_DIR}

RUN locale-gen en_US.UTF-8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
