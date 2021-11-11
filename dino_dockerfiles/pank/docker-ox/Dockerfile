FROM debian:testing-slim
LABEL maintainer "Rasmus <docker@pank.eu>"
LABEL version="0.9.2"

ENV DEBIAN_FRONTEND noninteractive
# Install Emacs plus TeX and friends for Org-mode
RUN apt-get update                                                        \
  && apt-get install --yes --no-install-recommends apt-utils              \
  && apt-get install --yes --no-install-recommends                        \
      make                                                                \
      wget                                                                \
      emacs-nox                                                           \
      ca-certificates                                                     \
      texlive-latex-base                                                  \
      texlive-plain-generic                                               \
      texlive-lang-english                                                \
      texlive-lang-european                                               \
      texlive-lang-german                                                 \
      texlive-latex-extra                                                 \
      texlive-bibtex-extra                                                \
      biber                                                               \
      fontconfig                                                          \
      texlive-luatex                                                      \
      texlive-xetex                                                       \
   && apt-get install --yes texlive-fonts-extra texlive-fonts-recommended \
   && apt-get autoclean                                                   \
   && apt-get --purge --yes autoremove                                    \
   && apt-get clean                                                       \
   && cd /tmp                                                             \
   && wget https://code.orgmode.org/bzg/org-mode/archive/master.tar.gz    \
   && tar xfz master.tar.gz                                               \
   && cd org-mode                                                         \
   && make autoloads                                                      \
   && cp -r lisp /usr/share/emacs/site-lisp/org                           \
   && cp -r contrib/lisp/ /usr/share/emacs/site-lisp/org_contrib          \
   && rm -rf /var/lib/apt/lists/*                                         \
   && rm -rf /var/cache/*                                                 \
   && rm -rf /tmp/*                                                       \
   && rm -rf /var/tmp/*                                                   \
   && rm -rf /usr/share/doc                                               \
   && rm -rf /usr/share/man                                               \
   && rm -rf /usr/share/locale

# Export the output data
WORKDIR /data
VOLUME ["/data"]
