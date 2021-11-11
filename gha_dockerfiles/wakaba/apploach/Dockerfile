FROM quay.io/wakaba/docker-perl-app-base

ADD rev /app/
ADD Makefile /app/
ADD LICENSE /app/
ADD config/ /app/config/
ADD db/ /app/db/
ADD bin/ /app/bin/
ADD lib/ /app/lib/
ADD modules/ /app/modules/

RUN cd /app && \
    make deps-docker PMBP_OPTIONS="--execute-system-package-installer --dump-info-file-before-die" && \
    echo '#!/bin/bash' > /server && \
    echo 'export LANG=C' >> /server && \
    echo 'export TZ=UTC' >> /server && \
    echo 'port=${PORT:-8080}' >> /server && \
    echo 'cd /app && ./perl bin/sarze.pl 0 ${port}' >> /server && \
    chmod u+x /server && \
    echo '#!/bin/bash' > /showrev && \
    echo 'cat /app/rev' >> /showrev && \
    chmod u+x /showrev && \
    rm -rf /var/lib/apt/lists/* /app/local/pmbp/tmp /app/deps

CMD ["/server"]

## License: Public Domain.
