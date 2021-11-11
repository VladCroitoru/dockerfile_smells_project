FROM desktopcontainers/base-debian

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q -y update \
 && apt-get -q -y install openjdk-8-jre \
                          default-java-plugin \
                          iceweasel \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 \
 \
 && sed -i 's/https:.*first.*"/"/g' /usr/lib/firefox-esr/browser/defaults/preferences/firefox-branding.js \
 \
 && sed -i 's/touch ".INITIALIZED"/&\n\n	# add weburl as firefox startpage\n	env | grep WEB_URL >> \/etc\/environment\n/g' /usr/local/bin/entrypoint.sh \
 \
 && echo "kill \$(pidof firefox-esr)" >> /usr/local/bin/ssh-app.sh \
 && echo "firefox --new-instance \$WEB_URL\n" >> /usr/local/bin/ssh-app.sh \
 \
 \
 && mkdir /home/app/.config/icedtea-web \
 && echo "deployment.security.jsse.hostmismatch.warning=false" > /home/app/.config/icedtea-web/deployment.properties \
 && echo "deployment.security.sandbox.awtwarningwindow=false" >> /home/app/.config/icedtea-web/deployment.properties \
 && echo "deployment.security.level=ALLOW_UNSIGNED" >> /home/app/.config/icedtea-web/deployment.properties \
 && chown app.app -R /home/app/.config
