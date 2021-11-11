FROM djmattyg007/ubuntu-build:20170213-1
MAINTAINER djmattyg007

RUN apt-get -q update && \
    apt-get -yq install \
        python3-netifaces \
        python3-requests \
        python3-systemd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip3 install click

ENV JDN_VERSION="2.0.0" JDN_ITERATION=1 BASEDIR=/tmp/journald-notify PKGDIR=/tmp/journald-notify/pkg

RUN curl -sS -L --create-dirs -o "${BASEDIR}/journald-notify.tar.gz" "https://github.com/djmattyg007/journald-notify/archive/${JDN_VERSION}.tar.gz"
WORKDIR "${BASEDIR}"
RUN tar xzvf "journald-notify.tar.gz"
WORKDIR "${BASEDIR}/journald-notify-${JDN_VERSION}"
RUN python3 setup.py install --root=${PKGDIR} --install-lib=/usr/lib/python3/dist-packages && \
    install -Dm644 LICENSE "${PKGDIR}/usr/share/journald-notify/LICENSE" && \
    install -Dm644 examples/journald-notify.json "${PKGDIR}/usr/share/journald-notify/journald-notify.json.example" && \
    install -Dm644 examples/journald-notify.service "${PKGDIR}/lib/systemd/system/journald-notify.service" && \
    mkdir -p ${PKGDIR}/usr/bin && \
    cp journald-notify ${PKGDIR}/usr/bin/journald-notify

COPY postinst ${BASEDIR}/postinst

WORKDIR ${BASEDIR}
RUN fpm \
    -C ${PKGDIR} \
    -s dir \
    -t deb \
    -n journald-notify \
    -a all \
    -v ${JDN_VERSION} \
    --iteration ${JDN_ITERATION}-xenial \
    --description "journald-notify ${JDN_VERSION}" \
    --license "BSD" \
    --url "https://github.com/djmattyg007/journald-notify" \
    --maintainer "Matthew Gamble" \
    --after-install ${BASEDIR}/postinst \
    -d python3-netifaces \
    -d python3-requests \
    -d python3-systemd \
    lib usr

CMD cp ${BASEDIR}/journald-notify_${JDN_VERSION}-${JDN_ITERATION}-xenial_all.deb /data
