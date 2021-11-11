FROM ubuntu:latest
MAINTAINER YC Liu "yuecendev@gmail.com"
COPY . /sendgrid-webhook-handler
WORKDIR /sendgrid-webhook-handler
RUN build_deps="python-dev build-essential" && \
    apt-get update -y && apt-get install -y python-pip ${build_deps} && \
    pip install -r requirements.txt && \
    apt-get purge -y --auto-remove ${build_deps} && \
    apt-get autoremove -y
ENTRYPOINT ["/sendgrid-webhook-handler/docker-entrypoint.sh"]
