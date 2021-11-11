FROM ubuntu:xenial 

MAINTAINER Minimum Builds <minumumbuilds@gmail.com>

ARG BUILD_DATE
ARG VCS_REF

LABEL Name=minimum_shrubbery_tacacs \
      Version=0.0.1 \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/minimumbuilds/minimum_tacacs_shrubbery.git" \
      org.label-schema.vcs-ref=$VCS_REF

RUN apt update && \
    apt -y install tacacs+ 

RUN ln -sf /dev/stdout /var/log/tac_plus.acct 

COPY tac_plus.conf /etc/tacacs+/tac_plus.conf

ENTRYPOINT ["/usr/sbin/tac_plus", "-G", "-g", "-C", "/etc/tacacs+/tac_plus.conf"]

EXPOSE 49
