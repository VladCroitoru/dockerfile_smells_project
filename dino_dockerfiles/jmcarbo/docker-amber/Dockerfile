FROM ubuntu
RUN apt-get update
RUN apt-get install -y build-essential libreadline-dev libsqlite3-dev libpq-dev libmysqlclient-dev libssl-dev libyaml-dev curl git apt-transport-https tmux vim
RUN curl https://dist.crystal-lang.org/apt/setup.sh | bash
RUN apt-get update
RUN apt-get install -y crystal
RUN curl -L https://github.com/amberframework/amber/archive/stable.tar.gz | tar xz
RUN cd amber-stable && shards install && make && install bin/amber /usr/local/bin/amber
