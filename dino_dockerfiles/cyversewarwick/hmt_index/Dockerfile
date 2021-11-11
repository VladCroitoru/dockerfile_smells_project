# run as (with code in folder):
#	docker build -t hmt-index .

# base everything on a recent Ubuntu
FROM debian:latest

# get system packages up to date
RUN apt-get update && apt-get -y upgrade

# I have no idea why this is needed. a C compiler seems basic.
RUN apt-get -y install build-essential

# good old wget
RUN apt-get -y install wget

# making .genome files needs this
RUN wget -P /bin/ http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/fetchChromSizes

# digging out the promoter needs this
RUN apt-get install bedtools

# FIMO lives in here, as does the background generator
# zlib is needed for MEME
RUN apt-get install -y zlibc zlib1g zlib1g-dev
# Sam lied, there is no python. there is no future.
RUN apt-get -y install python
# some perl stuff is needed as well
RUN apt-get install libexpat1-dev && \
 apt-get -y install libxml2-dev
RUN cpan HTML::PullParser && \
 cpan HTML::Template && \
 cpan XML::Simple && \
 cpan XML::Parser::Expat && \
 cpan Devel::CheckLib

# apparently this magically fixes all of the things
RUN apt-get -y install libxml-libxml-perl

# back to simple shit hopefully
RUN cpan XML::Compile && \
 cpan XML::Compile::Cache && \
 cpan XML::Compile::SOAP11 && \
 cpan XML::Compile::WSDL11 && \
 cpan XML::Compile::Transport::SOAPHTTP && \
 cpan Log::Log4perl && \
 cpan Math::CDF
# finally meme proper
RUN wget http://meme-suite.org/meme-software/4.10.2/meme_4.10.2.tar.gz
RUN tar zxf meme_4.10.2.tar.gz && cd meme_4.10.2 && \
 ./configure --prefix=$HOME/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt && \
  make && make test && make install

#the fetchChromSizes thing is useless. samtools is go
RUN apt-get -y install samtools

#need ImageMagick for PNG conversion
RUN apt-get -y install imagemagick

# okay. so, now we can do code things. like set up python3
RUN apt-get -y install python3 python3-dev python3-setuptools \
         python3-numpy python3-scipy
# need a new version of pandas for comment='#' functionality
RUN easy_install3 pip && pip install pandas

# glue over the code
RUN mkdir /scripts
COPY scripts /scripts/

#set up analysis crash text file
RUN apt-get -y install git
RUN git clone https://github.com/cyversewarwick/analysis_crash.git

# ...I think that's it for now?
ENTRYPOINT ["bash", "/scripts/hmt_index_tarwrapper.sh"]