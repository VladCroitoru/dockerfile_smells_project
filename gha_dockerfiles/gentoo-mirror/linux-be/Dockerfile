FROM gentoo/portage as portage
FROM gentoo/stage3-amd64 as setup
ENV installed_overlay /var/git/linux-be

RUN mkdir /etc/portage/repos.conf &&\
    echo -e "\
    [linux-be]\n\
    location = $installed_overlay\n\
    auto-sync = no"\
    >> /etc/portage/repos.conf/linux-be

RUN mkdir -p /etc/portage/package.use &&\
    cd /etc/portage/package.use &&\
    ln -s "$installed_overlay"/Documentation/package.use/linux-be.use

RUN mkdir -p /etc/portage/package.accept_keywords &&\
    cd /etc/portage/package.accept_keywords &&\
    ln -s "$installed_overlay"/Documentation/package.accept_keywords/linux-be.keywords &&\
    ln -s "$installed_overlay"/Documentation/package.accept_keywords/linux-be-zfs-master.keywords &&\
    ln -s "$installed_overlay"/Documentation/package.accept_keywords/linux-be-zfs-0.7.keywords


COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo

RUN echo "dev-vcs/git -gpg -iconv -nls -pcre-jit -pcre -perl -python -webdav" >> /etc/portage/package.use/git
RUN echo "sys-kernel/gentoo-sources symlink" >> /etc/portage/package.use/kernel

RUN emerge dev-vcs/git

RUN emerge sys-kernel/gentoo-sources

RUN cd /usr/src/linux && make defconfig
RUN cd /usr/src/linux && make

ADD --chown=portage:portage . $installed_overlay
