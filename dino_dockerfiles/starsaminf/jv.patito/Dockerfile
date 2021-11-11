FROM debian:jessie-slim
COPY ./docker-entrypoint.sh /usr/local/bin/
COPY ./sources.debian.list  /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y make flex g++ libmysqlclient-dev libmysql++-dev php5-fpm php5-mysql php5-gd nginx
RUN apt-get install -y mysql-client
RUN apt-get install -y python2.7 python3

# Setup JAVA_HOME
ENV JAVA_HOME="/usr/lib/jvm/default-jvm"

# Install Oracle JDK (Java SE Development Kit) 8u192 with Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files for JDK/JRE 8
RUN JAVA_VERSION=8 && \
    JAVA_UPDATE=192 && \
    JAVA_BUILD=12 && \
    JAVA_PATH=750e1c8617c5452694857ad95c3ee230 && \
    JAVA_SHA256_SUM=6d34ae147fc5564c07b913b467de1411c795e290356538f22502f28b76a323c2 && \
    JCE_SHA256_SUM=f3020a3922efd6626c2fff45695d527f34a8020e938a49292561f18ad1320b59 && \ 
    apt-get update && \
    apt-get -y install wget unzip && \
    cd "/tmp" && \
    wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" "http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_PATH}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \
    echo "${JAVA_SHA256_SUM}" "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" | sha256sum -c - && \
    wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" "http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION}/jce_policy-${JAVA_VERSION}.zip" && \
    echo "${JCE_SHA256_SUM}" "jce_policy-${JAVA_VERSION}.zip" | sha256sum -c - && \
    tar -xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \
    mkdir -p "/usr/lib/jvm" && \
    mv "/tmp/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}" "/usr/lib/jvm/java-${JAVA_VERSION}-oracle" && \
    ln -s "java-${JAVA_VERSION}-oracle" "$JAVA_HOME" && \
    ln -s "$JAVA_HOME/bin/"* "/usr/bin/" && \
    unzip -jo -d "$JAVA_HOME/jre/lib/security" "jce_policy-${JAVA_VERSION}.zip" && \    
    rm -rf "$JAVA_HOME/"*src.zip \
           "$JAVA_HOME/lib/missioncontrol" \
           "$JAVA_HOME/lib/visualvm" \
           "$JAVA_HOME/lib/"*javafx* \
           "$JAVA_HOME/jre/lib/plugin.jar" \
           "$JAVA_HOME/jre/lib/ext/jfxrt.jar" \
           "$JAVA_HOME/jre/bin/javaws" \
           "$JAVA_HOME/jre/lib/javaws.jar" \
           "$JAVA_HOME/jre/lib/desktop" \
           "$JAVA_HOME/jre/plugin" \
           "$JAVA_HOME/jre/lib/"deploy* \
           "$JAVA_HOME/jre/lib/"*javafx* \
           "$JAVA_HOME/jre/lib/"*jfx* \
           "$JAVA_HOME/jre/lib/amd64/libdecora_sse.so" \
           "$JAVA_HOME/jre/lib/amd64/"libprism_*.so \
           "$JAVA_HOME/jre/lib/amd64/libfxplugins.so" \
           "$JAVA_HOME/jre/lib/amd64/libglass.so" \
           "$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so" \
           "$JAVA_HOME/jre/lib/amd64/"libjavafx*.so \
           "$JAVA_HOME/jre/lib/amd64/"libjfx*.so \
           "$JAVA_HOME/jre/bin/jjs" \
           "$JAVA_HOME/jre/bin/keytool" \
           "$JAVA_HOME/jre/bin/orbd" \
           "$JAVA_HOME/jre/bin/pack200" \
           "$JAVA_HOME/jre/bin/policytool" \
           "$JAVA_HOME/jre/bin/rmid" \
           "$JAVA_HOME/jre/bin/rmiregistry" \
           "$JAVA_HOME/jre/bin/servertool" \
           "$JAVA_HOME/jre/bin/tnameserv" \
           "$JAVA_HOME/jre/bin/unpack200" \
           "$JAVA_HOME/jre/lib/ext/nashorn.jar" \
           "$JAVA_HOME/jre/lib/jfr.jar" \
           "$JAVA_HOME/jre/lib/jfr" \
           "$JAVA_HOME/jre/lib/oblique-fonts" \           
           "$JAVA_HOME/README.html" \
           "$JAVA_HOME/THIRDPARTYLICENSEREADME-JAVAFX.txt" \
           "$JAVA_HOME/THIRDPARTYLICENSEREADME.txt" \            
           "$JAVA_HOME/jre/README" \
           "$JAVA_HOME/jre/THIRDPARTYLICENSEREADME-JAVAFX.txt" \
           "$JAVA_HOME/jre/THIRDPARTYLICENSEREADME.txt" \
           "$JAVA_HOME/jre/Welcome.html" \
           "$JAVA_HOME/jre/lib/security/README.txt" && \           
    apt-get -y autoremove wget unzip && \
    apt-get -y clean && \
    rm -rf "/tmp/"* \
           "/var/cache/apt" \
           "/usr/share/man" \
           "/usr/share/doc" \
           "/usr/share/doc-base" \
           "/usr/share/info/*"
	   
	   
# code
RUN /usr/sbin/useradd -m -u 1536 judge

#
RUN CPU=`grep "cpu cores" /proc/cpuinfo |head -1|awk '{print $4}'` \
	&& sed -i "s/post_max_size = 8M/post_max_size = 80M/g" /etc/php5/fpm/php.ini \
	&& sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 80M/g" /etc/php5/fpm/php.ini \
	&& chmod +x /usr/local/bin/docker-entrypoint.sh \
	&& ln -s /usr/local/bin/docker-entrypoint.sh  /docker-entrypoint.sh

COPY nginx/default.conf /etc/nginx/sites-available/default

WORKDIR /home/judge/
EXPOSE 80
VOLUME ["/home/judge/"]

ENTRYPOINT ["/docker-entrypoint.sh"]
