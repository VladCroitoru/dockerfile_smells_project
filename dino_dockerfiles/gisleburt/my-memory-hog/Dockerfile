FROM alpine:3.4

RUN apk update \
 && apk add php5

ADD swallow-memory.php swallow-memory.php

CMD php swallow-memory.php
