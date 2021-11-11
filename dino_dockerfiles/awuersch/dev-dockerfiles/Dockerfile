# OPAM for debian-10 with local switch of OCaml 4.05.0
FROM ocaml/ocaml:debian-10
LABEL distro_style="apt" distro="debian" distro_long="debian-10" arch="x86_64" ocaml_version="4.05.0" opam_version="1.2" git_user="awuersch" operatingsystem="linux"
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
  echo $TZ > /etc/timezone && \
  sh -c 'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg' && \
  mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
  echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list && \
  echo "deb [trusted=yes] http://debian.stanford.edu/debian-stanford stable main" > /etc/apt/sources.list.d/stanford.list && \
  echo "Package: *\nPin: release o=Stanford\nPin-Priority:200\n" > /etc/apt/preferences.d/stanford.pref && \
  echo "Package: libremctl1\nPin: release o=Stanford\nPin-Priority:600" >> /etc/apt/preferences.d/stanford.pref && \
  DEBIAN_FRONTEND=noninteractive apt-get -y update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install \
# to trace system calls
    strace \
# for opam dependency calculation
    aspcud \
# for opam async_ssl package
    libssl-dev \
# krb5 packages
    krb5-config \
    krb5-user \
    libsasl2-modules-gssapi-mit \
    krb5-k5tls \
    krb5-pkinit \
    kstart \
    remctl-client \
    wallet-client \
# fsharp and its IDE -- visual studio code
    fsharp \
    libgtk2.0-dev \
    libasound2 \
    dbus-x11 \
    code \
# vim and deoplete prerequisites
    gettext \
    python3 \
    python3-dev \
    python \
    python-dev \
    python-pip \
    python3-pip \
    ruby \
    ruby-dev \
    libncurses5-dev \
    libatk1.0-dev \
    libxpm-dev \
# pyenv prerequisites
    libxt-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncursesw5-dev \
    tk-dev \
# deoplete prerequisite
    cscope \
# for easy removal of dpkg packages
    checkinstall && \
  DEBIAN_FRONTEND=noninteractive apt-get -y autoremove && \
  DEBIAN_FRONTEND=noninteractive apt-get -y clean && \
  rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* && \
  gem install rake && \
  gem install rubocop && \
  wget https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz && \
  tar xf go1.9.2.linux-amd64.tar.gz && \
  mv go /usr/local && \
  rm go1.9.2.linux-amd64.tar.gz && \
# vim with language interpretation
  git clone https://github.com/vim/vim && \
  sh -c 'cd vim && \
     git pull && \
     git fetch && \
     ./configure \
       --enable-multibyte \
       --enable-rubyinterp=dynamic \
       --with-ruby-command=/usr/bin/ruby \
       --enable-pythoninterp=dynamic \
       --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \
       --enable-python3interp \
       --with-python3-config-dir=/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu \
       --enable-cscope \
       --enable-gui=auto \
       --with-features=huge \
       --with-x \
       --enable-fontset \
       --enable-largefile \
       --disable-netbeans \
       --with-compiledby="tony.wuersch@gmail.com" \
       --enable-fail-if-missing && \
     make && \
     make install' && \
# opam
  git clone -b 1.2 git://github.com/ocaml/opam /tmp/tony && \
  sh -c "cd /tmp/tony && make cold && make install && echo Not installing OPAM2 wrappers && rm -rf /tmp/tony" && \
# user environment setup
  echo 'tony ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/tony && \
  chmod 440 /etc/sudoers.d/tony && \
  chown root:root /etc/sudoers.d/tony && \
  adduser --disabled-password --gecos '' tony && \
  passwd -l tony && \
  chown -R tony:tony /home/tony
