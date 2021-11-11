FROM alpine:3.6

# Important!  Update this no-op ENV variable when this Dockerfile
# is updated with the current date. It will force refresh of all
# of the base images and things like `apt-get update` won't be using
# old cached versions when the Dockerfile is built.
ENV REFRESHED_AT=2017-07-31 \
    LANG=en_US.UTF-8 \
    HOME=/opt/app \
    ERLANG_VERSION=20.0.1 \
    # Set this so that CTRL+G works properly
    TERM=xterm
ENV DIALYZER_PLT_PATH=$HOME/.dialyzer_plt
ENV DIALYZER_PLT=$DIALYZER_PLT_PATH/erlang-$ERLANG_VERSION.plt

WORKDIR /tmp/erlang-build

RUN echo "//////////////////// Creating HOME directory /////" && \
    mkdir -p $HOME && \
    echo "//////////////////////// Adding default user /////" && \
    adduser -s /bin/sh -u 1001 -G root -h $HOME -S -D default && \
    echo "///////// Setting HOME owner to default user /////" && \
    chown -R 1001:0 $HOME && \
    echo "/////////////////////////// Setting edge tag /////" && \
    echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    apk --update upgrade --no-cache && \
    echo "///////////////// Installing Erlang/OTP deps /////" && \
    apk add --no-cache pcre@edge \
      ca-certificates \
      openssl-dev \
      ncurses-dev \
      unixodbc-dev \
      zlib-dev \
      openssh \
      git && \
    echo "/////////// Installing Erlang/OTP build deps /////" && \
    apk add --no-cache --virtual .erlang-build \
      autoconf \
      build-base \
      perl-dev && \
    echo "///////////////// Shallow cloning Erlang/OTP /////" && \
    git clone -b OTP-$ERLANG_VERSION --single-branch --depth 1 https://github.com/erlang/otp.git . && \
    echo "//////////// Setting Erlang/OTP env variable /////" && \
    export ERL_TOP=/tmp/erlang-build && \
    export PATH=$ERL_TOP/bin:$PATH && \
    export CPPFlAGS="-D_BSD_SOURCE $CPPFLAGS" && \
    echo "///////////////////// Configuring Erlang/OTP /////" && \
    ./otp_build autoconf && \
    ./configure --prefix=/usr \
      --sysconfdir=/etc \
      --mandir=/usr/share/man \
      --infodir=/usr/share/info \
      --without-javac \
      --without-wx \
      --without-debugger \
      --without-observer \
      --without-jinterface \
      --without-cosEvent\
      --without-cosEventDomain \
      --without-cosFileTransfer \
      --without-cosNotification \
      --without-cosProperty \
      --without-cosTime \
      --without-cosTransactions \
      --without-et \
      --without-gs \
      --without-ic \
      --without-megaco \
      --without-orber \
      --without-percept \
      --without-typer \
      --enable-threads \
      --enable-shared-zlib \
      --enable-ssl=dynamic-ssl-lib \
      --enable-hipe && \
    echo "/////////////////////// Compiling Erlang/OTP /////" && \
    make -j4 && make install && \
    echo "////////////////////// Building dialyzer PLT /////" && \
    mkdir $DIALYZER_PLT_PATH && \
    dialyzer --build_plt --apps erts kernel stdlib crypto && \
    echo "//////////////////////////////// Cleaning up /////" && \
    cd $HOME && \
    rm -rf /tmp/erlang-build && \
    apk del --force .erlang-build && \
    echo "//////////////////////////////// Updating CA /////" && \
    update-ca-certificates --fresh

WORKDIR $HOME

CMD ["/bin/sh"]
