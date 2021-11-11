FROM base/archlinux

RUN mkdir context
RUN cd context; /usr/bin/curl -O https://raw.githubusercontent.com/adityam/context-pkgbuild/docker/PKGBUILD
RUN cd context; /usr/bin/curl -O https://raw.githubusercontent.com/adityam/context-pkgbuild/docker/context-minimals-docker.install
RUN cd context; /usr/bin/makepkg -sic --asroot --noconfirm
RUN rm -rf context

