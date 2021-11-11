FROM alpine

WORKDIR /root

RUN apk update && apk add \
    curl \
    tar \
    perl \
    xz
RUN curl https://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz -o tex-live.tar.gz \
    && tar xzf tex-live.tar.gz
RUN printf "%s\n" \
        "selected_scheme scheme-basic" \
        "tlpdbopt_install_docfiles 0" \
        "tlpdbopt_install_srcfiles 0" \
        > texlive.profile
RUN $(find ./ -name "install-tl*" -type d)/install-tl -profile ~/texlive.profile ; exit 0

RUN /usr/local/texlive/$(date +%Y)/bin/x86_64-linuxmusl/tlmgr install \
    collection-latexrecommended \
    collection-fontsrecommended \
    collection-langjapanese \
    lastpage \
    titlesec \
    multirow \
    ; exit 0

COPY entrypoint.sh /entrypoint.sh
COPY mystyle.sty /mystyle.sty

RUN rm -rf ~/* \
    && adduser -D user \
    && chmod +x /entrypoint.sh

USER user

WORKDIR /home/user

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "doc" ]
VOLUME /home/user
