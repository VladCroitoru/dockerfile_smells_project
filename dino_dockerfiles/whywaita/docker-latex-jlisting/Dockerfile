FROM debian:jessie
MAINTAINER whywaita <dev@whywrite.it>

ENV LANG en_US.UTF-8

# Setup and Install
#   * texlive-*: for LaTeX
#   * zip: for review-epubmaker
#   * curl & bzip2: for installing jlisting.sty
#   * ruby & ruby-pygments.rb: for review
#   * rake & git: for specific_install
#   * imagemagick: convert images
RUN apt-get update \
	  && apt-get install -y locales \
	  && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
	  && locale-gen en_US.UTF-8 \
	  && update-locale en_US.UTF-8 \
	  && apt-get install -y \
		     texlive-lang-cjk \
		     texlive-fonts-recommended \
		     curl \
		     bzip2 \
		     git \
		     imagemagick \
         ruby \
         rake
RUN	apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# Install jlisting.sty
RUN mkdir -p /usr/share/texlive/texmf-dist/tex/latex/jlisting && \
	  curl http://iij.dl.sourceforge.jp/mytexpert/26068/jlisting.sty.bz2 | \
		bunzip2 > /usr/share/texlive/texmf-dist/tex/latex/jlisting/jlisting.sty && \
	  mktexlsr

ADD spec.sh /tmp/spec.sh
RUN chmod 755 /tmp/spec.sh
