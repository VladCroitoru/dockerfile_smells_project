FROM debian:stretch

RUN apt-get update; \
    apt-get install -y default-jre wget unzip

RUN cd tmp; wget https://cdn.sencha.com/cmd/6.5.2/no-jre/SenchaCmd-6.5.2-linux-amd64.sh.zip; \
    unzip SenchaCmd-6.5.2-linux-amd64.sh.zip; \
    VERSION=$(ls | grep "SenchaCmd.*sh$" | cut -d"-" -f2); \
    ./SenchaCmd-$VERSION-linux-amd64.sh -q -dir /opt/sencha/cmd/$VERSION -Dall=true; \
    rm SenchaCmd-6.5.2-linux-amd64.sh.zip SenchaCmd-$VERSION-linux-amd64.sh; \
    ln -s /opt/sencha/cmd/$VERSION/sencha /usr/local/bin/; \
    \
    mkdir /opt/sencha/sdk; \
    wget https://cdn.sencha.com/ext/gpl/ext-6.2.0-gpl.zip; \
    unzip ext-6.2.0-gpl.zip; \
    mv ext-6.2.0 /opt/sencha/sdk/; \
    rm ext-6.2.0-gpl.zip; \
    \
    apt-get clean

RUN mkdir /app

WORKDIR /app

CMD ["sencha", "app", "watch"]
