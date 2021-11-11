FROM mterron/consul
MAINTAINER Miguel Terron <miguel.a.terron@gmail.com>

ARG BUILD_DATE
ARG	VCS_REF
ARG	HASHICORP_PGP_KEY=51852D87348FFC4C
ARG	VAULT_VERSION=1.0.1

LABEL maintainer="Miguel Terron <miguel.a.terron@gmail.com>" \
	  org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/mterron/vault.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc.1" \
      org.label-schema.version=$VAULT_VERSION \
      org.label-schema.description="Vault secure production ready Docker image"

USER root
WORKDIR /tmp
RUN	apk -q --no-cache add binutils ca-certificates gnupg wget libcap &&\
# Download Vault binary & integrity file
	gpg --keyserver hkps://hkps.pool.sks-keyservers.net:443 --receive-keys "$HASHICORP_PGP_KEY" &&\
	wget -nv --progress=bar:force --show-progress https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip &&\
	wget -nv --progress=bar:force --show-progress https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS &&\
	wget -nv --progress=bar:force --show-progress https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_SHA256SUMS.sig &&\
# Install Vault
	gpg --batch --verify vault_${VAULT_VERSION}_SHA256SUMS.sig vault_${VAULT_VERSION}_SHA256SUMS &&\
	grep "linux_amd64.zip" vault_${VAULT_VERSION}_SHA256SUMS | sha256sum -sc &&\
	unzip -q -o vault_${VAULT_VERSION}_linux_amd64.zip -d /usr/local/bin/ &&\
	strip --strip-debug /usr/local/bin/vault &&\
	setcap 'cap_ipc_lock=+ep' /usr/local/bin/vault &&\
# Create Vault user & group and add root to the vault group
	adduser -u 100001 -g 'Vault user' -s /dev/null -D vault &&\
	addgroup vault consul &&\
# Cleanup
	apk -q --no-cache del --purge binutils ca-certificates gnupg wget libcap &&\
	rm -rf vault_${VAULT_VERSION}_* /root/.gnupg

# Add Containerpilot
ARG	CONTAINERPILOT_VERSION=3.8.0
RUN	echo -n -e "\e[0;32m- Install Containerpilot\e[0m" &&\
	apk -q --no-cache add binutils &&\
	curl -sSL "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz" | tar xzf - -C /usr/local/bin &&\
	strip --strip-debug /usr/local/bin/containerpilot &&\
	# Vault health check
	echo -e '#!/bin/sh\nif curl -kisSfi1 --head https://127.0.0.1:8200/v1/sys/health?standbycode=204 &>/dev/null; then\n\texit 0\nelse\n\texit 1\nfi' > /usr/local/bin/vault-healthcheck &&\
	# Consul health check
	echo -e "#!/bin/sh\nsu-exec consul curl -s --unix-socket /run/consul/consul.http.sock http://consul/v1/status/leader | jq -cre 'if . != \"\" then true else false end'>/dev/null || exit 1"> /usr/local/bin/consul-healthcheck &&\
	chown root:root /usr/local/bin/containerpilot /usr/local/bin/*-healthcheck &&\
	chmod +x /usr/local/bin/containerpilot /usr/local/bin/*-healthcheck &&\
	apk -q --no-cache del --purge binutils &&\
	echo -e "\e[1;32m  ✔\e[0m"

# Copy scripts
COPY bin/* /usr/local/bin/
# Copy Containerpilot config
COPY containerpilot.json5 /etc/

EXPOSE 8200

HEALTHCHECK --start-period=600s CMD set -e && set -o pipefail && vault status -format=json | jq -ce '.sealed == false'

ENTRYPOINT ["containerpilot", "-config", "/etc/containerpilot.json5"]
COPY Dockerfile /etc/
