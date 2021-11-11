FROM wenhsiaoyi/ubuntu-base:jre8
MAINTAINER Jack Wen <http://github.com/wenhsiaoyi>

RUN apt-get update && \
    apt-get install -y \
        curl \
        ruby \
        unzip

RUN useradd -m sencha && \
    cd && cp -R .bashrc .profile /home/sencha && \
    mkdir -p /project && \
    chown -R sencha:sencha /home/sencha /project

USER sencha
ENV HOME /home/sencha
ENV _JAVA_OPTIONS -Xms1024m -Xmx2048m

RUN curl -o /home/sencha/cmd.sh.zip http://cdn.sencha.com/cmd/6.7.0.63/no-jre/SenchaCmd-6.7.0.63-linux-amd64.sh.zip && \
    unzip -p /home/sencha/cmd.sh.zip > /home/sencha/cmd-install.sh && \
    chmod +x /home/sencha/cmd-install.sh && \
    /home/sencha/cmd-install.sh -q && \
    rm /home/sencha/cmd*

ENV PATH /home/sencha/bin/Sencha/Cmd/6.7.0.63/:$PATH

EXPOSE 1841


VOLUME ["/var/www", "/opt/projects"]
WORKDIR /var/www

CMD ["bash"]
