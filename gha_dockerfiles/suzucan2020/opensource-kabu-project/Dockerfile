# コードを実行するコンテナイメージ
FROM python:3.8

# 必要なコマンドのインストールを行う
RUN apt-get -y update && apt-get install -y wget vim git curl make sudo

# 日本語設定
RUN apt-get install -y locales
RUN echo "ja_JP UTF-8" > /etc/locale.gen
RUN locale-gen

# TA-Libのインストールを行う
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib/ && \
    ./configure --prefix=/usr && \
    make && \
    make install

RUN pip install ta-lib
RUN pip install pandas
RUN pip install python-highcharts
RUN pip install yahoo_finance_api2
RUN pip install matplotlib
RUN pip install colorlog
RUN pip install lxml

# アクションのリポジトリからコードファイルをコンテナのファイルシステムパス `/`にコピー
COPY entrypoint.sh /entrypoint.sh

# dockerコンテナが起動する際に実行されるコードファイル (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]

# COPY ./work /tmp
# WORKDIR /tmp/work

# CMD ["ls -l"]
