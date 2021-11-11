from ubuntu:latest

MAINTAINER Naohiro Manago <manago.naohiro@chiba-u.jp>

ENV LANGUAGE=C.UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONIOENCODING=UTF-8 \
    PATH=/usr/local/anaconda3/bin:.:/bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin

RUN apt-get update --fix-missing && \
    apt-get upgrade -y && \
    apt-get install -y vim wget bzip2 curl grep sed dpkg \
    ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion npm ttf-freefont && \
    apt-get clean

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN npm install -g configurable-http-proxy

RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb

RUN wget --quiet https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /usr/local/anaconda3 && \
    rm ~/anaconda.sh

RUN conda update -y pip ipython jupyter jupyter_core jupyter_console jupyter_client ipywidgets

RUN conda install -y basemap netcdf4

RUN pip install jupyter_contrib_nbextensions jupyter-js-widgets-nbextension jupyter_nbextensions_configurator jupyterhub images2gif

COPY custom.js /usr/local/anaconda3/lib/python3.5/site-packages/notebook/static/custom/

COPY custom.css /usr/local/anaconda3/lib/python3.5/site-packages/notebook/static/custom/

COPY style.min.css /usr/local/anaconda3/lib/python3.5/site-packages/notebook/static/style/

COPY __init__.py /usr/local/anaconda3/lib/python3.5/site-packages/images2gif/

COPY images2gif.py /usr/local/anaconda3/lib/python3.5/site-packages/images2gif/

COPY jupyter_notebook_config.py /root/.jupyter/

RUN jupyter contrib nbextension install --user

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension

RUN curl http://www.cr.chiba-u.jp/~kuze-lab/temporary/VL2016.tar.bz2 | tar -xjC /root/

COPY exercise_main.js /root/.local/share/jupyter/nbextensions/exercise/main.js

COPY exercise2_main.js /root/.local/share/jupyter/nbextensions/exercise2/main.js

COPY exercise2_main.css /root/.local/share/jupyter/nbextensions/exercise2/main.css

RUN mkdir /root/.jupyter/nbconfig

COPY notebook.json /root/.jupyter/nbconfig/

COPY tree.json /root/.jupyter/nbconfig/

RUN ipython profile create

RUN echo "c.InlineBackend.rc = {'image.cmap':'gray'}" >>/root/.ipython/profile_default/ipython_config.py

WORKDIR /root/VL2016

EXPOSE 8888

ENTRYPOINT ["tini", "--"]

CMD ["jupyter", "notebook", "--no-browser"]
