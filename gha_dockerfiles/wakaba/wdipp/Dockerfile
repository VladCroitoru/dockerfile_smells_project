FROM quay.io/wakaba/docker-perl-app-base

RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get -y install sudo git wget curl make gcc build-essential libssl-dev && \
    rm -rf /var/lib/apt/lists/*

ADD rev /app/rev
ADD Makefile /app/
ADD bin/ /app/bin/
ADD lib/ /app/lib/
ADD config/ /app/config/
ADD modules/ /app/modules/

RUN cd /app && \
    make deps-docker PMBP_OPTIONS="--execute-system-package-installer --dump-info-file-before-die" && \
    echo '#!/bin/bash' > /server && \
    echo 'exec /app/bin/docker-server' >> /server && \
    chmod u+x /server && \
    rm -fr /app/.git /app/deps /app/t /app/t_deps && \
    rm -rf /var/lib/apt/lists/*

CMD ["/server"]

## License: Public Domain.