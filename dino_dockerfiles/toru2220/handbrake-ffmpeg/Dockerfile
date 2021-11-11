FROM	offbytwo/ffmpeg:latest as ffmpeg

FROM	djaydev/handbrake:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && apt-get upgrade -y && \
    apt-get -y install --no-install-recommends \
    libnuma1 \
    libssl1.1 \
    libfreetype6 \
    bash \
    lsdvd \
    locales \
    python3 \
    python3-pip \
    libxml2-utils \
    && apt-get -y clean && rm -r /var/lib/apt/lists/*

ENV TZ=Asia/Toyko
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /opt/ffmpeg
COPY --from=ffmpeg /opt/ffmpeg .

RUN ln -s /opt/ffmpeg/share/model /usr/local/share/
RUN ldconfig

ENV PATH="/opt/ffmpeg/bin:$PATH"
ENV PKG_CONFIG_PATH="/opt/ffmpeg/lib/pkgconfig"

RUN echo "ja_JP UTF-8" > /etc/locale.gen && locale-gen

ENV LANG=ja_JP.UTF-8

RUN pip3 install lxml

VOLUME	/data
WORKDIR	/data


