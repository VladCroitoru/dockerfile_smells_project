FROM ubuntu:trusty
EXPOSE 4567

RUN apt-get update && \
	apt-get install -yq ruby2.0 ruby2.0-dev pkg-config build-essential nodejs git libxml2-dev libxslt-dev && \
	apt-get autoremove -yq && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*
RUN gem2.0 install --no-ri --no-rdoc bundler
RUN bundle config build.nokogiri --use-system-libraries

ENV SLATE_DIR /slate
RUN mkdir -p "${SLATE_DIR}"

WORKDIR "${SLATE_DIR}"
ADD Gemfile "${SLATE_DIR}"
ADD Gemfile.lock "${SLATE_DIR}"

RUN bundle install

ADD source "${SLATE_DIR}/source"
ADD config.rb "${SLATE_DIR}"
CMD ["bundle", "exec", "middleman", "server", "--force-polling", "-l", "1"]
