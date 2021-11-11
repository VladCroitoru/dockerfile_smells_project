FROM nginx

ENV HOST $VIRTUAL_HOST

RUN mkdir -p /opt/work
COPY nginx.conf /opt/work
COPY replace_env_and_run.sh /opt/work/replace_env_and_run.sh

ENTRYPOINT bash /opt/work/replace_env_and_run.sh