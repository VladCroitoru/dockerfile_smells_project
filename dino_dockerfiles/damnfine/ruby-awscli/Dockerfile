FROM circleci/ruby:2.3-node

# downgrade to Node v6.8.0
RUN sudo npm cache clean -f
RUN sudo npm install -g n
RUN sudo n 6.8.0

# install python and pip
RUN sudo apt-get update
RUN sudo apt-get install -y python-dev python-pip libpython-dev

# install aws cli
RUN pip install awscli --user --upgrade
ENV PATH "$PATH:~/.local/bin"

RUN gem update --system --no-rdoc --no-ri -- --use-system-libraries
RUN gem install bundler -v 1.13.3 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman -v 3.4.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman-autoprefixer -v 2.7.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman-blog -v 3.5.3 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman-livereload -v 3.3.4 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman-imageoptim -v 0.2.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman-pagination -v 1.2.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install middleman-search -v 0.8.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install json -v 1.8.3 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install minitest -v 5.9.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install thread_safe -v 0.3.5 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install tzinfo -v 1.2.2 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install activesupport -v 4.2.7.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install autoprefixer-rails -v 6.5.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install mini_portile2 -v 2.1.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install nokogiri -v 1.6.8.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install rack -v 1.6.4 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install rack-test -v 0.6.3 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install xpath -v 2.0.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install chunky_png -v 1.3.7 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install coffee-script-source -v 1.10.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install multi_json -v 1.12.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install sass -v 3.4.22 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install rb-fsevent -v 0.9.7 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install ffi -v 1.9.14 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install rb-inotify -v 0.9.7 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install eventmachine -v 1.2.0.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install exifr -v 1.2.5 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install haml -v 4.0.7 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install hashery -v 2.1.2 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install image_size -v 1.4.2 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install in_threads -v 1.3.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install progress -v 3.2.2 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install kramdown -v 1.12.0 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install libv8 -v 3.16.14.15 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install thor -v 0.19.1 --no-rdoc --no-ri -- --use-system-libraries
RUN gem install therubyracer -v 0.12.2 --no-rdoc --no-ri -- --use-system-libraries