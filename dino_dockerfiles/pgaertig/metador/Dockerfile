FROM debian:buster-slim

ENV DEBIAN_FRONTEND=noninteractive HOME=/rubyapp GEM_HOME=/rubyapp/.gems

# Installing:
#   - ffmpeg
#   - VIPS for ruby-vips,  Imagemagick for MiniMagick, GDK Pixbuf
#   - Libraw for ImageMagick for cameras RAW files
#   - libmagic - detecting file formats
#   - ghostscript - PDF conversion
#   - Ruby 2.5
RUN apt-get update -yq && apt-get dist-upgrade -yq && \
    apt-get install -yq --no-install-recommends \
                        imagemagick ffmpeg libvips libgdk-pixbuf2.0-0 ghostscript \
                        libgirepository1.0 gir1.2-vips-8.0 gir1.2-gdkpixbuf-2.0 \
                        libraw-dev libmagic1 dumb-init \
                        ruby bundler git && \
    apt-get -y autoremove && apt-get -y clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/{man,doc,locale,zoneinfo,icons}


# These files need to be added first to reinvoke gems installation once they change
ADD Gemfile Gemfile.lock metador.gemspec /rubyapp/
ADD lib/metador/version.rb /rubyapp/lib/metador/version.rb
ADD util /rubyapp/util

# Installing gems with build dependencies. Once built dependencies are removed to keep image small.
RUN apt-get update -yq && \
    apt-get install -yq --no-install-recommends \
            ruby-dev libgirepository1.0-dev libgdk-pixbuf2.0-dev libvips-dev libgsf-1-dev nasm \
            && \
    cd /rubyapp && \
    bundle install --clean --force --no-cache --system --without development && \
    apt-get remove -yq ruby-dev libgirepository1.0-dev libgdk-pixbuf2.0-dev libvips-dev libgsf-1-dev nasm && apt-get autoremove -yq && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/{man,doc,locale,zoneinfo,icons} && \
    rm -rf /var/lib/gems/*/cache /rubyapp/.bundle/cache /root/.bundle/cache && \
    /rubyapp/util/setup_imagemagick.sh

ADD . /rubyapp

CMD ["/rubyapp/docker/container_run.sh"]
