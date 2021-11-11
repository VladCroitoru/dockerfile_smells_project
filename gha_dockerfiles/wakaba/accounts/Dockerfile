FROM quay.io/wakaba/docker-perl-app-base

ADD rev /app/
ADD Makefile /app/
ADD LICENSE /app/
ADD config/ /app/config/
ADD db/ /app/db/
ADD bin/ /app/bin/
ADD lib/ /app/lib/
ADD modules/ /app/modules/
ADD t_deps/bin/setup-db-for-test.pl /app/t_deps/bin/setup-db-for-test.pl

RUN cd /app && \
    make deps-docker PMBP_OPTIONS="--execute-system-package-installer --dump-info-file-before-die" && \
    echo '#!/bin/bash' > /server && \
    echo 'port=${PORT:-8080}' >> /server && \
    echo 'cd /app && ./perl bin/sarze.pl 0 ${port}' >> /server && \
    chmod u+x /server && \
    echo '#!/bin/bash' > /setup-db-for-test && \
    echo 'cd /app' >> /setup-db-for-test && \
    echo 'exec ./perl t_deps/bin/setup-db-for-test.pl "$@"' >> /setup-db-for-test && \
    chmod u+x /setup-db-for-test && \
    echo '#!/bin/bash' > /showrev && \
    echo 'cat /app/rev' >> /showrev && \
    chmod u+x /showrev && \
    rm -rf /var/lib/apt/lists/* /app/local/pmbp/tmp
    ## Use of |/setup-db-for-test| is deprecated.

CMD ["/server"]

## License: Public Domain.