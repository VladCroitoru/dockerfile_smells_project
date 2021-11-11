FROM ubuntu:14.04.3
MAINTAINER Bo Gao (bogao@dcs.warwick.ac.uk)
LABEL Description="Image which includes the Perl toolchain (plenv+cpanm+carton)"

ENV PLENV_VERSION	5.18.2

ENV PLENV_ROOT		/root/.plenv
#ENV PATH			$PLENV_ROOT/bin:$PLENV_ROOT/shims:$PATH

RUN apt-get update && apt-get install -y \
	build-essential \
	curl			\
	git 			\
 && apt-get clean

# A. Install the Perl toolchain: plenv -> cpanminus -> carton

# A1. Install plenv
RUN git clone git://github.com/tokuhirom/plenv.git $PLENV_ROOT \
 && git clone git://github.com/tokuhirom/Perl-Build.git $PLENV_ROOT/plugins/perl-build/

#ADD ./plenv.sh /etc/profile.d/plenv.sh
#RUN . /etc/profile

RUN echo 'export PLENV_VERSION='$PLENV_VERSION	>> /etc/profile.d/plenv.sh \
 && echo 'export PLENV_ROOT="'$PLENV_ROOT'"' 	>> /etc/profile.d/plenv.sh \
 && echo 'export PATH="$PLENV_ROOT/bin:$PATH"' 	>> /etc/profile.d/plenv.sh \
 && echo 'eval "$(plenv init -)"' 				>> /etc/profile.d/plenv.sh \
 && . /etc/profile 					\
 && plenv install $PLENV_VERSION 	\
 && plenv rehash 					\
 && plenv global $PLENV_VERSION

RUN cachebuster=b953b35

# A2. Install cpanminus
RUN . /etc/profile \
 && plenv install-cpanm

# A3. Install Carton
RUN . /etc/profile \
 && cpanm Carton

CMD bash -l