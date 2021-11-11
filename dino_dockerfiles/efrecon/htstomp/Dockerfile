FROM efrecon/mini-tcl
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>

# Copy files, arrange to copy the READMEs, which will also create the
# relevant directories.
COPY *.tcl /opt/htstomp/
COPY lib/*.md /opt/htstomp/lib/
COPY exts/*.md /opt/htstomp/exts/

# Install git so we can install dependencies, then htstomp into /opt and til in
# the lib subdirectory. Finally cleanup. Do this in one single go to keep the
# size of the image small.
RUN apk add --update-cache git && \
    git clone https://github.com/efrecon/tcl-stomp /tmp/tcl-stomp && \
    rm -rf /tmp/tcl-stomp/.git && \
    mv /tmp/tcl-stomp/lib/stomp /opt/htstomp/lib/ && \
    git clone https://github.com/efrecon/til /opt/htstomp/lib/til && \
    rm -rf /opt/htstomp/lib/til/.git && \
    rm -rf /var/cache/apk/* && \
    apk del git

# Expose the default HTTP incoming port.
EXPOSE 8080

# Export the plugin directory so it gets easy to test new plugins.
VOLUME /opt/htstomp/exts

ENTRYPOINT ["tclsh8.6", "/opt/htstomp/htstomp.tcl"]
CMD ["-verbose", "notice"]
