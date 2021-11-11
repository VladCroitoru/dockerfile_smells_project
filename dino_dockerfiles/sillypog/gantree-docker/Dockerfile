FROM ruby:2.1.2-onbuild

MAINTAINER Peter Hastie <phastie@bleacherreport.com>

RUN apt-get update && apt-get install -qy \
  wget \
  unzip \
  groff

RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -b ~/bin/aws

WORKDIR /deploy

CMD ["/bin/bash"]
