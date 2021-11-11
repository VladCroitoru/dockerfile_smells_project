FROM shsingh/kali-linux-docker
MAINTAINER shain.singh@gmail.com

RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && \
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive

RUN set -x \
    && apt-get -yqq update \
    && apt-get -yqq dist-upgrade \
    && apt-get clean

# install full Kali release
RUN apt-get -y install kali-linux-full

# install custom toolset
RUN apt-get -y install zsh vim git tmux

CMD ["/bin/zsh"]
