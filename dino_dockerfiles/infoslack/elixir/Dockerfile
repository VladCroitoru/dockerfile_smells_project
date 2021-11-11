FROM erlang:18.1

MAINTAINER Daniel Romero <infoslack@gmail.com>

ENV ELIXIR_VERSION=1.1.1

RUN curl -SL "https://github.com/elixir-lang/elixir/archive/v$ELIXIR_VERSION.tar.gz" -o elixir.tar.gz \
    && mkdir -p /usr/src/elixir \
    && tar -xvf elixir.tar.gz -C /usr/src/elixir --strip-components=1 \
    && rm elixir.tar.gz \
    && cd /usr/src/elixir \
    && make -j$(nproc) clean install \
    && rm -rf /usr/src/elixir

CMD ["mix"]
