FROM frolvlad/alpine-glibc:alpine-3.6
USER root

ENV ANACONDA_VERSION 4.4.0
ENV ANACONDA_INSTALL_SH Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh 
ENV ANACONDA_INSTALL_DIR /opt
ENV PATH /bin:/sbin:$ANACONDA_INSTALL_DIR/anaconda/bin:/usr/bin

ENV PASSWORD 'coolyaolei'

# Change mirror site For China
# RUN echo 'https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/main' > /etc/apk/repositories && \
#     echo 'https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/community' >> /etc/apk/repositories

# We need to install openssl so that wget can fetch from HTTPS
RUN apk update && \
    apk add --no-cache openssl

RUN apk add --no-cache tini

RUN wget https://repo.continuum.io/archive/$ANACONDA_INSTALL_SH
# China mirror site
# RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/$ANACONDA_INSTALL_SH

RUN apk add --no-cache bash libstdc++

# Actually install anaconda. We are pinning the anaconda version for trackability!

RUN mkdir -p $ANACONDA_INSTALL_DIR && \
     bash ./$ANACONDA_INSTALL_SH -b -p $ANACONDA_INSTALL_DIR/anaconda && \
     rm $ANACONDA_INSTALL_SH && \
     mkdir -p /notebook

RUN jupyter-notebook --generate-config --allow-root

VOLUME ['/notebook']

EXPOSE 8888

ENTRYPOINT [ "/sbin/tini", "--" ]

CMD echo c.NotebookApp.password =\'`python -c "from notebook.auth import passwd; print(passwd('$PASSWORD'),end='')"`\' >> /root/.jupyter/jupyter_notebook_config.py && \
jupyter-notebook --allow-root --no-browser --notebook-dir=/notebook --ip=0.0.0.0
