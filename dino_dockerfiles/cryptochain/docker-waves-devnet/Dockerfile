FROM anapsix/alpine-java:8_server-jre

MAINTAINER Dmitry Ananichev <a@qozz.ru>

EXPOSE 6863 6869

RUN mkdir /waves /conf /data

VOLUME ["/data"]

VOLUME ["/conf"]

WORKDIR /waves

ADD docker-entrypoint.sh /waves/docker-entrypoint.sh

RUN chmod -v +x docker-entrypoint.sh

RUN apk add --no-cache curl jq openssl

RUN ver=$(curl https://api.github.com/repos/wavesplatform/Waves/releases | jq --arg version "$version" '[.[] | {tag: .tag_name, name: .name, assets: [.assets[].browser_download_url]} | select(.name | startswith("Testnet")) | select(.name | endswith($version)), select(.name == .tag)] | .[0] | .tag') && \
	ver="${ver%\"}" && ver="${ver#\"}" && \
	wget -P /waves -O waves.conf https://raw.githubusercontent.com/wavesplatform/Waves/$ver/waves-testnet.conf

RUN sed -i "s|directory = .*|directory = \"/data\"|g" /waves/waves.conf

RUN curl https://api.github.com/repos/wavesplatform/Waves/releases | jq --arg version "$version" '[.[] | {tag: .tag_name, name: .name, assets: [.assets[].browser_download_url]} | select(.name | startswith("Testnet")) | select(.name | endswith($version)), select(.name == .tag)] | .[0] | [.assets] | flatten | .[] | select(. | endswith(".jar"))' | xargs wget -P /waves -O waves.jar

ENTRYPOINT ["/waves/docker-entrypoint.sh"]
