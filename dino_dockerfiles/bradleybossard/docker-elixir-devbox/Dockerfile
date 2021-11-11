FROM bradleybossard/docker-common-devbox
MAINTAINER Bradley Bossard <bradleybossard@gmail.com>

# Build the image
# docker build --rm -t docker-elixir-devbox .

# Fire up an instance with a bash shell and mount the current directory on /src
# docker run -i -t --rm -v $PWD:/src bradleybossard/docker-elixir-devbox

RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb
RUN apt-get update

RUN apt-get install -y elixir

