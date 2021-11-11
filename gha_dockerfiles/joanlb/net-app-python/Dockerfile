FROM alpine

ARG DATE=${DATE}
ARG NAME=${NAME}
ENV NAME=${NAME}
RUN apk --no-cache add bash

ADD ./.env /.env
ADD ./entrypoint /entrypoint

RUN bash < /entrypoint
