FROM alpine:latest

# install packages and change shell to bash (just to be safe)
RUN apk update && apk add --no-cache bash openssh-client expect jq git rsync lftp && \
	sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

CMD ["/bin/bash"]
