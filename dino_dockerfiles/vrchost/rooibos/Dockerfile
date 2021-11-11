FROM python:2.7

LABEL org.label-schema.name="MDID" \
      org.label-schema.description="Basic intallation of MDID" \
      org.label-schema.schema-version="1.0"

ENV PYTHONUNBUFFERED=1

HEALTHCHECK CMD curl -f http://localhost:8080/ || exit 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends libjpeg-dev libfreetype6-dev libldap2-dev \
       autoconf automake build-essential libass-dev libtheora-dev libtool libvorbis-dev pkg-config \
       texinfo zlib1g-dev yasm libx264-dev libmp3lame-dev libsasl2-dev unixodbc-dev \
    && useradd mdid \
    && rm -Rf /var/lib/apt/lists

### Install compiled libraries first so repackagaing MDID itself goes a little faster
# Install GFX
ADD http://www.swftools.org/swftools-0.9.2.tar.gz /opt/tools/swftools-0.9.2.tar.gz
RUN cd /opt/tools \
    && tar xzf swftools-0.9.2.tar.gz \
    && cd swftools-0.9.2 \
    && ./configure \
    && make -j4

# Install FFMPEG
ADD http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 /opt/ffmpeg/ffmpeg-snapshot.tar.bz2
RUN cd /opt/ffmpeg \
    && tar xjf ffmpeg-snapshot.tar.bz2 \
    && cd ffmpeg \
    && PATH="/opt/ffmpeg/bin:$PATH" \
    PKG_CONFIG_PATH="/opt/ffmpeg/lib/pkgconfig" \
    ./configure \
    --prefix="/opt/ffmpeg" \
    --pkg-config-flags="--static" \
    --extra-cflags="-I/opt/ffmpeg/include" \
    --extra-ldflags="-L/opt/ffmpeg/lib" \
    --bindir="/opt/ffmpeg/bin" \
    --enable-gpl \
    --enable-libass \
    --enable-libfreetype \
    --enable-libmp3lame \
    --enable-libtheora \
    --enable-libvorbis \
    --enable-libx264 \
    && PATH="/opt/ffmpeg/bin:$PATH" make -j4 install \
    && cp /opt/ffmpeg/bin/* /usr/local/bin \
    && cd .. \
    && rm -Rf ffmpeg-snapshot.tar.bz2 ffmpeg

# Actually start installing MDID itself
COPY . /opt/mdid
WORKDIR /opt/mdid

ENV DJANGO_SETTINGS_MODULE="rooibos_settings.local_settings"

# Install python packages and cleanup
RUN pip install --no-cache-dir --allow-external --upgrade -r requirements.txt \
    && mkdir /opt/mdid/log /opt/mdid/scratch /opt/mdid/storage /opt/mdid/static \
    && mv rooibos_settings/base_docker.py rooibos_settings/base.py \
    && mv rooibos_settings/docker_template.py rooibos_settings/local_settings.py \
    && python manage.py collectstatic --noinput \
    && apt-get purge -y build-essential yasm autoconf automake gcc g++ \
    && apt-get autoremove -y

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "rooibos.wsgi:application", "--log-config", "docker/gunicorn-logging.conf"]
