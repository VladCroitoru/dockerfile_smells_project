FROM ubuntu:xenial

MAINTAINER Sun Seng David Tan <sunix@sunix.org>

RUN apt-get update && \
    apt-get install -y ghostscript pdftk wget imagemagick webp libwebp-dev libgraphicsmagick1-dev libmagickcore-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /data && chmod 777 /data
RUN sed -i 's#<policy domain="coder" rights="none" pattern="PDF" />#<policy domain="coder" rights="read|write" pattern="PDF" />#' /etc/ImageMagick-6/policy.xml

USER 0
# Set permissions on /etc/passwd and /home to allow arbitrary users to write
COPY --chown=0:0 entrypoint.sh /
COPY --chown=0:0 download.sh /

RUN mkdir -p /projects && \
    mkdir -p /home/user && \
    chgrp -R 0 /home && \
    chmod -R g=u /etc/passwd /etc/group /home && \
    chmod +x /entrypoint.sh && chmod +x /download.sh
COPY bashrc /home/user/.bashrc

USER 10001
ENV HOME=/home/user
WORKDIR /projects
ENTRYPOINT [ "/entrypoint.sh" ]

CMD cd /data && pdftk *.pdf cat output large.pdf && pdf2ps large.pdf very_large.ps && ps2pdf very_large.ps final.pdf && rm large.pdf very_large.ps
