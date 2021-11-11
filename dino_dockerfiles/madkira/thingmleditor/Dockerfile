FROM ubuntu:14.04

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \
    apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer libxext-dev libxrender-dev libxtst-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

# Install libgtk as a separate step so that we can share the layer above with
# the netbeans image
RUN apt-get update && apt-get install -y libgtk2.0-0 libcanberra-gtk-module

RUN wget 'http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/neon/3/eclipse-dsl-neon-3-linux-gtk-x86_64.tar.gz&r=1' -O /tmp/eclipse.tar.gz -q && \
    echo 'Installing eclipse' && \
    tar -xf /tmp/eclipse.tar.gz -C /opt && \
    rm /tmp/eclipse.tar.gz

RUN /opt/eclipse/eclipse -clean -purgeHistory -application org.eclipse.equinox.p2.director -noSplash \
	-repository \
http://download.eclipse.org/modeling/tmf/xtext/updates/composite/releases/ \
-uninstallIUs \
org.eclipse.xtend.sdk.feature.group,org.eclipse.xtext.sdk.feature.group

RUN /opt/eclipse/eclipse -clean -purgeHistory -application org.eclipse.equinox.p2.director -noSplash \
	-repository \
http://download.eclipse.org/modeling/tmf/xtext/updates/composite/releases/,http://thingml.org/dist/update2/ \
-installIUs \
org.eclipse.xtend.sdk.feature.group,org.eclipse.xtext.sdk.feature.group,thingml.feature.feature.group


ADD run /usr/local/bin/eclipse

RUN chmod +x /usr/local/bin/eclipse && \
    mkdir -p /home/developer && \
    echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:1000:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown developer:developer -R /home/developer && \
    chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo



USER developer
ENV HOME /home/developer
WORKDIR /home/developer
CMD /usr/local/bin/eclipse
