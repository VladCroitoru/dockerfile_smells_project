FROM dalibo/pandocker

RUN tlmgr update --self && tlmgr init-usertree ; tlmgr install \
      moderncv \
      etoolbox \
      fontawesome && \
  wget -O fonts.zip "https://fonts.google.com/download?family=Roboto|Noto%20Sans|Open%20Sans|Roboto%20Condensed|Source%20Sans%20Pro|Raleway|Merriweather|Roboto%20Slab|PT%20Sans|Open%20Sans%20Condensed|Droid%20Sans|Droid%20Serif|Fira%20Sans|Fira%20Sans%20Condensed|Fira%20Sans%20Extra%20Condensed|Fira%20Mono"  && \
  wget -O firacode.zip "https://github.com/tonsky/FiraCode/releases/download/1.204/FiraCode_1.204.zip" && \
  unzip fonts.zip -d ~/.fonts && \
  unzip firacode.zip -d ~/.fonts && \
  fc-cache -v -f && \
  rm -rf fonts.zip firacode.zip

ENTRYPOINT ["pandoc"]

CMD ["--help"]
