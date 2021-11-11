FROM ubuntu:14.04

WORKDIR /root
ADD setup setup.sh
RUN apt-get update && apt-get install -yqq wget curl git gfortran-4.8 vim g++-4.8 openssl build-essential r-cran-ggplot2 gcc-4.8 libssl-dev protobuf-compiler libprotobuf-dev libapparmor1 psmisc zsh nano

# Install rstudio server
RUN wget https://download2.rstudio.org/rstudio-server-1.1.383-amd64.deb \
	&& dpkg -i rstudio-server-1.1.383-amd64.deb \
	&& apt-get -f install -y \
	&& rm *.deb \
	&& useradd -m rstudio \
	&& echo rstudio:rstudio | chpasswd

# Setting locale
RUN dpkg-reconfigure -f noninteractive locales \
 && /usr/sbin/update-locale \
 && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
 && locale-gen en_US.UTF-8

# Users with other locales should set this in their derivative image
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# oh my zsh setting
RUN wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh \
  && chmod a+x install.sh \
  && bash install.sh \
  && rm install.sh

RUN ./setup.sh && git clone https://github.com/google/rappor.git
WORKDIR rappor
RUN ./build.sh && cp -r analysis apps/rappor-analysis/ && cp -r analysis apps/rappor-sim/ \
	&&cp -r /root/rappor /home/rstudio \
	&& chown -R rstudio:rstudio /home/rstudio \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

ADD run run.sh
VOLUME ["/root/rappor"]
EXPOSE 6788 6789 8787

ENTRYPOINT ["/bin/bash"]
CMD ["./run.sh"]
