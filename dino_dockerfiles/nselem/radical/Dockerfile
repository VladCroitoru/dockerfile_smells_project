# DOCKER-VERSION 0.3.4
FROM perl:5.20

## Installing perl modules for Radical
RUN curl -L http://cpanmin.us | perl - App::cpanminus
RUN cpanm Bio::Perl
RUN cpanm Statistics::Descriptive
RUN cpanm Parallel::ForkManager
RUN cpanm Bio::Phylo
RUN cpanm List::MoreUtils
RUN cpanm Array::Compare
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils --fix-missing \
    git \
    cmake \
    libargtable2-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install unzip

## install RAXML
 RUN wget https://github.com/stamatak/standard-RAxML/archive/v8.0.0.zip \
 && unzip v8.0.0.zip \
 && rm -rf v8.0.0.zip 
# # Compile RAxML # See https://github.com/stamatak/standard-RAxML #  RUN cd standard-RAxML-8.0.0; \
RUN cd standard-RAxML-8.0.0; \
  make -f Makefile.gcc; rm *.o; \
  mv raxmlHPC /usr/local/bin/

###____________________________________________
##install radical
## Download radical
RUN if [ ! -d /opt ]; then mkdir /opt; fi
#RUN wget -O /opt/radical-0.2.tar.gz http://desalle.amnh.org/radical-0.2.tar.gz \
RUN git clone https://github.com/nselem/radical 
# && cd /opt/radical/quicktree_1.1 && make quicktree

#Esta parte no es necesario, cuando se instala radical el proceso se detiene hasta aqui porque da error, ya que estas ubicaciones no existen
#RUN mv /usr/local/lib/perl5/site_perl/5.20.3/x86_64-linux/List/ /usr/local/lib/perl5/site_perl/5.20.3/

## install vim 
RUN apt-get install -y vim
## install R
RUN apt-get install -y r-base

## edit path
## edit PERL5
ENV PATH=$PATH:/root/radical/radical-0.2/bin
ENV PERL5LIB=$PERL5LIB:/root/radical/radical-0.2/lib:/usr/local/lib/perl5/site_perl/5.20.2/:/usr/local/lib/perl5/5.20.2/x86_64-linux/:/usr/local/lib/perl5/site_perl/5.20.2/x86_64-linux/:/usr/share/perl5/local/:/usr/local/lib/x86_64-linux-gnu/perl/5.20.2/:/usr/local/lib/x86_64-linux-gnu/perl/5.20.2/auto/:/usr/local/share/perl/5.20.2/x86_64-linux-gnu-thread-multi/:/usr/local/share/perl/5.20.2/:/usr/local/lib/perl5/site_perl/5.20.3/:/usr/local/lib/perl5/site_perl/5.20.3/x86_64-linux/List/:/usr/local/lib/perl5/site_perl/5.20.3/x86_64-linux/auto/

RUN apt-get update
#RUN apt-get install vim

#ENV PATH /opt/blast/bin:$PATH:
WORKDIR /usr/src/radical 

##Useful to convert partition nexus file
#http://gaurav.github.io/taxondna/
