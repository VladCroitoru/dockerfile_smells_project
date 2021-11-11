FROM heroku/jvm

# Install Boot

RUN wget -O /usr/bin/boot https://github.com/boot-clj/boot-bin/releases/download/latest/boot.sh \
 && chmod +x /usr/bin/boot

# Boot ENV

ENV BOOT_HOME /.boot
ENV BOOT_AS_ROOT yes
ENV BOOT_LOCAL_REPO /m2
ENV BOOT_JVM_OPTIONS=-Xmx2g
ENV BOOT_VERSION 2.6.0
ENV BOOT_CLOJURE_VERSION 1.7.0

# download & install deps, cache REPL and web deps
RUN /usr/bin/boot repl -e '(System/exit 0)' && rm -rf target
