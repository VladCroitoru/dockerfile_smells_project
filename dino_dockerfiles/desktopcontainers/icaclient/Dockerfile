FROM desktopcontainers/base-debian

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -q -y update && \
    apt-get -q -y install wget \
                          iceweasel && \
    apt-get -q -y install libxmu6 \
                          libglu1-mesa && \
    \
    wget -O - https://www.citrix.com/de-de/downloads/workspace-app/linux/workspace-app-for-linux-latest.html 2>/dev/null | grep '<a' | grep icaclient_ | grep _amd64 | sed 's/.*rel="/https:/g' | sed 's/".*//g' | sed 's/^/wget -O icaclient.deb /g' | sh && \
    \
    apt-get -q -y install -f /icaclient.deb && \
    \
    apt-get -q -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    \
    mkdir -p /opt/Citrix/ICAClient/keystore/cacerts && \
    ln -s /usr/share/ca-certificates/mozilla/* /opt/Citrix/ICAClient/keystore/cacerts/ && \
    c_rehash /opt/Citrix/ICAClient/keystore/cacerts/ > /dev/null && \
    \
    echo "kill \$(pidof firefox-esr)" >> /container/scripts/app && \
    echo "firefox --new-instance \$WEB_URL\n" >> /container/scripts/app && \
    \
    mkdir /home/app/.ICAClient && \
    touch /home/app/.ICAClient/.eula_accepted && \
    chown app.app -R /home/app/.ICAClient && \
    \
    sed -i 's/# INIT PHASE/# INIT PHASE\nenv | grep WEB_URL >> \/etc\/environment\n/g' /container/scripts/entrypoint.sh
