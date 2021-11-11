FROM efrecon/mini-tcl
MAINTAINER Emmanuel Frecon <efrecon@gmail.com>

# Copy files, arrange to copy the READMEs, which will also create the
# relevant directories.
COPY *.tcl /opt/http2mqtt/
COPY lib/ /opt/http2mqtt/lib/
COPY exts/*.tcl /opt/http2mqtt/exts/

# Install git so we can install dependencies, then http2mqtt into /opt and til in
# the lib subdirectory. Finally cleanup. Do this in one single go to keep the
# size of the image small.
# RUN apk add --no-cache git && \
#     git clone --depth 1 https://github.com/efrecon/til /opt/http2mqtt/lib/til && \
#     rm -rf /opt/http2mqtt/lib/til/.git && \
#     git clone --depth 1 https://github.com/efrecon/toclbox /opt/http2mqtt/lib/toclbox && \
#     rm -rf /opt/http2mqtt/lib/toclbox/.git && \
#     apk del git

# Expose the default HTTP incoming port.
EXPOSE 8080

# Export the plugin directory so it gets easy to test new plugins.
VOLUME /opt/http2mqtt/exts

ENTRYPOINT ["tclsh8.6", "/opt/http2mqtt/http2mqtt.tcl"]