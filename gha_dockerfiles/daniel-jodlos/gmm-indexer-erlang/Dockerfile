FROM erlang:alpine

RUN mkdir /buildroot
WORKDIR /buildroot

RUN apk add -uUv git gcc g++ && \
    git clone https://github.com/erlang/rebar3.git && \
    cd rebar3 && \
    ./bootstrap

COPY src src/
COPY include include/
COPY rebar.config .
RUN rebar3 as prod release

FROM erlang:alpine

RUN apk add --no-cache openssl && \
    apk add --no-cache ncurses-libs && \
    apk add --no-cache redis

COPY --from=0 /buildroot/_build/prod/rel/prod /prod
COPY config/redis.conf .
COPY ./entrypoint.sh .

RUN chmod 777 ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
