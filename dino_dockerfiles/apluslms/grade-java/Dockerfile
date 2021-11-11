ARG BASE_TAG=latest
FROM apluslms/grading-base:$BASE_TAG

COPY rootfs /

RUN : \
 # openjdk package fails in debian slim container... fix that
 && mkdir -p /usr/share/man/man1 \
 && apt_install \
    # Install Java 11
    openjdk-17-jdk-headless \
 # fixes missing org.GNOME.Accessibility.AtkWrapper
 && echo "" > /etc/java-17-openjdk/accessibility.properties \
 # install apt+ivy for ivy_install
 && apt_install \
    ant \
    ivy \
 && rm -r /usr/share/man \
\
 # Install libraries
 && ivy_install -n "grade-java" -d "/usr/local/java/lib" \
    junit junit 4.13 \
\
 && :

COPY bin /usr/local/bin
ENV CLASSPATH=.:/exercise:/exercise/*:/exercise/lib/*:/usr/local/java/lib/*
CMD ["run-all-junits"]
