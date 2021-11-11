FROM mesosphere/aws-cli:1.11.188 AS resource

RUN apk --no-cache add \
  jq \
  bash \
  curl \
  git

#RUN git config --global user.email "git@localhost"
#RUN git config --global user.name "git"

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*

#FROM resource AS tests
#ADD test/ /tests
#RUN /tests/all.sh

FROM resource
