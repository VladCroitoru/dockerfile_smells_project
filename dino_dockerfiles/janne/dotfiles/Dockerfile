FROM ubuntu

# Refresh dpkg
ENV REFRESHED_AT 2017-10-22
RUN apt-get -qq update

# Deps
RUN apt-get install -y \
    build-essential \
    bash-completion \
    curl \
    screen \
    vim \
    git \
    ruby-full \
    python \
    sudo

# Nodejs
ENV NPM_CONFIG_PREFIX /usr/local
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# Add dotfiles
ADD . /etc/skel/

# Add user
ENV USERNAME user
RUN adduser --disabled-password --gecos '' $USERNAME
RUN chown -R $USERNAME:$USERNAME /usr/local
RUN echo "$USERNAME ALL=NOPASSWD:ALL" >> /etc/sudoers
USER $USERNAME
WORKDIR /home/$USERNAME

CMD ["/bin/bash"]
