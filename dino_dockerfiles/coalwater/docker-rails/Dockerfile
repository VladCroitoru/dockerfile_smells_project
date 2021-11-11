FROM debian:jessie

# Updating and upgrading the system
RUN apt-get -qq update && apt-get -qqy upgrade && apt-get autoclean

# Installing build essentials curl wget git
RUN apt-get install -qqy build-essential curl wget git && apt-get autoclean

# installing fish shell
RUN echo 'deb http://download.opensuse.org/repositories/shells:/fish:/release:/2/Debian_7.0/ /' >> /etc/apt/sources.list.d/fish.list
RUN curl -Ls http://download.opensuse.org/repositories/shells:fish:release:2/Debian_7.0/Release.key | apt-key add -
RUN apt-get update -qq && apt-get install -qqy fish && apt-get autoclean
RUN chsh -s /usr/bin/fish

# installing ruby install
RUN curl -Ls https://github.com/postmodern/ruby-install/archive/v0.5.0.tar.gz | tar -xz -C /tmp &&\
    make -C /tmp/ruby-install-0.5.0/ install &&\
    rm -rf /tmp/ruby-install-0.5.0

# installing chruby
RUN curl -Ls https://github.com/postmodern/chruby/archive/v0.3.9.tar.gz | tar -xz -C /tmp &&\
    make -C /tmp/chruby-0.3.9/ install &&\
    rm -rf /tmp/chruby-0.3.9

# installing chruby fish
RUN curl -Ls https://github.com/JeanMertz/chruby-fish/archive/v0.6.0.tar.gz | tar -xz -C /tmp &&\
    make -C /tmp/chruby-fish-0.6.0/ install &&\
    rm -rf /tmp/chruby-fish-0.6.0 &&\
    echo 'source /usr/local/share/chruby/chruby.fish' >> /etc/fish/config.fish &&\
    echo 'source /usr/local/share/chruby/auto.fish' >> /etc/fish/config.fish

# Installing ruby dependencies
RUN apt-get install -qqy zlib1g-dev libyaml-dev libssl-dev libgdbm-dev libreadline-dev libncurses5-dev libffi-dev &&\
    apt-get autoclean

# Creating dev user
RUN useradd -m -p dev -s /usr/bin/fish dev


# Installing ruby 2.2.2 under dev user
RUN su -l dev -c 'ruby-install ruby 2.2.2 --no-install-deps' &&\
    su -l dev -c "rm -rf ~/src" &&\
    su -l dev -c "echo '2.2.2' > ~/.ruby-version"

# Installing ruby 2.1.6 under dev user
RUN su -l dev -c 'ruby-install ruby 2.1.6 --no-install-deps' &&\
    su -l dev -c "rm -rf ~/src"

# install mysql and pg developement libs
RUN apt-get install -y libpq-dev libmysqlclient-dev && apt-get autoclean

# expose the rails port
EXPOSE 3000
