FROM l3iggs/archlinux

MAINTAINER Matthew Eichler <matthew.eichler@aventinesolutions.nl>

RUN pacman --noconfirm -Suyy && pacman --noconfirm -S zsh sudo libyaml

ADD sudoers /etc/sudoers

ENV APP_HOME /opt/rubie
RUN useradd --home-dir $APP_HOME --shell /bin/zsh --user-group --groups users,wheel rubie
COPY locale.conf /etc/
COPY .zshrc install_bootstrap_gems.sh $APP_HOME/
RUN chown -Rv rubie $APP_HOME

# Set up  user + directory
USER rubie
WORKDIR $APP_HOME

# RVM for Rubies and Gems
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys '409B6B1796C275462A1703113804BB82D39DC0E3' && \
    curl -sSL https://get.rvm.io | bash -s stable --ruby=2.2.3

ENV PATH $PATH:$APP_HOME/.rvm/bin

RUN $APP_HOME/install_bootstrap_gems.sh && sudo pacman --noconfirm -S emacs-nox

ENTRYPOINT ["/bin/zsh"]
