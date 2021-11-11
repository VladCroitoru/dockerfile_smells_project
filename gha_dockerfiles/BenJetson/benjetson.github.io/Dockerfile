FROM ruby:2.7

VOLUME /mnt/app
VOLUME /mnt/app/vendor
VOLUME /mnt/app/node_modules

RUN mkdir /buildctx
WORKDIR /buildctx

RUN gem install bundler

RUN apt-get update && apt-get install -y \
	build-essential \
	python3 \
	python3-pip \
	nodejs \
	npm \
	;

# Install shellcheck.
ARG SHCK_VERSION="v0.7.1"
RUN set -e; \
	mkdir -p /tmp/shck_install \
	&& cd /tmp/shck_install \
	&& wget "https://github.com/koalaman/shellcheck/releases/download/${SHCK_VERSION}/shellcheck-${SHCK_VERSION}.linux.x86_64.tar.xz" \
	&& tar --xz -xvf shellcheck-"${SHCK_VERSION}".linux.x86_64.tar.xz \
	&& cp shellcheck-"${SHCK_VERSION}"/shellcheck /usr/bin/ \
	&& shellcheck --version \
	&& rm -rf /tmp/shck_install

# Install eclint.
ARG ECLINT_VERSION="0.3.2"
ARG ECLINT_GITLAB_UPLOAD_TAG="38b6bd1c60e02d07b9c8b83ab115ce52"
RUN set -e; \
	mkdir -p /tmp/eclint_install \
	&& cd /tmp/eclint_install \
	&& wget "https://gitlab.com/greut/eclint/uploads/${ECLINT_GITLAB_UPLOAD_TAG}/eclint_${ECLINT_VERSION}_linux_x86_64.tar.gz" \
	&& tar -xzvf eclint_"${ECLINT_VERSION}"_linux_x86_64.tar.gz \
	&& cp eclint /usr/bin \
	&& eclint --version \
	&& rm -rf /tmp/eclint_install

COPY Gemfile Gemfile.lock ./
RUN bundle install --system

COPY scripts/requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /mnt/app

RUN useradd -m app
USER app
