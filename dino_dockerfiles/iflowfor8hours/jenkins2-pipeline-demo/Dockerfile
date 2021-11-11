FROM jenkinsci/jenkins:latest
MAINTAINER Matt Urbanski

USER root
ENV CF_CLI $PWD/
ENV PATH $CF_CLI:$PATH

ADD https://cli.run.pivotal.io/stable?release=linux32-binary&version=6.19.0&source=github-rel $CF_CLI/cf.tgz

RUN tar zxvf $CF_CLI/cf.tgz
RUN cf --version

USER jenkins
RUN install-plugins.sh \
  branch-api \
  durable-task \
  git-server \
  handlebars \
  icon-shim \
  jquery-detached \
  junit \
  mailer \
  matrix-project \
  mock-slave \
  momentjs \
  pipeline-build-step \
  pipeline-input-step \
  pipeline-stage-step \
  pipeline-stage-view \
  scm-api \
  script-security \
  ssh-credentials \
  structs \
  workflow-api \
  workflow-basic-steps \
  workflow-durable-task-step \
  workflow-job \
  workflow-multibranch \
  workflow-scm-step \
  workflow-step-api \
  workflow-support \
  workflow-aggregator \
  ssh-slaves \
  ws-cleanup
