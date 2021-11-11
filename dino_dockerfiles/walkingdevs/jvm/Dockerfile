FROM walkingdevs/glibc

ENV JAVA_HOME=/jvm

RUN wget http://dl.bintray.com/aibar/generic/jdk-8.102.tar.gz -O jdk.tar.gz && \
    tar xzf jdk.tar.gz && \
    rm jdk.tar.gz && \
    mv jdk1.8.0_102 fat-jdk && \

    #
    # Our minimal JDK
    #
    mkdir -pv jvm/bin \
              jvm/lib/amd64/jli && \
    mkdir -pv jvm/jre/bin \
              jvm/jre/lib/ext \
              jvm/jre/lib/security \
              jvm/jre/lib/amd64/jli \
              jvm/jre/lib/amd64/server && \

    #
    # Jre libs
    #
    cd fat-jdk/jre/lib && \

    cp rt.jar \
       currency.data \
       tzdb.dat \
       jsse.jar \
       jce.jar \
       content-types.properties \
       resources.jar /jvm/jre/lib && \

    cp amd64/jvm.cfg \
       amd64/libjava.so \
       amd64/libverify.so \
       amd64/libzip.so \
       amd64/libinstrument.so \
       amd64/libmanagement.so \
       amd64/libnet.so \
       amd64/libnio.so \
       amd64/libattach.so \
       amd64/libresource.so /jvm/jre/lib/amd64 && \

    cp amd64/server/libjvm.so /jvm/jre/lib/amd64/server && \

    cp amd64/jli/libjli.so /jvm/jre/lib/amd64/jli && \

    cp security/US_export_policy.jar \
       security/blacklisted.certs \
       security/cacerts \
       security/java.policy \
       security/java.security \
       security/local_policy.jar /jvm/jre/lib/security && \

    cp ext/sunjce_provider.jar \
       ext/sunec.jar /jvm/jre/lib/ext && \

    #
    # Executables
    #
    cp /fat-jdk/jre/bin/java /jvm/jre/bin && \
    cp /fat-jdk/bin/java \
       /fat-jdk/bin/javac /jvm/bin && \

    #
    # Jdk libs
    #
    cp /fat-jdk/lib/tools.jar /jvm/lib && \
    cp /fat-jdk/lib/amd64/jli/libjli.so /jvm/lib/amd64/jli && \

    ln -s /jvm/bin/java /bin/java && \
    ln -s /jvm/bin/javac /bin/javac && \

    rm -rf /fat-jdk