FROM dhspence/docker-baseimage

# File Author / Maintainer
MAINTAINER David Spencer <dspencer@wustl.edu>

COPY GeneralAlignment.sh /usr/local/bin/

RUN chmod a+x /usr/local/bin/GeneralAlignment.sh

##############
# STAR
##############
WORKDIR /usr/local/
RUN pwd
RUN git clone https://github.com/alexdobin/STAR.git
WORKDIR /usr/local/STAR/
RUN pwd
RUN git checkout 2.5.3a 
WORKDIR /usr/local/STAR/source 
RUN pwd
RUN make STAR
ENV PATH /usr/local/STAR/source:$PATH
WORKDIR /

RUN cpan install DB_File && \
   cpan install URI::Escape && \
   cpan install Set::IntervalTree && \
   cpan install Carp::Assert && \
   cpan install JSON::XS && \
   cpan install PerlIO::gzip

WORKDIR /usr/local/
RUN git clone --recursive https://github.com/STAR-Fusion/STAR-Fusion.git

RUN ln -s /usr/local/STAR-Fusion/STAR-Fusion /usr/local/bin/

