FROM cell/playground:latest
ENV DOCKER_IMAGE="cell/cvim"
ENV DEFAULT_CMD=vim

RUN apt-get update &&\
  DEBIAN_FRONTEND=noninteractive apt-get install -qy --no-install-recommends python3 python3-pip &&\
  apt-get clean -y && rm -rf /var/lib/apt/lists/*

#vim
COPY material/skel      /etc/skel/
RUN apt-get update &&\
  DEBIAN_FRONTEND=noninteractive apt-get install -qy vim-nox git exuberant-ctags silversearcher-ag &&\
  apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\
  git clone --depth 1 https://github.com/junegunn/fzf.git /etc/skel/.fzf &&\
  /etc/skel/.fzf/install --bin &&\
  git clone --depth 1 https://github.com/gmarik/Vundle.vim.git /etc/skel/.vim/bundle/Vundle.vim &&\
  rm -rf /etc/skel/.vim/bundle/Vundle.vim/.git &&\
  ln -s /etc/skel/.vim /root/ &&\
  vim -u /etc/skel/.vimrc +PluginInstall +qall &&\
  rm -rvf /tmp/*
#https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
RUN pip install --no-cache-dir --system \
      yamllint black flake8 flake8-markdown \
      bashate &&\
  rm -rvf /tmp/*

#Material
COPY material/scripts   /usr/local/bin/
COPY material/payload   /opt/payload/
COPY material/profile.d /etc/profile.d/

