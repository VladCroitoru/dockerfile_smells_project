FROM yamitzky/miniconda-neologd:miniconda3

WORKDIR /usr/src/app

RUN pip install \
      bottle==0.12.13 \
      gunicorn==19.7.1

COPY . /usr/src/app

ENV MECAB_DICDIR=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd

CMD [ "python", "-m", "bottle", "-b", "0.0.0.0:80", "main" ]
