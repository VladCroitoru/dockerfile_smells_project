FROM ubuntu:14.04
MAINTAINER Haoyang Zeng <haoyangz@mit.edu>

RUN apt-get update
RUN apt-get install -y -q wget build-essential python perl zlib1g-dev autoconf automake libtool ant libexpat1-dev libxml2-dev

RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::PullParser'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::Template'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Simple'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Parser::Expat'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::SOAP11'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::WSDL11'
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::Transport::SOAPHTTP'

RUN mkdir /meme-install/
WORKDIR /meme-install/
RUN wget -q http://meme-suite.org/meme-software/4.10.2/meme_4.10.2.tar.gz && tar zxf meme_4.10.2.tar.gz && cd meme_4.10.2 && \
./configure --prefix=/meme --with-url=http://meme-suite.org --enable-build-libxml2 --enable-build-libxslt && \
make && \
make test && \
make install

ENV PATH /meme/bin:$PATH
RUN chmod -R 777 /meme
