FROM tokbox/centos6_java8_pst

MAINTAINER Manas Pradhan <manas@tokbox.com>

ENV LANG C.UTF-8
ENV ELASTALERT_HOME .
ENV ELASTALERT_VERSION v0.1.4

ARG vcs_ref="Unknown"
ARG vcs_branch="Unknown"
ARG build_date="Unknown"

LABEL org.label-schema.vcs-type="git" \
      org.label-schema.vcs-url="https://github.com/manasdpradhan/elastalert" \
      org.label-schema.vcs-ref=$vcs_ref \
      org.label-schema.vcs-branch=$vcs_branch \
      org.label-schema.docker.dockerfile=/Dockerfile \
      org.label-schema.build-date=$build_date

WORKDIR /opt


RUN yum -y install \
    ca-certificates \
    python \
    epel-release \
    python-devel \
    gcc \
    libffi-devel \
    openssl-devel \
    build-essential

RUN yum clean all

RUN yum -y install \
  python-pip \

COPY setup.py .
RUN mkdir rules
RUN mkdir elastalert
COPY rules/* ./rules/
COPY ./config.yaml ./config.yaml
COPY ./Dockerfile .
COPY ./elastalert ./elastalert



ADD requirements*.txt ./
RUN pip install --upgrade -r requirements.txt


CMD ["python", "elastalert/elastalert.py", "--verbose"]
