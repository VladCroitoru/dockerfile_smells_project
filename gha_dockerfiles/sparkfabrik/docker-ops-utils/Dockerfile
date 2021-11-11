FROM alpine:3.13
RUN apk add --no-cache file gettext jq rclone mysql-client mariadb-connector-c postgresql-client bash curl aws-cli
RUN curl -o /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it

# Make the terminal pretty and add node_modules binaries to PATH
RUN echo "whoami &>/dev/null && PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] ' || PS1='\[\033[1;36m\]unknown\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '" >> /etc/profile \
    && echo "export TERM=xterm" >> /etc/profile

COPY app /app

RUN chmod +x /app/docker-entrypoint.sh \
    && chmod -R +x /app/commands

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
