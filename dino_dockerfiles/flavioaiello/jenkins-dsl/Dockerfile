FROM alpine:3.8

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH ${PATH}:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_VERSION 2.164.1
ENV JENKINS_PLUGINS_LATEST true
ENV FC_LANG de-CH
ENV LC_CTYPE de_CH.UTF-8

# Add scripts and plugin list
COPY files /

# Packages
RUN set -ex;\
    apk update;\
    apk add --no-cache tini ca-certificates openjdk8 bash git curl zip wget docker fontconfig ttf-dejavu jq coreutils openssh py2-pip;\
    rm -rf /var/cache/apk/*;\
    echo "*** fix key permissions ***";\
    chmod 600 /root/.ssh/id_rsa;\
    echo "*** Installing docker-compose ***";\
    pip install --upgrade pip;\
    pip install docker-compose

# Install Jenkins and plugins from plugins.txt
RUN echo "*** Installing jenkins ***";\
    curl -sSL --create-dirs --retry 3 mirrors.jenkins.io/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /usr/share/jenkins/jenkins.war;\
    echo "*** Recursive solve and reduce plugin dependencies ***";\
    curl -sSO --retry 3 https://updates.jenkins.io/current/update-center.actual.json;\
    false; until [ $? -eq 0 ]; do \
       cp /var/jenkins_home/plugins.txt /var/jenkins_home/check;\
       jq --arg p "$(sed -e ':a;N;$!ba;s/\n/ /g' /var/jenkins_home/plugins.txt)" -r '.plugins[] | select([.name] | inside([$p]))| .dependencies[] | select(.optional == false)| .name + ":" + .version' update-center.actual.json >> /var/jenkins_home/plugins.txt;\
       sort -Vr /var/jenkins_home/plugins.txt | sort -u -t: -k1,1 -o /var/jenkins_home/plugins.txt;\
       cmp -s /var/jenkins_home/check /var/jenkins_home/plugins.txt;\
    done;\
    rm /var/jenkins_home/check;\
    echo "*** Jenkins install plugins from plugins.txt *** ";\
    while read plugin; do \
       if $JENKINS_PLUGINS_LATEST; then plugin="${plugin%:*}:latest"; else plugin="${plugin%:*}:${plugin#*:}"; fi;\    echo "*** Downloading ${plugin} ***";\
       curl -sSL --create-dirs --retry 3 http://mirrors.jenkins.io/download/plugins/${plugin%:*}/${plugin#*:}/${plugin%:*}.hpi -o /var/jenkins_home/plugins/${plugin%:*}.jpi;\
       touch /var/jenkins_home/plugins/${plugin%:*}.jpi.pinned;\
    done < /var/jenkins_home/plugins.txt

EXPOSE 8080 8443

ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]
CMD ["java", "${JAVA_OPTS}", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseCGroupMemoryLimitForHeap", "-XX:MaxRAMFraction=2", "-XX:+HeapDumpOnOutOfMemoryError", "-XshowSettings:vm", "-Djava.awt.headless=true", "-Djenkins.install.runSetupWizard=false", "-jar", "/usr/share/jenkins/jenkins.war", "${JENKINS_OPTS}"]
