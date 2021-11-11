FROM alpine:latest

# install ruby
RUN apk --no-cache add --update linux-headers build-base \
                                openntpd bash curl grep vim wget \
                                ruby-dev ruby ruby-irb \
                                sqlite-dev mysql-dev \
                                ca-certificates \
                                git

# create gemrc file
RUN curl -o ~/.gemrc https://gist.githubusercontent.com/NeMO84/b0ebbda7503d90f768b4/raw/fadaca6438d7cca9ff29bdc18248af364791dee5/.gemrc

# upgrade gem
RUN gem update --system

# install bundler, io-console, bigdecimal
RUN gem install bundler io-console bigdecimal
RUN bundle config --global silence_root_warning 1

# setup up some helpful aliases
RUN echo "alias ls='ls --color=auto'" >> ~/.bashrc
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc
RUN echo "alias grep='/usr/bin/grep --color=auto'" >> ~/.bashrc
RUN echo "alias vi='vim'" >> ~/.bashrc
RUN echo "alias ping='ping -c 5'" >> ~/.bashrc
RUN echo "alias ports='netstat -tulanp'" >> ~/.bashrc
RUN echo "alias rm='rm -i'" >> ~/.bashrc
RUN echo "alias mv='mv -i'" >> ~/.bashrc
RUN echo "alias cp='cp -i'" >> ~/.bashrc
RUN echo "alias ln='ln -v'" >> ~/.bashrc
RUN echo "alias wget='wget -c'" >> ~/.bashrc

CMD ["ruby", "-v"]
