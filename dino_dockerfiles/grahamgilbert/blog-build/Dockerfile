FROM ruby:2.3-jessie
WORKDIR /tmp/blog
USER root
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV TZ=America/Los_Angeles
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US
RUN git clone https://github.com/grahamgilbert/blog.git /tmp/blog \
    && apt-get -qq update \
    && apt-get install -y locales \
    && echo "en_US UTF-8" > /etc/locale.gen \
    && locale-gen en_US.UTF-8 \
    && apt-get install -y libgsl0ldbl libgsl0-dev \
    && gem install bundler \
    && gem install html-proofer \
    && bundle install