FROM alpine:3.4
MAINTAINER Andrey Subbotin "andrey@subbotin.me"

RUN apk --no-cache add bash jq

# Install kubectl
# Note: Latest version may be found on:
# https://aur.archlinux.org/packages/kubectl-bin/
ADD https://storage.googleapis.com/kubernetes-release/release/v1.7.1/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl && kubectl version --client

RUN mkdir -p /srv
COPY run.sh /srv/
ENTRYPOINT ["/bin/bash"]
CMD ["/srv/run.sh"]



