FROM fedora:27

# Need to upgrade, because of some problems with pip.
RUN dnf -y upgrade --refresh && \
    dnf -y install 'dnf-command(copr)' && \
    dnf -y copr enable petersen/pandoc && \
    dnf -y install \
        graphviz \
        pandoc \
        pandoc-citeproc \
        texlive-cm \
        texlive-euenc \
        texlive-hyphen-base \
        texlive-latex \
        texlive-lm-math \
        texlive-tex-ini-files \
        texlive-unicode-data \
        texlive-xetex-bin \
        && \
    /usr/bin/pip3 install \
        Flask \
        actdiag \
        blockdiag \
        nwdiag \
        pandocfilters \
        seqdiag \
        typing \
        && \
    rm -rf /var/cache/* /root/.cache /tmp/.[A-Za-z]* /tmp/* && \
    mktexfmt xelatex.fmt
