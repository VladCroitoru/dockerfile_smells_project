# 
#

FROM ruby:2.3
MAINTAINER damien clochard <damien.clochard@dalibo.com>

RUN apt-get -qq update \
 && apt-get -qq -y install locales \
                           wget unzip \
                           rsync openssh-client \ 
    # clean up
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set the locale
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR:fr
ENV LC_ALL fr_FR.UTF-8
RUN echo "${LANG} UTF-8" > /etc/locale.gen
RUN locale-gen

# Install jekyll with bundler 
ADD Gemfile .
RUN bundle install

# html5_lint
RUN wget -O master.zip https://github.com/mozilla/html5-lint/archive/v0.3.0.zip \
 && unzip master.zip \
 && mv html5-lint-0.3.0/html5check.py /usr/local/bin

