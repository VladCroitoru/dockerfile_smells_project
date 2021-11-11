FROM alpine:3.7

ENV GLIBC_VERSN 2.26-r0
ENV GLIBC_SH512 3cb28205f94e7d194036e91c8f5e852bc0264bc0492ea5025214df0fad0b7f17d0e235cb4d234ad5b578d40a2aef9e5121c1a8d029fe8e1696eeaae701c2cc0b
ENV GLIBC_BIN_SH512 04a8da5238d90446071528575ef3a53244bca802c8db4efaff218cbd5f7f6ef370a026addfc07fdf8560f38f0814e16b55f3673091dc54e251f5081034f465fa
ENV GLIBC_I18N_SH512 11d91b31b8c3150c4b4829ee23360571c622d2c55972f21aebfe74288c4867a8b721ad03b71491ab3b3d421b8931f47c80b365e57ae3778b853b20c861e0a0ac

#
# BASE PACKAGES + DOWNLOAD GLIBC
#
COPY ./vendor-keys/sgerrand.rsa.pub /etc/apk/keys/
RUN apk add --no-cache \
            bash \
            ca-certificates \
            curl \
            gzip \
            tar && \
    mkdir /opt/ && \
    echo "=== INSTALLING GLIBC =========================" && \
    echo "${GLIBC_SH512}  /opt/glibc-${GLIBC_VERSN}.apk" > /opt/glibc-${GLIBC_VERSN}.apk.sha512 && \
    curl -jkSL -o /opt/glibc-${GLIBC_VERSN}.apk \
        https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSN}/glibc-${GLIBC_VERSN}.apk && \
    sha512sum -c /opt/glibc-${GLIBC_VERSN}.apk.sha512 && \
    apk add /opt/glibc-${GLIBC_VERSN}.apk && \
    echo "=== INSTALLING GLIBC-BIN AND I18N ============" && \
    echo "${GLIBC_BIN_SH512}  /opt/glibc-bin-${GLIBC_VERSN}.apk" > /opt/glibc-bin-${GLIBC_VERSN}.apk.sha512 && \
    curl -jkSL -o /opt/glibc-bin-${GLIBC_VERSN}.apk \
        https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSN}/glibc-bin-${GLIBC_VERSN}.apk && \
    sha512sum -c /opt/glibc-bin-${GLIBC_VERSN}.apk.sha512 && \
    echo "${GLIBC_I18N_SH512}  /opt/glibc-i18n-${GLIBC_VERSN}.apk" > /opt/glibc-i18n-${GLIBC_VERSN}.apk.sha512 && \
    curl -jkSL -o /opt/glibc-i18n-${GLIBC_VERSN}.apk \
        https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSN}/glibc-i18n-${GLIBC_VERSN}.apk && \
    sha512sum -c /opt/glibc-i18n-${GLIBC_VERSN}.apk.sha512 && \
    apk add --no-cache /opt/glibc-bin-${GLIBC_VERSN}.apk /opt/glibc-i18n-${GLIBC_VERSN}.apk && \
    rm -rf /tmp/* /var/cache/apk/* /opt/glibc*  && \
    /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 && \
    echo "export LANG=en_US.UTF-8" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib


ENV LANG en_US.UTF-8
