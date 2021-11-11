FROM dlanguage/dmd

ADD . .

WORKDIR /src

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:chris-needham/ppa && apt-get update && \
    apt-get install -y curl libsox-fmt-mp3 sox git audiowaveform && \
    curl -sL https://deb.nodesource.com/setup_9.x | bash && \
    apt-get install -y nodejs && \
    dub --quiet build duck:duck --build=release && \
    dub --quiet build duck:runtime --build=release && \
    rm -rf duck && \
    cd tools/server/site && npm install && npm run build && \
    rm -rf node_modules && cd ../../.. && \
    npm uninstall -g npm && \
    apt-get remove --purge --autoremove -y git python3 curl && \
    rm -rf /usr/share/doc /usr/share/doc/man /var/lib/apt/lists /dlang/dub /dlang/${COMPILER}-${COMPILER_VERSION}/src/dmd

EXPOSE 80

CMD find . && cd tools/server && node index
