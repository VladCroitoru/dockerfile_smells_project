FROM crosbymichael/python

RUN apt-get update && apt-get install --yes libav-tools nodejs npm && pip install --upgrade youtube_dl httpie && ln -s /usr/bin/nodejs /usr/bin/node && npm install -g http-server && mkdir /http
WORKDIR /http

COPY example .
COPY demo-data .
RUN for v in $(find . -name youtube.url); do (export video=$(cat $v) && cd `dirname $v` && youtube-dl $video -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -o 1080p.mp4) done

CMD ./demo-data && http-server -p 8000
