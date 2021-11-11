FROM ubuntu:xenial
MAINTAINER Mike Lloyd <mlloyd@pivotal.io>

# update our package repositories and install some needed dependencies.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y ruby \
    curl \
    git \
    php5* \
    python-setuptools \
    scala \
    apt-transport-https \
    build-essential

# add our user.
RUN localedef -i en_US -f UTF-8 en_US.UTF-8 \
	&& useradd -m -s /bin/bash pcfdev \
	&& echo 'pcfdev ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# copy our init scripts.
WORKDIR /home/pcfdev
ADD ["dotnet.sh", "packages.sh", "./setup/"]

# install .net and nuget.
RUN bash setup/dotnet.sh && \
    apt install -y nuget

USER pcfdev
RUN bash setup/packages.sh
ENTRYPOINT ["/bin/bash"]