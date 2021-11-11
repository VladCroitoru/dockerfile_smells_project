FROM base/archlinux
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

RUN pacman -Sy --noconfirm base-devel ruby

# TODO: don't hardcode ruby version
# RUN ruby -e 'print Gem.user_dir'
# RUN echo $PATH
ENV PATH /root/.gem/ruby/2.5.0/bin:$PATH

RUN gem install bundler

RUN pacman -S --noconfirm python2 python2-pip
RUN pip2 install pygments

RUN mkdir site
WORKDIR site
COPY ./ ./

RUN bundle install

EXPOSE 3000
CMD ["jekyll", "serve", "--host=0.0.0.0"]
