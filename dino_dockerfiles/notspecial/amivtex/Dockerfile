FROM python:3.7-slim-buster

COPY ./texlive.profile /tmp/install-tl-unx/texlive.profile
COPY ./amivtex /usr/local/texlive/texmf-local/tex/latex/amivtex

# Add texlive directory to the path
ENV PATH /usr/local/texlive/bin/x86_64-linux:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
		perl \
		wget \
        # Xelatex needs libfontconfig
		libfontconfig \
        # Small tools to allow entrypoint to check if fonts are installed
        fontconfig \
	&& \
    rm -rf /var/lib/apt/lists/* && \
    # Download Installer
    wget -O- http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | \
    tar -xz -C /tmp/install-tl-unx --strip-components=1 && \
    # Install basic TeX
    /tmp/install-tl-unx/install-tl \
      --profile=/tmp/install-tl-unx/texlive.profile && \
    # Install xelatex and all required packages
    tlmgr install \
        collection-latex \
        collection-langgerman \
        xetex \
        polyglossia \
        xcolor \
        pgf \
        koma-script \
        titlesec \
        extsizes \
        changepage \
        ms \
        blindtext \
        hyperref \
        zapfding \
        etoolbox \
        # required for iflang
        oberdiek \
    && \
    # Cleanup
    rm -rf /tmp/install-tl-unx && \
    apt-get purge -y --auto-remove \
        perl

# Entrypoint script downloads non-public fonts at container start
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
