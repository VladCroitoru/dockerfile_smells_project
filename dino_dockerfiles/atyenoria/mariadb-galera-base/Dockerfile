FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y  software-properties-common
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
RUN add-apt-repository 'deb [arch=amd64,i386] http://ftp.yz.yamagata-u.ac.jp/pub/dbms/mariadb/repo/10.1/debian jessie main'

RUN apt-get update && apt-get -y --no-install-recommends --no-install-suggests install host socat unzip ca-certificates wget rsync curl dnsutils
RUN apt-get -y install mariadb-server mariadb-client xtrabackup galera


RUN wget -O /bin/galera-healthcheck 'https://github.com/sttts/galera-healthcheck/releases/download/v20150303/galera-healthcheck_linux_amd64'
RUN test "$(sha256sum /bin/galera-healthcheck | awk '{print $1;}')" = "86f60d9d82b1f9d2d474368ed7e81a0a361508031a292244847136b0ed2ee770"
RUN chmod +x /bin/galera-healthcheck




RUN apt-get install -y software-properties-common build-essential zsh git jq s3cmd
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git /root/.oh-my-zsh && \
    cp -R /root/.oh-my-zsh /laravel && \
    chsh -s /bin/zsh


RUN wget https://releases.hashicorp.com/consul-template/0.13.0/consul-template_0.13.0_linux_amd64.zip -O consul-template.zip && \
    unzip consul-template.zip && \
    mv consul-template /usr/local/bin && \
    rm consul-template.zip


RUN wget https://github.com/major/MySQLTuner-perl/tarball/master
RUN tar xf master
RUN mv major-MySQLTuner-perl-*/mysqltuner.pl /usr/local/bin



#vim plugin
RUN apt-get install -y vim
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
RUN git clone https://github.com/atyenoria/vim-pathogen.git ~/.vim.tmp && \
    ln -sf ~/.vim.tmp/autoload/pathogen.vim ~/.vim/autoload/pathogen.vim && \
    git clone https://github.com/atyenoria/nerdcommenter.git ~/.vim/bundle/nerdcommenter && \
    git clone https://github.com/atyenoria/delimitMate.git ~/.vim/bundle/delimitMate && \
    git clone https://github.com/atyenoria/PDV--phpDocumentor-for-Vim.git ~/.vim/bundle/phpDocumentor && \
    git clone https://github.com/atyenoria/vim-colorschemes.git ~/.vim/bundle/colorschemes && \
    git clone https://github.com/atyenoria/vim-misc.git ~/.vim/bundle/vim-misc && \
    git clone https://github.com/atyenoria/vim-colorscheme-switcher.git ~/.vim/bundle/colorscheme-switcher
ADD .vimrc /root/.vimrc


EXPOSE 3306 4444 4567 4568
