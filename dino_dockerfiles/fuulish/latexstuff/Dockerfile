FROM debian:testing
#FROM debian:jessie

#RUN apt-get update && apt-get install -my texlive-full git latexdiff

RUN apt-get update && apt-get install -my texlive texlive-extra-utils git python wget perl xzdec make asciidoc latexdiff texlive-binaries bibtool

#RUN tlmgr init-usertree ; exit 0
#RUN tlmgr update --all && tlmgr install texliveonfly

#RUN apt-get update && apt-get install -y python wget perl git
#RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && tar -xzf install-tl-unx.tar.gz && cd install-tl-* && echo I | ./install-tl && tlmgr install texliveonfly

RUN git clone https://gitlab.com/git-latexdiff/git-latexdiff.git git-latexdiff.git && cd git-latexdiff.git && make install
