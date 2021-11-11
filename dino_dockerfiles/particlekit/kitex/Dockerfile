FROM opensuse/leap:15.0


RUN zypper --non-interactive in --auto-agree-with-licenses --no-recommends \ 
              make unzip \
              patterns-openSUSE-technical_writing \
              texlive-bbm \
              texlive-collection-bibtexextra \
              texlive-collection-binextra \
              texlive-collection-context \
              texlive-collection-fontsrecommended \
              texlive-collection-fontutils \
              texlive-collection-langeuropean \
              texlive-collection-langgerman \
              texlive-collection-latexextra \
              texlive-collection-metapost \
              texlive-collection-pstricks \
              texlive-collection-publishers \
              texlive-collection-mathscience \
              texlive-luatex \
              texlive-luatextra \
              texlive-plain \
              texlive-collection-xetex \
              texlive-inconsolata \
              texlive-metapost \
              texlive-tools \
              texlive-sourcesanspro \
              texlive-newtx \
              texlive-libertine \
              texlive-boondox \
              zypper clean --all

ADD getnonfreefonts-sys /usr/local/bin/
ADD tex /usr/share/texmf/tex

RUN export TEXMFLOCAL=/usr/share/texmf/ && export TEXMFHOME=/usr/share/texmf/ &&\
    chmod 755 /usr/local/bin/getnonfreefonts-sys &&\
    chgrp -R mktex /usr/share/texmf/ &&\
    /usr/local/bin/getnonfreefonts-sys -a &&\
    echo y | /usr/bin/updmap-sys --syncwithtrees --outputdir /usr/share/texmf/  &&\
    /usr/local/bin/getnonfreefonts-sys -r &&\
    mkdir /cache

WORKDIR /cache
VOLUME ["/cache"]

