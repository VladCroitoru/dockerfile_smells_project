# Dockerfile to build Bio-Linux 8
#
# VERSION 0.1

# use vanilla ubuntu base image
FROM ubuntu

# maintained by me
MAINTAINER Steve Moss <gawbul@gmail.com>

# update aptitude and install some required packages
RUN apt-get update && apt-get -y install build-essential cpanminus curl emacs git manpages perl perl-base perlbrew tmux vim wget

# create ensembl user
RUN useradd -r -m -U -d /home/ensembl -s /bin/bash -c "EnsEMBL User" -p '' ensembl
RUN usermod -a -G sudo ensembl

# turn off password requirement for sudo groups users
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers

# change user to ensembl
USER ensembl

# set HOME environment variable
ENV HOME /home/ensembl

# change working directory
WORKDIR $HOME

# install ensembl dependencies
RUN sudo apt-get -y install mysql-client libmysqlclient-dev libssl-dev
RUN sudo cpanm DBI DBD::mysql
RUN sudo chown -R ensembl:ensembl $HOME/.cpanm

# clone git repositories
RUN mkdir -p src
WORKDIR $HOME/src
RUN git clone https://github.com/bioperl/bioperl-live.git
WORKDIR $HOME/src/bioperl-live
RUN git checkout bioperl-release-1-6-901
WORKDIR $HOME/src
RUN git clone https://github.com/Ensembl/ensembl-git-tools.git
ENV PATH $HOME/src/ensembl-git-tools/bin:$PATH
RUN git ensembl --clone api
RUN git clone https://github.com/Ensembl/ensembl-tools.git

# update bash profile
RUN echo >> $HOME/.profile && \
echo '# set ensembl perl libraries' >> $HOME/.profile && \
echo PERL5LIB=\$PERL5LIB:$HOME/src/bioperl-live >> $HOME/.profile && \
echo PERL5LIB=\$PERL5LIB:$HOME/src/ensembl/modules >> $HOME/.profile && \
echo PERL5LIB=\$PERL5LIB:$HOME/src/ensembl-compara/modules >> $HOME/.profile && \
echo PERL5LIB=\$PERL5LIB:$HOME/src/ensembl-variation/modules >> $HOME/.profile && \
echo PERL5LIB=\$PERL5LIB:$HOME/src/ensembl-funcgen/modules >> $HOME/.profile && \
echo export PERL5LIB >> $HOME/.profile && \
echo >> $HOME/.profile && \
echo '# set ensembl tools in path' >> $HOME/.profile && \
echo PATH=$HOME/src/ensembl-git-tools/bin:\$PATH && \
echo PATH=$HOME/src/ensembl-tools/scripts/assembly_converter:\$PATH >> $HOME/.profile && \
echo PATH=$HOME/src/ensembl-tools/scripts/id_history_converter:\$PATH >> $HOME/.profile && \
echo PATH=$HOME/src/ensembl-tools/scripts/region_reporter:\$PATH >> $HOME/.profile && \
echo PATH=$HOME/src/ensembl-tools/scripts/variant_effect_predictor:\$PATH >> $HOME/.profile && \
echo export PATH >> $HOME/.profile

# setup environment
ENV PERL5LIB $PERL5LIB:$HOME/src/bioperl-live:$HOME/src/ensembl/modules:$HOME/src/ensembl-compara/modules:$HOME/src/ensembl-variation/modules:$HOME/src/ensembl-funcgen/modules
ENV PATH $HOME/src/ensembl-tools/scripts/assembly_converter:$HOME/src/ensembl-tools/scripts/id_history_converter:$HOME/src/ensembl-tools/scripts/region_reporter:$HOME/src/ensembl-tools/scripts/variant_effect_predictor:$PATH

# change working directory
WORKDIR $HOME

# create script to test connection to database
RUN echo '#!/usr/bin/env perl' > ensembl_test_db_conn.pl && \
echo "use strict; use warnings; use Bio::EnsEMBL::Registry; my \$registry = 'Bio::EnsEMBL::Registry'; \$registry->load_registry_from_db(-host => 'ensembldb.ensembl.org', -user => 'anonymous', -verbose => '1');" >> ensembl_test_db_conn.pl
RUN chmod a+x ensembl_test_db_conn.pl