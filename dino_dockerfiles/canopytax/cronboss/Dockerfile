FROM alpine

RUN apk add --update python3 && \
    rm /var/cache/apk/*

COPY . /app/
RUN python3 -m ensurepip && \
    python3 -m pip install -r /app/requirements.txt

# Hotfix for glibc hack that fixes the order of DNS resolving (i.e. check /etc/hosts first and then lookup DNS-servers).
# To fix this we just create /etc/nsswitch.conf and add the following line:
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf

Entrypoint ["/app/cronboss.py"]
