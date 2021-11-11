FROM gentoo/portage:latest as portage

FROM gentoo/stage3-amd64:latest as builder
COPY --from=portage /var/db/repos/gentoo /var/db/repos/gentoo

RUN emerge dev-python/jinja
RUN rm -rf /var/db/repos/gentoo
RUN echo 'FEATURES="-ipc-sandbox -network-sandbox -pid-sandbox"' >> /etc/portage/make.conf
COPY overlay-packagelist /usr/local/bin

FROM scratch
COPY --from=builder / /

ENTRYPOINT ["overlay-packagelist"]
