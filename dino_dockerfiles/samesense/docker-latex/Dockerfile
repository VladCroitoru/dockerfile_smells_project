FROM blang/latex
MAINTAINER Perry Evans <@oncolytic>

ADD latexmk.pl /usr/bin/latexmk
RUN chmod +x /usr/bin/latexmk

ADD build /usr/bin/build
RUN chmod +x /usr/bin/build

ADD autobuild /usr/bin/autobuild
RUN chmod +x /usr/bin/autobuild

ADD clean /usr/bin/clean
RUN chmod +x /usr/bin/clean

ENV TEXMFHOME /root/texmf
ADD cls /root/texmf

RUN texhash
RUN mktexlsr /root/texmf

VOLUME /latex
WORKDIR /latex
