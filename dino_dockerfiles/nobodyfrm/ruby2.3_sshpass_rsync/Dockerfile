FROM ruby:2.3

RUN apt-get update && apt-get install -y  sshpass rsync locales && rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 && export LANG=en_US.UTF-8 && export LC_ALL=en_US.UTF-8

RUN gem install html-proofer kwalify bundler --pre
RUN echo "source 'https://rubygems.org' \n\
    gem 'wdm', '>= 0.1.0' if RbConfig::CONFIG['target_os'] =~ /mswin|mingw|cygwin/i \n\
    gem 'middleman', '~> 4.1.6' \n\
    gem 'therubyracer' \n\
     \n\
    group :unix do \n\
        gem 'rb-inotify' \n\
    end \n\
    \n\
    gem 'uglifier' \n\
    gem 'middleman-minify-html' \n\
    gem 'middleman-livereload' \n\
    gem 'listen' \n\
    gem 'middleman-search'" > Gemfile

RUN ls -la
RUN cat Gemfile
RUN bundle install
