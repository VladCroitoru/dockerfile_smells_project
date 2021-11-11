FROM fojas/rbenv-nvm

RUN yum -y install postgresql-devel && yum clean all

RUN rbenv install 2.1.5 && rbenv global 2.1.5
RUN cd && source .nvm/nvm.sh && nvm install 0.8.14

ENV PATH ~/.nvm/v0.8.14/bin:$PATH

