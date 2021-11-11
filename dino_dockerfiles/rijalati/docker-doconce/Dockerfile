FROM jamiehewland/alpine-pypy:5.3.0
MAINTAINER ritchie.latimore@bluemedora.com

RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories \
    && apk --update --no-cache add git imagemagick texlive-full@testing a2ps diffutils make openssh \
    && pip install preprocess \
    && pip install Mako \
    && pip install sphinx --upgrade \
    && pip install ipython \
    && pip install -e git+https://github.com/ryan-roemer/sphinx-bootstrap-theme#egg=sphinx-bootstrap-theme \
    && pip install -e git+https://github.com/shkumagai/sphinxjp.themes.impressjs#egg=sphinxjp.themes.impressjs \
    && pip install -e git+https://github.com/kriskda/sphinx-sagecell#egg=sphinx-sagecell \
    && pip install -e git+https://bitbucket.org/hplbit/pygments-ipython-console#egg=pygments-ipython-console \
    && git clone https://github.com/hplgit/doconce.git \
    && cd doconce \
    && pypy setup.py install 

ENTRYPOINT ["/usr/local/bin/doconce"]