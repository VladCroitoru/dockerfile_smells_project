FROM miseyu/docker-ubuntu16-python3.6

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y unzip gcc \
    zlib1g-dev libgconf-2-4 libgtk-3-0 libasound2-dev libssl-dev libbz2-dev \
    libreadline-dev wget libxml2-dev libxslt1-dev g++ udev ttf-freefont \
    xvfb gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable firefox && \
    apt-get clean

ENV TZ Asia/Tokyo

RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz -P /usr/local && \
    tar xvzf /usr/local/geckodriver-v0.19.0-linux64.tar.gz -C /usr/bin
