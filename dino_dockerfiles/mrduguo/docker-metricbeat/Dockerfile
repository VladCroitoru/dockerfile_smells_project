FROM    alpine:3.3
ADD     entrypoint.sh    /entrypoint.sh
ADD     metricbeat.yml /metricbeat.yml

RUN     apk add --update python curl && \
        wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.21-r2/glibc-2.21-r2.apk" \
             "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.21-r2/glibc-bin-2.21-r2.apk" && \
        apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \
        /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
         curl -sL https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-5.0.1-linux-x86_64.tar.gz | tar xz -C . && \
         mv metricbeat-*-linux-x86_64 /metricbeat && \
         mv /metricbeat/metricbeat /bin/metricbeat && \
         rm -rf *.apk && \
         mkdir /logs && \
         chmod +x /entrypoint.sh

ENTRYPOINT  ["/entrypoint.sh"]
