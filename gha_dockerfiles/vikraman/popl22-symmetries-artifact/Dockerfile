FROM   haskell:8.10.4-buster
LABEL  authors="Jacek Karwowski, Vikraman Choudhury"

RUN stack --resolver lts-17.15 --system-ghc install Agda-2.6.1.3

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y emacs-nox cloc && rm -rf /var/lib/apt/lists/*

COPY vendor/dot-emacs /root/.emacs
COPY vendor/agda-libraries /root/.agda/libraries
COPY vendor/agda-defaults /root/.agda/defaults

VOLUME   /artifact/
COPY   . /artifact/
WORKDIR  /artifact/

RUN make
