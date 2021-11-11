#GFFcomapre- compare and evaluate the accuracy of RNA-Seq transcript assemblers (Cufflinks, Stringtie)
FROM      ubuntu:14.04.3
MAINTAINER Kapeel Chougule

LABEL Description="GFFcomapre- compare and evaluate the accuracy of RNA-Seq transcript assemblers (Cufflinks, Stringtie)"
RUN apt-get update && apt-get install -y build-essential cmake
#install git
RUN apt-get install --yes git

RUN git clone https://github.com/gpertea/gclib \
&&  git clone https://github.com/gpertea/gffcompare \
&&  cd gffcompare \
&& make release

ENV PATH "/gffcompare:$PATH"
ENTRYPOINT ["gffcompare"]
