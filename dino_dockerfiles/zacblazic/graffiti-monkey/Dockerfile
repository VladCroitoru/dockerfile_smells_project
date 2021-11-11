FROM python:2.7.14-alpine3.7 AS builder

WORKDIR /src
ADD . /src
RUN python setup.py sdist

FROM python:2.7.14-alpine3.7

ARG GRAFFITI_MONKEY_VERSION
ARG GRAFFITI_MONKEY_PACKAGE="graffiti_monkey-${GRAFFITI_MONKEY_VERSION}.tar.gz"

COPY --from=builder /src/dist /tmp
RUN pip install /tmp/${GRAFFITI_MONKEY_PACKAGE}

CMD ["/bin/sh"]
