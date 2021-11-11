FROM ubuntu:latest

MAINTAINER Damien Matabon <damien.matabon@gmail.com>

RUN apt-get update && apt-get install -y rubygems git curl
RUN gem install net-ssh -v '~> 3.1'
RUN gem install capistrano-symfony --pre

# tmp fix to clone the last version of capistrano-file-permissions until there is a tag
RUN rm -rf /var/lib/gems/2.3.0/gems/capistrano-file-permissions-1.0.0 && \
    git clone https://github.com/capistrano/file-permissions.git /var/lib/gems/2.3.0/gems/capistrano-file-permissions-1.0.0

ENV SSH_AUTH_SOCK /root/ssh-agent

WORKDIR /root/workdir

ENTRYPOINT ["cap"]