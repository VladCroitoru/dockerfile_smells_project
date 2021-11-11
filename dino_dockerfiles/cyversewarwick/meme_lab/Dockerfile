#base on a prior MEME install
FROM cyversewarwick/hmt_index:latest

#pick up a few new packages
RUN apt-get update && apt-get -y upgrade && apt-get -y install libpng-dev libgd-dev

#glue over the scripts. need them early as GD installation hedges on one because reasons
COPY scripts /scripts

#CPAN time
RUN cpan MooseX:Declare
#BioPerl is also a primadonna and refuses to cpan its way to glory because reasons
RUN apt-get -y install bioperl

#the GD Perl package refuses to be cpanned, and the commands refuse to work in a Dockerfile
RUN mkdir gd && cd gd && bash /scripts/install_GD.sh

#analysis crash text file set up in the base HMT_index container already

#...I think that's it?
ENTRYPOINT ["bash", "/scripts/meme_lab_tarwrapper.sh"]