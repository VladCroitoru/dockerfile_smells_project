FROM python:3.8.11-alpine

ENV UNO_URL https://raw.githubusercontent.com/dagwieers/unoconv/master/unoconv
ENV TG_TOKEN=''

RUN apk update && \
    apk upgrade --no-cache && \
    apk add build-base && \
    apk add util-linux

RUN apk add --no-cache bash \
    curl \
    libreoffice-common \
    libreoffice-writer \
    ttf-droid-nonlatin \
    ttf-droid \
    ttf-dejavu \
    ttf-freefont \
    ttf-liberation \
    ttf-opensans \
    ttf-freefont \
    ttf-inconsolata \
    terminus-font \
    && curl -Ls $UNO_URL -o /usr/local/bin/unoconv \
    && chmod +x /usr/local/bin/unoconv

# install ms-fonts
RUN apk --no-cache add msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f -v

# install Google fonts
# RUN wget https://github.com/google/fonts/archive/main.tar.gz -O gf.tar.gz
# RUN tar -xf gf.tar.gz
# RUN mkdir -p /usr/share/fonts/truetype/google-fonts
# RUN find $PWD/fonts-main/ -name "*.ttf" -exec install -m644 {} /usr/share/fonts/truetype/google-fonts/ \; || return 1
# RUN rm -f gf.tar.gz
# RUN fc-cache -f && rm -rf /var/cache/*

WORKDIR /home

# install
COPY requirements.txt main.py ./
RUN pip install --upgrade pip && pip install -U pip install -r requirements.txt

# Remove the extracted fonts directory
# Remove the following line if you're installing more applications
# after this RUN command and you have errors while installing them
RUN apk del curl && rm -rf $PWD/fonts-main && rm -rf /var/cache/*

#COPY *.doc ./
#RUN apk -v cache clean
ENTRYPOINT ["python", "main.py"]