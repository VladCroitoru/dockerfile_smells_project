From alpine:edge

RUN apk add --update \
	python3 py-pip unzip libexif \
    udev chromium chromium-chromedriver xvfb \
    ttf-freefont

RUN mkdir /noto && \
    cd /noto && \
    wget https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip && \
    unzip NotoSansCJKjp-hinted.zip && \
    mkdir -p /usr/share/fonts/noto && \
    cp *.otf /usr/share/fonts/noto && \
    chmod 644 -R /usr/share/fonts/noto/ && \
    fc-cache -fv && \
    rm -rf /noto

RUN pip3 install selenium pyvirtualdisplay awscli boto3 requests pytz

ADD init.sh /tmp/init.sh
WORKDIR /tmp

CMD ["/tmp/init.sh"]
