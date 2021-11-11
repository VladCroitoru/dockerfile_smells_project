FROM gentoo/stage3-amd64
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN touch /etc/init.d/functions.sh && \
    echo 'PYTHON_TARGETS="${PYTHON_TARGETS} python2_7"' >> /etc/portage/make.conf && \
    echo 'PYTHON_SINGLE_TARGET="python2_7"' >> /etc/portage/make.conf && \
    echo 'EMERGE_DEFAULT_OPTS="--ask=n --jobs=4"' >> /etc/portage/make.conf && \
    echo 'GENTOO_MIRRORS="http://gentoo.osuosl.org/ http://mirrors.evowise.com/gentoo/"' >> /etc/portage/make.conf

RUN mkdir -p /etc/portage/repos.conf

RUN ( \
    echo '[gentoo]'  && \
    echo 'location = /usr/portage' && \
    echo 'sync-type = rsync' && \
    echo 'sync-uri = rsync://rsync.us.gentoo.org/gentoo-portage/' && \
    echo 'auto-sync = yes' \
    )> /etc/portage/repos.conf/gentoo.conf

# Setup the portage directory and permissions
RUN mkdir -p /usr/portage/{distfiles,metadata,packages}
RUN chown -R portage:portage /usr/portage
RUN echo "masters = gentoo" > /usr/portage/metadata/layout.conf

# Sync portage
RUN emerge-webrsync -q

# Display some news items
RUN eselect news read new

# Finalization
RUN env-update
