FROM alpine:latest

# install packages and change shell to bash (just to be safe)
RUN apk add --no-cache bash openssh-client git rsync ed jq && \
    sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

CMD ["/bin/bash"]
