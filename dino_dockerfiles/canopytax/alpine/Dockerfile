from alpine

# Fix env command to also have the --null option
copy my_env.sh /usr/local/bin/env

RUN apk add --update bash && \
    rm /var/cache/apk/*
    
# Hotfix for glibc hack that fixes the order of DNS resolving (i.e. check /etc/hosts first and then lookup DNS-servers).
# To fix this we just create /etc/nsswitch.conf and add the following line:
ONBUILD RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf
