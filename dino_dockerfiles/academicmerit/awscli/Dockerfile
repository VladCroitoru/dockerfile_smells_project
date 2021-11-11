FROM python:3.6.7-alpine3.8 AS base

# install python dependencies
FROM base AS builder

COPY requirements.txt /
RUN pip install --upgrade pip==18.1 && \
   pip install --install-option="--prefix=/install" -r /requirements.txt

# build final image
FROM base

COPY --from=builder /install /usr/local
RUN apk add --no-cache bash=4.4.19-r1
ARG UID=1000
RUN adduser -D -u $UID aws
USER aws
WORKDIR /home/aws
