FROM base/archlinux:latest
RUN pacman -Syy --noconfirm ghostscript libpng libraw librsvg libwebp libwmf libxml2 openexr openjpeg2 imagemagick
ADD imgcat run.sh /
CMD ["./run.sh"]