USER tony
ENV HOME /home/tony
WORKDIR /home/tony
RUN mkdir .ssh && \
  chmod 700 .ssh && \
  git config --global user.email "tony.wuersch@gmail.com" && \
  git config --global user.name "Tony Wuersch" && \
  sudo -u tony sh -c 'git clone \
    -b master \
    git://github.com/ocaml/opam-repository' && \
  sudo -u tony sh -c 'opam init -a -y \
    --comp 4.05.0 \
    /home/tony/opam-repository' && \
  sudo -u tony sh -c 'opam install -y \
    depext \
    travis-opam \
    merlin \
    astring \
    fpath \
    cmdliner \
    jbuilder \
    topkg \
    topkg-care \
    topkg-jbuilder \
    xmlm \
    xtmpl \
    utop \
    sexplib \
    ppx_sexp_conv \
    ounit \
    bisect_ppx \
    async_ssl' && \
  sudo -u tony sh -c 'opam source -y \
    async_ssl' && \
# Pyenv is for easy python virtualenv definition and access
  sh -c 'curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash' && \
  echo '' >> .bashrc && \
  echo 'set -o vi' >> .bashrc && \
  echo 'export VISUAL=vim' >> .bashrc && \
  echo 'export EDITOR=vim' >> .bashrc && \
  echo 'export LANG=C' >> .bashrc && \
  echo '' >> .bashrc && \
  echo 'vi() {' >> .bashrc && \
  echo '  vim "$@"' >> .bashrc && \
  echo '}' >> .bashrc && \
  echo '' >> .bashrc && \
  echo 'export PATH="/home/tony/.pyenv/bin:$PATH"' >> .bashrc && \
  echo 'eval "$(pyenv init -)"' >> .bashrc && \
  echo 'eval "$(pyenv virtualenv-init -)"' >> .bashrc && \
  pip2 install --user flake8 && \
  pip3 install --user flake8 && \
# install neovim Python support
  pip2 install --user neovim && \
  pip3 install --user neovim && \
  mkdir -p .vim/pack/plugins/start && \
  sh -c 'cd .vim/pack/plugins/start && \
# merlin prerequisite plugins
    git clone https://github.com/Shougo/deoplete.nvim.git && \
    git clone https://github.com/vim-syntastic/syntastic.git && \
    git clone https://github.com/ervandew/supertab.git && \
    git clone https://github.com/ctrlpvim/ctrlp.vim.git' && \
# vimrc definition
  echo 'syntax on' >> .vimrc && \
  echo 'filetype plugin indent on' >> .vimrc && \
  echo '' >> .vimrc && \
  echo "let g:opamshare = substitute(system('opam config var share'),'\\n$','','''')" >> .vimrc && \
  echo 'execute "set rtp+=" . g:opamshare . "/merlin/vim"' >> .vimrc && \
  echo 'let mapleader = "-"' >> .vimrc && \
  echo 'let maplocalleader = "\\"' >> .vimrc && \
  echo '' >> .vimrc && \
  echo 'set statusline+=%#warningmsg#' >> .vimrc && \
  echo 'set statusline+=%{SyntasticStatuslineFlag()}' >> .vimrc && \
  echo 'set statusline+=%*' >> .vimrc && \
  echo '' >> .vimrc && \
  echo 'let g:syntastic_always_populate_loc_list = 1' >> .vimrc && \
  echo 'let g:syntastic_auto_loc_list = 1' >> .vimrc && \
  echo 'let g:syntastic_check_on_open = 1' >> .vimrc && \
  echo 'let g:syntastic_check_on_wq = 0' >> .vimrc && \
  echo '' >> .vimrc && \
  echo "let g:syntastic_ocaml_checkers = ['merlin']" >> .vimrc && \
  echo "let g:syntastic_python_checkers = ['flake8']" >> .vimrc && \
  echo "let g:syntastic_ruby_checkers = ['rubocop','mri']" >> .vimrc && \
  echo "let g:syntastic_c_include_dirs = \
    ['.', 'include', 'lib/dns', \
     'lib/dns/include', 'lib/isc', \
     'lib/isc/include', 'lib/isc/unix/include', \
     'lib/isc/pthreads/include']" >> .vimrc

ENTRYPOINT [ "opam", "config", "exec", "--" ]
CMD [ "bash" ]
