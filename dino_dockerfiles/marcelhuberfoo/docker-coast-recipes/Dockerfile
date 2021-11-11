FROM marcelhuberfoo/arch

MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>

USER root

RUN echo -e '[infinality-bundle]\nSigLevel=Never\nServer = http://bohoomil.com/repo/$arch\n[infinality-bundle-fonts]\nSigLevel=Never\nServer = http://bohoomil.com/repo/fonts' >> /etc/pacman.conf
RUN pacman -Syy && \
    printf "\\ny\\ny\\n" | pacman -S  multilib-devel && \
    printf "y\\ny\\n" | pacman -Scc
RUN pacman -S --noconfirm --quiet --noprogressbar --needed python2 git lib32-openssl lib32-zlib gdb doxygen graphviz \
    fontconfig-infinality-ultimate ibfonts-meta-base && \
    printf "y\\ny\\n" | pacman -Scc
RUN rm -f /var/lib/pacman/sync/*.db

ADD entrypoint.sh /
ADD pip.conf /$UNAME/.pip/
RUN sed -i "s|USER|$UNAME|" /$UNAME/.pip/pip.conf
RUN chown -R $UNAME:$GNAME /$UNAME/

USER $UNAME
ENV VENVDIR=/$UNAME/.venv27scons
RUN echo "[[ -d \"\$VENVDIR\" ]] && . $VENVDIR/bin/activate" >> $HOME/.bashrc

RUN cd $HOME && git clone --single-branch --branch master --depth 1 https://github.com/pypa/virtualenv.git
RUN python2 $HOME/virtualenv/virtualenv.py $VENVDIR
RUN cd $HOME && git clone --single-branch --branch master --depth 1 https://gerrit.coast-project.org/p/coast.git
RUN cd $HOME/coast && \
    git clone --single-branch --branch master --depth 1 https://gerrit.coast-project.org/p/boost.git 3rdparty/boost &&\
    git clone --single-branch --branch master --depth 1 https://gerrit.coast-project.org/p/wdscripts.git && \
    git clone --single-branch --branch master --depth 1 https://gerrit.coast-project.org/p/recipes.git

RUN bash -l -c 'pip install -U -r $HOME/coast/requires.txt'

RUN bash -l -c 'cd $HOME/coast && \
      scons -u --jobs=$(nproc) --with-src-boost=3rdparty/boost --ignore-missing --doxygen-only && \
      scons -u --jobs=$(nproc) CoastRecipes --with-src-boost=3rdparty/boost && \
      cd apps/CoastRecipes && ln -s ../../doc/Coast/html COASTDoc'

USER root

EXPOSE 51200 51201

ENTRYPOINT ["/entrypoint.sh"]
CMD ["dummy"]

