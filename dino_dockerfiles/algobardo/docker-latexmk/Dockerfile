FROM ubuntu
MAINTAINER algobardo

RUN apt-get update && apt-get install -y build-essential texlive-full texlive-generic-extra texlive-formats-extra texlive-fonts-extra texlive-science latexmk xzdec wget \
  hunspell hunspell-en-us hunspell-da
RUN tlmgr init-usertree && tlmgr update --all && tlmgr install clrscode3e
