FROM ubuntu:15.10

MAINTAINER findcoo <powzxc@gmail.com>

RUN apt-get update && \
	    apt-get install -y build-essential\
	    			git curl wget bash-completion \
				openssh-server gfortran sudo make \
				cmake libssl-dev libreadline-dev llvm \
				libsqlite3-dev libmysqlclient-dev python-dev \
				python3-dev zlib1g-dev libbz2-dev language-pack-ko	
RUN mkdir /var/run/sshd && \
	useradd -m User -s /bin/bash && \
	echo 'root:root' | chpasswd && \
	echo 'User:User' | chpasswd && \
	echo 'User 	ALL=(ALL) 	ALL' >> /etc/sudoers.d/User && \
	sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
 	sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
	locale-gen ko_KR.UTF-8 
WORKDIR /home/User
ENV HOME /home/User

RUN git clone https://github.com/yyuu/pyenv.git $HOME/.pyenv
ENV PYENV_ROOT $HOME/.pyenv 
ENV PATH $PYENV_ROOT/bin:$HOME/bin:$PATH
RUN echo 'export PYENV_ROOT='$PYENV_ROOT >> $HOME/.bashrc && \
	echo 'export PATH='$PATH >> $HOME/.bashrc && \
	echo 'eval "$(pyenv init -)"' >> $HOME/.bashrc && \
	exec $SHELL

#pyenv install and setting
ENV EXEC_PYENV $PYENV_ROOT/bin/pyenv 
RUN $EXEC_PYENV install 2.7.10 && \
	$EXEC_PYENV install 3.5.1 && \
	$EXEC_PYENV global 2.7.10 3.5.1 && \
	$EXEC_PYENV rehash 

#building vim, using for pyenv
RUN mkdir build_vim
WORKDIR $HOME/build_vim
ENV PYENV_VERSIONS=$PYENV_ROOT/versions \
	VIM_URL=https://github.com/vim/vim.git

RUN echo 'export PYENV_VERSIONS='$PYENV_VERSIONS >> $HOME/.bashrc

RUN git clone $VIM_URL
WORKDIR $HOME/build_vim/vim
RUN ./configure --with-features=huge \
		--enable-multibyte \
		--enable-rubyinterp \
		--enable-pythoninterp=dynamic \
		--with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \
		--enable-python3interp=dynamic \
		--with-python3-config-dir=/usr/lib/python3.4/config-3.4m-x86_64-linux-gnu \
		--disable-gui --enable-cscope --prefix=/usr
RUN make VIMRUNTIMEDIR=/usr/share/vim/vim74 && \
	make install
WORKDIR $HOME
RUN rm -rf ./build_vim

#-- default vimrc setting
RUN echo "\n\n\"vimrc default setting" \ 
	"\nnmap <leader>l :set list!<CR>" \
	"\nset nu" \
	"\nset autochdir" \
	"\nset ts=4" \ 
	"\nset bs=4" \
	"\nset noexpandtab" \
	"\nset nocompatible" \
	"\nsyntax on" >> $HOME/.vimrc
RUN ln -s /usr/bin/vim /usr/bin/vi

#-- neobundle install
ENV NEOBUNDLE https://raw.githubusercontent.com/Shougo/neobundle.vim/master/bin/install.sh
RUN curl $NEOBUNDLE > install.sh && \
	    sh ./install.sh && \
	    rm ./install.sh

#-- install and setup vim plugins

RUN echo "\n\n\"neobundle start" \
	    "\nset runtimepath+=~/.vim/bundle/neobundle.vim/" \
	    "\ncall neobundle#begin(expand('~/.vim/bundle/'))" \
	    "\nNeoBundleFetch 'Shougo/neobundle.vim'" \
	    "\nNeoBundle 'davidhalter/jedi-vim'" \
	    "\nNeoBundle 'tpope/vim-fugitive'" \
	    "\nNeoBundle 'scrooloose/nerdtree'" \
	    "\nNeoBundle 'ervandew/supertab'" \
	    "\nNeoBundleLazy 'lambdalisue/vim-pyenv', {" \
	    "\n\t\ 'depends': ['davidhalter/jedi-vim']," \
	    "\n\t\ 'autoload': {" \
	    "\n\t\t\ 'filetypes': ['python', 'python3']," \
	    "\n\t\ }}" \
	    "\ncall neobundle#end()" \
	    "\nNeoBundleCheck" >> $HOME/.vimrc && \
	echo "\n\n\"supertab setting" \
		"\nlet g:SupperTabDefaultCompletionType = \"context\"" >> $HOME/.vimrc && \
	echo "\n\n\"jedi setting" \
	    	"\nlet g:jedi#completions_enabled = 0 " \
		"\nau FileType python let g:jedi#completions_enabled = 1" >> $HOME/.vimrc && \
	echo "\n\n\"vim-pyenv setting" \
	    	"\nif jedi#init_python()" \
		"\n\tfunction! s:jedi_auto_force_py_version() abort" \
		"\n\t\tlet major_version = pyenv#python#get_internal_major_version() " \
		"\n\t\tcall jedi#force_py_version(major_version)" \
		"\nendfunction" \
		"\naugroup vim-pyenv-custom-augroup" \
		"\n\t\tautocmd! *" \
		"\n\t\tautocmd User vim-pyenv-activate-post call s:jedi_auto_force_py_version()" \
		"\n\t\tautocmd User vim-pyenv-deactivate-post call s:jedi_auto_force_py_version()" \
		"\n\taugroup END" \
		"\nendif" >> $HOME/.vimrc 


RUN mkdir -p $HOME/src && \
	chown -R User:User $HOME
VOLUME $HOME/src

EXPOSE 100-1024 5000-5999 8000-8999 9000-9999

CMD ["/usr/sbin/sshd", "-D"]
