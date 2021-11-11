FROM ubuntu:14.04.1
MAINTAINER densuke

# 日付周りを日本語向けに変更します
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    echo 'Asia/Tokyo' > /etc/timezone && date
# 日本向けマシンではハードウェアクロックはローカルタイムです
RUN sed -e 's;UTC=yes;UTC=no;' -i /etc/default/rcS

# ロケールを基本日本語に設定します
RUN echo 'LC_ALL=ja_JP.UTF-8' > /etc/default/locale && \
    echo 'LANG=ja_JP.UTF-8' >> /etc/default/locale && \
		locale-gen ja_JP.UTF-8
# リポジトリを日本語向けに変更します
RUN sed -e 's;http://archive;http://jp.archive;' -e  's;http://us\.archive;http://jp.archive;' -i /etc/apt/sources.list
RUN [ ! -x /usr/bin/wget ] && apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y wget && \
		touch /.get-wget
RUN wget -q https://www.ubuntulinux.jp/ubuntu-ja-archive-keyring.gpg -O- | apt-key add - && \
    wget -q https://www.ubuntulinux.jp/ubuntu-jp-ppa-keyring.gpg -O- | apt-key add - && \
		wget https://www.ubuntulinux.jp/sources.list.d/trusty.list -O /etc/apt/sources.list.d/ubuntu-ja.list

# システムを更新します
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y

# 後始末をします
RUN [ -f /.get-wget ] && \
    DEBIAN_FRONTEND=noninteractive apt-get purge --auto-remove -y wget && \
		rm -f /.get-wget
RUN apt-get clean

# デフォルトロケール(変数)を日本語向けに変更しておきます
ENV LC_ALL ja_JP.UTF-8
ENV LANG j_JP.UTF-8

