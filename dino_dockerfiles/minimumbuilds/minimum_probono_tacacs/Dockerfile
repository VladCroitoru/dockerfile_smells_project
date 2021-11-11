FROM ubuntu:xenial 

MAINTAINER Minimum Builds <minumumbuilds@gmail.com>

ARG BUILD_DATE
ARG VCS_REF

LABEL Name=minimum_shrubbery_tacacs \
      Version=0.0.1 \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/minimumbuilds/minimum_tacacs_shrubbery.git" \
      org.label-schema.vcs-ref=$VCS_REF

# TODO Move this to multistage build, remove build layer.

RUN apt-get update && \
    apt-get install -y build-essential libnet-ldap-perl libpcre3-dev git

WORKDIR /tacacs
RUN git clone https://github.com/minimumbuilds/probono_tacacs.git PROJECTS
WORKDIR /tacacs/PROJECTS
RUN ./configure
RUN make
RUN make install
COPY tac_plus.cfg .

# RUN ln -sf /dev/stdout /var/log/tac_plus.acct 

CMD ["tac_plus", "tac_plus.cfg"]
EXPOSE 49
