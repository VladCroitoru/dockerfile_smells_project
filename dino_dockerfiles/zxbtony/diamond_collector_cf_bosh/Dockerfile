FROM ruby:2.2-alpine

ENV CF_CLI_VERSION "6.23.1"
ENV CF_BGD_VERSION "1.1.0"
ENV CF_BGD_CHECKSUM "fe6ebd3c2dc3a287db0d31eeaed200d1a27117d9a6ddd875de561e4a6e8858d1"
ENV CF_BGD_TEMPFILE "/tmp/blue-green-deploy.linux64"


RUN gem install bosh_cli -v 1.3232.0 --no-rdoc --no-ri

RUN apk add --update \
	bash \
	openssl \
	openssh-client \
	file \
  gcc \
	python \
	python-dev \
	py-pip \
  py-psutil \
	git \
	curl \
	ca-certificates \
	ruby-json \
	unzip \
	libc6-compat && \
	rm -rf /var/cache/apk/* && \
	pip install diamond
RUN ln -s /lib/ /lib64

COPY ./collectors /collectors
COPY init.py /init.py
COPY run.sh /run.sh

RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&version=${CF_CLI_VERSION}" | tar -zx -C /usr/local/bin
RUN curl -L 'https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64' -o /usr/local/bin/jq && chmod +x /usr/local/bin/jq
RUN curl -L -o "${CF_BGD_TEMPFILE}" \
  "https://github.com/bluemixgaragelondon/cf-blue-green-deploy/releases/download/v${CF_BGD_VERSION}/blue-green-deploy.linux64" \
  && echo "${CF_BGD_CHECKSUM}  ${CF_BGD_TEMPFILE}" | sha256sum -c - \
  && chmod +x "${CF_BGD_TEMPFILE}" \
  && cf install-plugin -f "${CF_BGD_TEMPFILE}" \
  && rm "${CF_BGD_TEMPFILE}" \
  && chmod +x /run.sh

ENTRYPOINT ["/run.sh"]

