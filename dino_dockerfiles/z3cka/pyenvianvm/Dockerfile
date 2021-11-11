# c9 on debian + Pyenv
FROM z3cka/c9
MAINTAINER Casey Grzecka <c@sey.gr>

# Install Pyenv deps
RUN apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl libcurl4-openssl-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

# Install pyenv
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# pyenv-virtualenv
# already installed #RUN git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# pyenv-virtualenvwrapper
RUN git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

RUN source ~/.bashrc
