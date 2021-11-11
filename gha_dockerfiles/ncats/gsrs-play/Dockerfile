FROM centos:8 AS builder
RUN dnf -y install dejavu-sans-fonts dejavu-serif-fonts fontconfig git java-1.8.0-openjdk-devel && dnf clean all && fc-cache -f
COPY . /tmp/build
WORKDIR /tmp/build
RUN ./activator clean
RUN ./activator -Dconfig.file=modules/ginas/conf/ginas.conf ginas/dist
RUN cd /opt && \
    jar xf /tmp/build/modules/ginas/target/universal/ginas-*.zip && \
    mv /opt/ginas-* /opt/g-srs && \
    chmod 755 /opt/g-srs/bin/ginas
RUN cd /root && \
    jar xf /tmp/build/lib/jni-inchi-0.7-jar-with-dependencies.jar && \
    mkdir -p /root/.jnati/repo/jniinchi/1.03_1 && \
    mv /root/META-INF/jniinchi/1.03_1/LINUX-AMD64 /root/.jnati/repo/jniinchi/1.03_1/LINUX-AMD64 && \
    rm -rf * && \
    rm -rf .ivy2 .sbt && \
    chmod -R g=u /root
WORKDIR /opt/g-srs
RUN mv /tmp/build/modules/ginas/conf /opt/g-srs/conf
RUN sed -i "s/localhost/db/g" conf/ginas-mysql.conf
RUN sed -i "s/localhost:5433/db:5432/g" conf/ginas-postgres.conf
RUN sed -i "s/#evolutionplugin=disabled/evolutionplugin=disabled/g" conf/ginas-*.conf

FROM centos:8
RUN dnf -y install dejavu-sans-fonts dejavu-serif-fonts fontconfig java-1.8.0-openjdk-headless && dnf clean all
COPY --from=builder /opt /opt
COPY --from=builder /root /root
COPY entrypoint.sh /entrypoint.sh
RUN fc-cache -f && \
    mkdir /data && \
    chmod -R g=u /data && \
    ln -s /data/conf/evolutions /opt/g-srs/conf/evolutions && \
    ln -s /data/conf/sql /opt/g-srs/conf/sql && \
    ln -s /data/exports /opt/g-srs/exports && \
    ln -s /data/ginas.ix /opt/g-srs/ginas.ix && \
    ln -s /data/logs /opt/g-srs/logs
VOLUME ["/data"]
EXPOSE 9000
ENTRYPOINT ["/entrypoint.sh"]
WORKDIR /opt/g-srs
CMD ["bin/ginas"]
