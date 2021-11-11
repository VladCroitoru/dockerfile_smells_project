FROM openjdk:7

ENV FLEX_HOME='/flex-sdk'

RUN update-ca-certificates \
		&& apt-get update \
		&& apt-get install -y --no-install-recommends ant rsync bzip2 \
		&& curl -L -o /tmp/flex-sdk.tar.gz http://www-us.apache.org/dist/flex/4.16.0/binaries/apache-flex-sdk-4.16.0-bin.tar.gz \
		&& tar -xzf /tmp/flex-sdk.tar.gz -C /tmp \
		&& mv /tmp/apache-flex-sdk-* $FLEX_HOME \
		&& cd $FLEX_HOME \
		&& ant -f installer.xml -Dair.sdk.version=2.6 \
                         -Djava.awt.headless=true \
                         -Dinput.air.download=y \
                         -Dinput.fontswf.download=y \
                         -Dinput.flash.download=y \
		&& chown -R root:root $FLEX_HOME \
		&& apt-get purge -y --auto-remove  -o APT::AutoRemove::RecommendsImportant=false bzip2 \
		&& apt-get clean \
		&& rm -rf /var/lib/apt/lists/* /tmp/*

ENV PATH="$FLEX_HOME/bin:$PATH"

RUN ls -la $FLEX_HOME
RUN mkdir -p /app

WORKDIR /app

ENTRYPOINT []