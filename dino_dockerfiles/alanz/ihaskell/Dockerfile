# set up an IHaskell instance
#
# build with
#  docker build -t 'alanz/IHaskell' .
# run with
# docker run -P -d 'alanz/IHaskell'
# docker run -p 2222:22 -p 8778:8778 -d 'alanz/IHaskell'

# ssh-keygen -t rsa
# Call it ./docker_unsecure_id_rsa, no passphrase

FROM alanz/haskell-platform-2013.2-deb64

MAINTAINER alan.zimm@gmail.com

ENV DEBIAN_FRONTEND noninteractive

#-----------------------------------------------------------------------
# Install emacs and ssh server
RUN echo "deb http://cdn.debian.net/debian/ testing main non-free contrib" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y dist-upgrade

RUN apt-get -y install python-dev
RUN apt-get -y install automake
RUN apt-get -y install libtool
RUN apt-get -y install g++
RUN apt-get -y install libtinfo-dev libncurses5-dev
RUN apt-get -y install sudo


RUN wget https://github.com/zeromq/zeromq4-x/archive/v4.0.3.tar.gz
RUN tar xvfz v4.0.3.tar.gz

RUN cd zeromq4-x-4.0.3 && ./autogen.sh
RUN cd zeromq4-x-4.0.3 && ./configure
RUN cd zeromq4-x-4.0.3 && make
RUN cd zeromq4-x-4.0.3 && make install


# Dependencies for the ihaskell stuff
RUN apt-get -y install libgtk2.0-dev libgtk-3-dev
RUN apt-get -y install libmagic-dev

# For the ssh server
RUN apt-get -y install ssh openssh-server ssh


#-----------------------------------------------------------------------

#ADD . /src

#RUN /src/setup.sh

#DOCKER_PASSWORD=password
#echo User: docker Password: $DOCKER_PASSWORD
#DOCKER_ENCRYPYTED_PASSWORD=`perl -e 'print crypt('"$DOCKER_PASSWORD"', "aa"),"\n"'`
# result of above is aajfMKNH1hTm2
#useradd -m -d /home/docker -p $DOCKER_ENCRYPYTED_PASSWORD docker
RUN useradd -m -d /home/docker -p 'aajfMKNH1hTm2' docker
#RUN useradd -m -d /home/docker docker
RUN sed -Ei 's/adm:x:4:/docker:x:4:docker/' /etc/group
RUN adduser docker sudo

# Set the default shell as bash for docker user.
RUN chsh -s /bin/bash docker

#-----------------------------------------------------------------------

RUN sudo -u docker echo "export PATH=~/.cabal/bin:$PATH" >> ~/.bashrc

RUN sudo -u docker cabal update

RUN sudo -u docker cabal install cabal-install
RUN sudo -u docker cabal install happy cpphs

# RUN sudo -u docker cabal install zeromq4-haskell

RUN sudo -u docker cabal install ipython-kernel
RUN sudo -u docker cabal install ghci-lib
RUN sudo -u docker cabal install haskell-src-exts
RUN sudo -u docker cabal install ghc-parser
RUN sudo -u docker cabal install tar
RUN sudo -u docker cabal install hlint
RUN sudo -u docker cabal install haskell-src-meta
RUN sudo -u docker cabal install haskeline
RUN sudo -u docker cabal install hspec
RUN sudo -u docker cabal install shelly
RUN sudo -u docker cabal install classy-prelude-0.7.0

# RUN echo "export PATH=~/.cabal/bin:$PATH" >> /etc/profile
RUN sudo -i -u docker bash -c 'export PATH=~/.cabal/bin:$PATH && cabal install ihaskell'

# RUN sudo -u docker cabal install ihaskell
RUN sudo -u docker cabal install ihaskell-aeson
RUN sudo -u docker cabal install ihaskell-blaze
RUN sudo -u docker cabal install gtk2hs-buildtools
RUN sudo -i -u docker bash -c 'export PATH=~/.cabal/bin:$PATH && cabal install cairo'
RUN sudo -i -u docker bash -c 'export PATH=~/.cabal/bin:$PATH && cabal install ihaskell-charts'
RUN sudo -u docker cabal install ihaskell-diagrams
RUN sudo -u docker cabal install ihaskell-display
RUN sudo -u docker cabal install ihaskell-magic

#-----------------------------------------------------------------------
# Set up IHaskell surrounding environment

RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y install git

RUN sudo -i -u docker bash -c 'echo "export PATH=~/.cabal/bin:$PATH" >> ~/.bashrc'

# Get IHaskell initial run to download/install environment
RUN sudo -i -u docker bash -c 'echo "exit" > foo'
RUN sudo -i -u docker bash -c 'export PATH=~/.cabal/bin:$PATH && IHaskell console < foo'

# for debugging
# RUN apt-get -y install iceweasel
# RUN apt-get -y install libparse-netstat-perl libnet-ifconfig-wrapper-perl
# RUN apt-get -y install emacs

# Make sure it listens on all interfaces
RUN sudo -i -u docker bash -c 'echo "c.NotebookApp.ip = \"0.0.0.0\"" >> ~/.ipython/profile_haskell/ipython_notebook_config.py'

# Populate with sample notebooks
ADD ./notebooks/ /home/docker/.ihaskell/notebooks/


# expose the docker port
EXPOSE 8778

#-----------------------------------------------------------------------

# Set up sshd directory
RUN mkdir /var/run/sshd

# Expose the ssh port
EXPOSE 22
# Start shell and ssh services.
#CMD ["/usr/sbin/sshd", "-D"]

ADD ./docker/run.sh /home/docker/run.sh

ENV PATH /home/docker/.cabal/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
USER docker
CMD ["bash","/home/docker/run.sh"]
#CMD ["IHaskell","notebook"]


