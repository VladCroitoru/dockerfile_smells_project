FROM spacemacs/emacs25:develop

SHELL ["/bin/bash", "-c"]
# copying the spacemacs file
ENV HOME=$UHOME
ENV VENV_NAME='venv'
ENV PYVERS='3.6.4'
ENV WORKON_HOME=${UHOME}/.Environments
ENV VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
ENV VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
ENV VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'


# update and installing necesary tools
# https://github.com/yyuu/pyenv/wiki/Common-build-problems
RUN apt-get update && apt-get upgrade -y \
&& apt-get install -y curl make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev  gcc libxml2-dev libxslt1-dev \
python3-pip python3-dev python3-tk && cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip

RUN pip3 install --upgrade 'jedi>=0.9.0' 'json-rpc>=1.8.1' 'service_factory>=0.1.5' \
      flake8 autoflake hy yapf ipython virtualenvwrapper \
 && mkdir -p ${WORKON_HOME} \
 && echo 'source $(which virtualenvwrapper.sh)' >> ${UHOME}/.bashrc \
 && echo 'mkvirtualenv venv3' >> ${UHOME}/.bashrc
 # cat pyenvinit >> ${UHOME}/.bashrc && \

COPY .spacemacs "${UHOME}/.spacemacs"
COPY private "${UHOME}/.emacs.d/private"
RUN install-deps

RUN source ${UHOME}/.bashrc

RUN chown -R ${UNAME} ${UHOME}  \
  && chgrp -R ${GNAME} ${UHOME}  \
  && chmod ug+rw -R ${UHOME} \
  && git config --global user.name serret887\
  && git config --global user.email serret887@gmail.com

#TODO is initializing the source file after I exit emacs fix that
