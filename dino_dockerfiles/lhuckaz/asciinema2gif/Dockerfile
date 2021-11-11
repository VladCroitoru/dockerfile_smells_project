FROM ubuntu

RUN apt-get update

RUN apt-get install gcc g++ make python-setuptools ruby curl git imagemagick gifsicle npm sudo -y

RUN mkdir /home/asciinema

RUN chmod -R 777 /home/asciinema

RUN groupadd -r asciinema && useradd -r -g asciinema asciinema

RUN chown -R asciinema:asciinema /home/asciinema

RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -

RUN apt-get install nodejs -y

ADD ./sudoers /etc/sudoers

RUN chmod 440 /etc/sudoers

RUN locale-gen --purge en_US.UTF-8

RUN echo 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

USER asciinema

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

RUN ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
ENV PATH /home/asciinema/.linuxbrew/bin:$PATH
RUN echo 'export PATH="/home/asciinema/.linuxbrew/bin:$PATH"' >>~/.bash_profile

RUN brew update && brew install asciinema

RUN sudo npm install --global phantomjs2

RUN brew install asciinema2gif

CMD ["bash"]