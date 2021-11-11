FROM debian:stretch
MAINTAINER Naoaki Obiki
RUN apt-get update && apt-get install -y sudo git
ARG username="9zilla"
ARG password="9zilla"
RUN mkdir /home/$username && useradd -s /bin/bash -d /home/$username $username && echo "$username:$password" | chpasswd && echo ${username}' ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/$username && mkdir -p /home/$username/ci && chown -R $username:$username /home/$username
ENV HOME /home/$username
ENV ANYENV_HOME $HOME/.anyenv
ENV ANYENV_ENV $ANYENV_HOME/envs
RUN git clone "https://github.com/riywo/anyenv" $ANYENV_HOME
RUN echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> /home/$username/.bash_profile && echo 'eval "$(anyenv init -)"' >> /home/$username/.bash_profile
ENV PATH $ANYENV_HOME/bin:$PATH
RUN mkdir $ANYENV_ENV && chown -R $username:$username $ANYENV_HOME
