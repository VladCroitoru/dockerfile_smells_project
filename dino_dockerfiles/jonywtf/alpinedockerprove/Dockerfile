FROM docker:1.10.3

RUN apk add --no-cache perl make
RUN cpan App::Prove;
RUN printf '#!/bin/sh\ndocker run -i tnt $1\nretval=$?' > /usr/bin/run_docker
RUN printf '#!/bin/sh\nprove -v /usr/bin/run_docker :: $1\nretval=$?' > /usr/bin/run_test
RUN chmod 777 /usr/bin/run_docker
RUN chmod 777 /usr/bin/run_test
