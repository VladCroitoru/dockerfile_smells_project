FROM busybox:1.26

ADD builds/2.0.0/linux_amd64/tld-proxy-pac /bin/tld-proxy-pac

ENTRYPOINT ["tld-proxy-pac", "--forward-host=127.0.0.1"]
