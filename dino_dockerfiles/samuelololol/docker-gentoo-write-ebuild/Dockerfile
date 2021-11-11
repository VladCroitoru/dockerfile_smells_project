FROM samuelololol/docker-gentoo-websync
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN rm /sbin/unix_chkpwd
RUN echo ">=dev-lang/python-2.7.12:2.7 sqlite" >> /etc/portage/package.use/layman
RUN echo ">=dev-lang/python-3.4.5 sqlite" >> /etc/portage/package.use/layman
RUN echo "app-portage/layman git mercurial sqlite subversion" >> /etc/portage/package.use/layman
RUN emerge -uv layman eix gentoolkit vim app-portage/repoman

RUN mkdir -p /usr/local/portage/{metadata,profiles}
RUN chown -R portage:portage /usr/local/portage

#repo_name of local repo
RUN echo 'localrepo' > /usr/local/portage/profiles/repo_name

#layout.conf of local repo
RUN echo 'masters = gentoo' > /usr/local/portage/metadata/layout.conf
RUN echo 'auto-sync = false' >> /usr/local/portage/metadata/layout.conf

#localrepo.conf of local repo
RUN echo '[localrepo]' > /etc/portage/repos.conf/localrepo.conf
RUN echo 'location = /usr/local/portage' >> /etc/portage/repos.conf/localrepo.conf
#only used for local test
#COPY portage /usr/local/portage

#update eix database
RUN eix-update

#add command alias
RUN echo "alias l='ls -l'" >> /root/.bashrc
RUN echo "alias lh='l -h'" >> /root/.bashrc
RUN echo "alias la='l -a'" >> /root/.bashrc
