FROM opensuse/leap:15
MAINTAINER xuewenlong <flippy@sina.com>

ARG JAVA_VERSION=${JAVA_VERSION:-8}
ARG JAVA_UPDATE=${JAVA_UPDATE:-221}
ARG JAVA_BUILD=${JAVA_BUILD:-11}
ARG JAVA_PATH=${JAVA_PATH:-230deb18db3e4014bb8e3e8324f81b43}
ENV JVM_BASE=/usr/lib64/jvm
ENV JAVA_HOME=${JVM_BASE}/java

RUN zypper -n in aaa_base-extras busybox libcares2 libexpat1 libmetalink3 timezone wget && \
rm -rf \
/etc/skel/.emacs \
/etc/skel/.inputrc \
/usr/lib/base-scripts/backup-rpmdb \
/usr/lib/base-scripts/backup-sysconfig \
/usr/lib/base-scripts/check-battery \
/usr/lib/systemd/system/backup-rpmdb.service \
/usr/lib/systemd/system/backup-rpmdb.timer \
/usr/lib/systemd/system/backup-sysconfig.service \
/usr/lib/systemd/system/backup-sysconfig.timer \
/usr/lib/systemd/system/check-battery.service \
/usr/lib/systemd/system/check-battery.timer \
/usr/share/fillup-templates \
/var/adm/backup \
/usr/bin/busybox.install \
/usr/share/busybox \
/usr/share/info \
/usr/share/man \
/usr/share/doc \
/var/cache/zypp/* && \
find /usr/share/locale -name '*.mo' -exec rm {} \; && \
zypper clean -a && \
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
echo "nobody:x:65534:" >> /etc/group && \
echo "nobody:x:65534:65534:nobody:/var/lib/nobody:/bin/bash" >> /etc/passwd && \
echo "nobody:!:17569::::::" >> /etc/shadow && \
mkdir -p /var/lib/nobody && \
chown 65534:65534 /var/lib/nobody && \
echo "#!/bin/bash" > /tmp/busybox_install.sh && \
echo "CMDS=\`busybox --list\`" >> /tmp/busybox_install.sh && \
echo "for cmd in \$CMDS;do" >> /tmp/busybox_install.sh && \
echo "  if [[ \"\$cmd\" != \"[\" && \"\$cmd\" != \"[[\" ]];then" >> /tmp/busybox_install.sh && \
echo "  busybox which \$cmd 1>/dev/null 2>&1" >> /tmp/busybox_install.sh && \
echo "    if [ \$? -ne 0 ];then" >> /tmp/busybox_install.sh && \
echo "       echo \"link /usr/bin/busybox -> /usr/local/bin/\$cmd\"" >> /tmp/busybox_install.sh && \
echo "       ln -s /usr/bin/busybox /usr/local/bin/\$cmd"  >> /tmp/busybox_install.sh && \
echo "    fi" >> /tmp/busybox_install.sh && \
echo "  fi" >> /tmp/busybox_install.sh && \
echo "done" >> /tmp/busybox_install.sh && \
chmod o+x /tmp/busybox_install.sh && \
/tmp/busybox_install.sh && \
rm -rf /tmp/*

ENV LANG=en_US.UTF-8

RUN cd /tmp && \
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie;" "http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_PATH}/jre-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie;" "http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION}/jce_policy-${JAVA_VERSION}.zip" && \
mkdir -p "${JVM_BASE}" && \
cd "${JVM_BASE}" && \
gzip -dc "/tmp/jre-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" | tar -xvf - && \
chown -R root:root "${JVM_BASE}/jre1.${JAVA_VERSION}.0_${JAVA_UPDATE}" && \
ln -s "${JVM_BASE}/jre1.${JAVA_VERSION}.0_${JAVA_UPDATE}" "${JAVA_HOME}" && \
ln -sf ${JAVA_HOME}/bin/* /usr/bin/ && \
cd ${JAVA_HOME} && \
unzip -o -d lib/security /tmp/jce_policy-${JAVA_VERSION}.zip && \
rm -rf COPYRIGHT LICENSE README *.html *.txt \
bin/javaws \
man \
plugin \
lib/missioncontrol \
lib/visualvm \
lib/*javafx* \
lib/jfr* \
lib/plugin.jar \
lib/desktop \
lib/deploy* \
lib/images \
lib/javaws.jar \
lib/*javafx* \
lib/*jfx* \
lib/amd64/libdecora_sse.so \
lib/amd64/libprism_*.so \
lib/amd64/libfxplugins.so \
lib/amd64/libglass.so \
lib/amd64/libgstreamer-lite.so \
lib/amd64/libjavafx*.so \
lib/amd64/libjfx*.so \
lib/ext/jfxrt.jar \
lib/oblique-fonts \
lib/security/README.txt \
/tmp/*

RUN zypper -n in libreoffice libreoffice-writer libreoffice-calc dejavu-fonts wqy-zenhei-fonts && \
echo '#!/bin/bash' > /usr/bin/run_soffice.sh && \
echo ': ${HOST_IN:=127.0.0.1}' >> /usr/bin/run_soffice.sh && \
echo ': ${PORT_IN:=8100}' >> /usr/bin/run_soffice.sh && \
echo 'SOFFICE_CMD="/usr/lib64/libreoffice/program/soffice"' >> /usr/bin/run_soffice.sh && \
echo 'SOFFICE_ARGS=(' >> /usr/bin/run_soffice.sh && \
echo '    "--accept=socket,host=${HOST_IN},port=${PORT_IN},tcpNoDelay=1;urp"' >> /usr/bin/run_soffice.sh && \
echo '    "--headless"' >> /usr/bin/run_soffice.sh && \
echo '    "--invisible"' >> /usr/bin/run_soffice.sh && \
echo '    "--nodefault"' >> /usr/bin/run_soffice.sh && \
echo '    "--nofirststartwizard"' >> /usr/bin/run_soffice.sh && \
echo '    "--nolockcheck"' >> /usr/bin/run_soffice.sh && \
echo '    "--nologo"' >> /usr/bin/run_soffice.sh && \
echo '    "--norestore"' >> /usr/bin/run_soffice.sh && \
echo ')' >> /usr/bin/run_soffice.sh && \
echo 'case "$1" in' >> /usr/bin/run_soffice.sh && \
echo '    -- | soffice-headless)' >> /usr/bin/run_soffice.sh && \
echo '        shift' >> /usr/bin/run_soffice.sh && \
echo '        fc-cache -f' >> /usr/bin/run_soffice.sh && \
echo '        exec ${SOFFICE_CMD} "${SOFFICE_ARGS[@]}" "$@"' >> /usr/bin/run_soffice.sh && \
echo '        ;;' >> /usr/bin/run_soffice.sh && \
echo '    -*)' >> /usr/bin/run_soffice.sh && \
echo '        fc-cache -f' >> /usr/bin/run_soffice.sh && \
echo '        exec ${SOFFICE_CMD} "$@"' >> /usr/bin/run_soffice.sh && \
echo '        ;;' >> /usr/bin/run_soffice.sh && \
echo '    debug)' >> /usr/bin/run_soffice.sh && \
echo '        echo "LibreOffice parameters:" ${SOFFICE_ARGS[@]}' >> /usr/bin/run_soffice.sh && \
echo '        exit 0' >> /usr/bin/run_soffice.sh && \
echo '        ;;' >> /usr/bin/run_soffice.sh && \
echo '    *)' >> /usr/bin/run_soffice.sh && \
echo '        exec "$@"' >> /usr/bin/run_soffice.sh && \
echo 'esac' >> /usr/bin/run_soffice.sh && \
echo 'exit 0' >> /usr/bin/run_soffice.sh && \
chmod 755 /usr/bin/run_soffice.sh && \
rm -rf \
/usr/share/alsa \
/usr/share/appdata \
/usr/share/applications \
/usr/share/application-registry \
/usr/share/doc \
/usr/share/man \
/usr/share/themes \
/usr/share/X11/xkb \
/usr/share/icons \
/usr/share/mime \
/usr/share/zsh \
/usr/share/libreoffice/*.txt \
/usr/share/libreoffice/help \
/usr/share/libreoffice/share/config \
/usr/share/libreoffice/share/wizards \
/usr/lib64/libreoffice/help \
/usr/lib64/libreoffice/share/autocorr \
/usr/lib64/libreoffice/share/autotext \
/usr/lib64/libreoffice/share/classification \
/usr/lib64/libreoffice/share/dtd \
/usr/lib64/libreoffice/share/emojiconfig \
/usr/lib64/libreoffice/share/template \
/usr/lib64/libreoffice/share/wizards \
/usr/lib64/libreoffice/share/wordbook \
/var/cache/zypp/* && \
zypper clean -a

VOLUME /var/cache/fontconfig
ENTRYPOINT [ "/usr/bin/run_soffice.sh" ]
