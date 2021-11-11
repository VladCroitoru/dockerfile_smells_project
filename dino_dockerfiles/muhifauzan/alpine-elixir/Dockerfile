FROM muhifauzan/alpine-erlang:20.0.1

# Important!  Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like `apt-get update` won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT=2017-07-31 \
    ELIXIR_VERSION=1.5.1
ENV DIALYZER_PLT=$DIALYZER_PLT_PATH/dialyxir_erlang-$ERLANG_VERSION.plt \
    ELIXIR_PLT=$DIALYZER_PLT_PATH/dialyxir_erlang-$ERLANG_VERSION_elixir-$ELIXIR_VERSION.plt

WORKDIR /tmp/elixir-build

RUN apk --update upgrade --no-cache && \
    echo "/////////////// Installing Elixir build deps /////" && \
    apk add --no-cache --virtual .elixir-build \
      make && \
    echo "///////////////////// Shallow cloning Elixir /////" && \
    git clone -b v$ELIXIR_VERSION --single-branch --depth 1 https://github.com/elixir-lang/elixir.git . && \
    echo "/////////////////////////// Compiling Elixir /////" && \
    make && make install && \
    mix local.hex --force && \
    mix local.rebar --force && \
    echo "////////////////////// Building dialyzer PLT /////" && \
    mkdir /tmp/dialyxir && cd /tmp/dialyxir && \
    git clone https://github.com/jeremyjh/dialyxir.git . && \
    MIX_ENV=prod mix do compile, archive.build, archive.install --force && \
    cd ../ && \
    mix dialyzer --plt && \
    rm $DIALYZER_PLT_PATH/* && \
    mv $HOME/.mix/dialyxir* $DIALYZER_PLT_PATH && \
    echo "//////////////////////////////// Cleaning up /////" && \
    cd $HOME && \
    rm -rf /tmp/elixir-build && \
    apk del --force .elixir-build && \
    rm -rf /tmp/dialyxir && \
    rm -rf .mix/archives/dialyxir*

WORKDIR $HOME

CMD ["/bin/sh"]
