FROM node:0.12
MAINTAINER JuanPabloAJ <jpabloaj@gmail.com>

WORKDIR /tmp

# install python3.4
RUN apt-get update && apt-get install -y python3.4

# "warning: the VM is running with native name encoding of latin1
# which may cause Elixir to malfunction as it expects utf8."
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && sed -i 's/^# \(en_US.UTF-8 UTF-8\)/\1/' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8

# install elixir
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \
    dpkg -i erlang-solutions_1.0_all.deb && \
    apt-get update && apt-get install -y elixir

ADD . /app
WORKDIR /app

RUN npm install

CMD ["node", "server.js"]
