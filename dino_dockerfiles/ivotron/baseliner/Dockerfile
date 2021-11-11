FROM ivotron/ansible:2.4.1.0-alpine3

RUN apk --no-cache add bash curl git rsync && \
    curl -SL https://download.docker.com/linux/static/stable/x86_64/docker-17.06.2-ce.tgz | tar -xzv docker/docker && \
    mv docker/docker /usr/bin && \
    rm -r docker/ && \
    echo '#!/bin/bash' > /usr/bin/sudo && \
    echo '$@' >> /usr/bin/sudo && \
    chmod 755 /usr/bin/sudo
ADD . /etc/ansible/roles/baseliner

ENTRYPOINT ["/etc/ansible/roles/baseliner/bin/baseliner"]
