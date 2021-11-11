FROM alpine
# for /etc/ssh/moduli, install openssh-client
RUN apk update && \
    apk add openssh-client \
        python py-virtualenv python-dev gcc musl-dev libffi-dev openssl-dev
COPY . /opt/hotcake
RUN virtualenv /opt/hotcake/venv && /opt/hotcake/venv/bin/pip install -U pip && /opt/hotcake/venv/bin/pip install /opt/hotcake
ENV HOTCAKE_HTTP_PORT=80 HOTCAKE_SSH_PORT=22
# please set these variables at runtime for login
#ENV HOTCAKE_USERNAME=myuser HOTCAKE_PASSWORD=mypassword
EXPOSE 80 22
ENTRYPOINT ["/opt/hotcake/entrypoint.sh"]
