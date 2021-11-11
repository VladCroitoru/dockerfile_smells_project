# Extend from Alpine open-jdk
FROM alpine:3.7

# Set Maintainer
LABEL authors="Vernon Chapman <g8tor692@gmail.com>"

# Add System PAckages
RUN apk --no-cache add build-base bash \
                    python3 python3-dev ncurses make coreutils \
                    gawk bash file libpng libpng-dev freetype \
                    freetype-dev libzmq && \
    pip3 install "numpy==1.14.0" "pandas==0.22.0" "beautifulsoup4==4.6.0" \
                 "gastrodon==0.9.3" "jupyter==1.0.0" 