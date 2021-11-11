FROM dit4c/dit4c-container-x11:debian
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list && \
  echo "deb http://deb.torproject.org/torproject.org jessie main" >> /etc/apt/sources.list && \
  apt-key adv --keyserver keys.gnupg.net --recv-key 886DDD89

RUN apt-get update && \
  apt-get install -y \
    tor deb.torproject.org-keyring python-pip python-all-dev && \
  apt-get -t jessie-backports install -y torsocks midori && \
  apt-get clean

RUN pip install ipython jupyter

RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1) && \
  sed -i "${LNUM}ilauncher_item_app = /usr/share/applications/midori-private.desktop" /etc/tint2/panel.tint2rc

COPY etc /etc
COPY var /var

RUN su - researcher -c "mkdir -p ~/.jupyter && echo \"c.NotebookApp.base_url = '/jupyter'\" > ~/.jupyter/jupyter_notebook_config.py"

ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/torsocks/libtorsocks.so
