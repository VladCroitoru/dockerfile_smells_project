FROM nginx:stable-alpine

ENV PROJECT_ROOT_DIR /opt/snake_tournament

COPY client ${PROJECT_ROOT_DIR}/client
COPY server ${PROJECT_ROOT_DIR}/server
COPY docker_content/entrypoint.sh /entrypoint.sh
COPY docker_content/nginx_default.conf /etc/nginx/conf.d/default.conf

RUN apk update
RUN apk add python3
RUN python3.5 -m pip install -r ${PROJECT_ROOT_DIR}/server/requirements.txt

EXPOSE 80

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
