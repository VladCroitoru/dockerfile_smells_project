# Author: Yale Huang
#
# Usage: nvidia-docker run -it -p 8888:8888 --cap-add SYS_ADMIN --device /dev/fuse \
#            --security-opt apparmor=unconfined --name yale.huang.colaboratory \
#            yaleh/colaboratory-tensorflow \
#            /run_jupyter.sh --NotebookApp.token='' \
#                --NotebookApp.allow_origin='https://colab.research.google.com' \
#                --allow-root

FROM tensorflow/tensorflow:1.4.1-gpu

MAINTAINER Yale Huang <calvino.huang@gmail.com>

RUN pip install jupyter_http_over_ws
RUN jupyter serverextension enable --py jupyter_http_over_ws
RUN pip install --upgrade --ignore-installed notebook
RUN pip install keras

COPY run_jupyter.sh /

EXPOSE 8888/tcp

CMD ["/run_jupyter.sh"]

