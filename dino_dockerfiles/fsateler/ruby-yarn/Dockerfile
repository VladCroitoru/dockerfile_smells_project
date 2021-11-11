FROM ruby:2.5-slim

# Enable https: instead of git: for github urls
RUN bundle config github.https true

RUN mkdir -p /usr/src/app /usr/src/app/vendor
WORKDIR /usr/src/app

RUN \
	echo 'path-exclude=/usr/share/doc/*' >> /etc/dpkg/dpkg.cfg.d/99-excludes && \
	echo 'path-exclude=/usr/share/man/*' >> /etc/dpkg/dpkg.cfg.d/99-excludes && \
	echo 'path-exclude=/usr/share/locale/*' >> /etc/dpkg/dpkg.cfg.d/99-excludes && \
	echo 'path-include=/usr/share/locale/locale.alias' >> /etc/dpkg/dpkg.cfg.d/99-excludes && \
	echo 'path-include=/usr/share/locale/es*/*' >> /etc/dpkg/dpkg.cfg.d/99-excludes && \
	apt-get update && \
	apt-get install --no-install-recommends -y \
		apt-transport-https \
		systemd \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Repo for Node/Yarn
COPY apt-conf /etc/apt

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		nodejs \
		yarn \
		git \
		build-essential \
		libpq-dev \
		gyp \
		graphicsmagick \
		curl \
		libxrender1 \
		libxext6 \
		libxrender1 \
		libfontconfig1 \
		pdftk \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	curl -L https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz | \
		tar -C /usr/ --strip-components=1 -xvJ && \
	which wkhtmltopdf && wkhtmltopdf --version

