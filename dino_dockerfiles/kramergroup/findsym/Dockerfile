FROM alpine:3.5

# Install isotropy
RUN wget http://stokes.byu.edu/iso/iso.zip && \
    mkdir -p /isotropy && \
    unzip /iso.zip -d /isotropy && \
    rm -rf /iso.zip && \
    ln -s /isotropy/findsym /bin/findsym && \
    ln -s /isotropy/iso /bin/iso && \
    ln -s /isotropy/comsubs /bin/comsubs && \
    ln -s /isotropy/smodes /bin/smodes

ENV ISODATA=/isotropy/

# Install entrypoint
COPY entrypoint.sh /entrypoint

CMD ["/entrypoint"]
