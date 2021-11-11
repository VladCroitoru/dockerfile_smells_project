FROM ruby:2.3.1
MAINTAINER manabu.ishii.rb@gmail.com
RUN apt-get update; apt-get install -y graphviz ; apt-get clean
RUN gem install --no-ri --no-rdoc berkshelf -v 5.1.0
RUN mkdir /.berkshelf ; chmod 777 /.berkshelf
RUN echo "[url \"https://\"]\n  insteadOf = git://\n[user]\n  name = Docker Berfkshelf\n  email = docker-berkshelf@example.com" > /.gitconfig ; chmod 666 /.gitconfig
WORKDIR /work
CMD ["berks", "help"]
