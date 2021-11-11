FROM ansibleplaybookbundle/apb-base

RUN yum install -y jq && yum clean all
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | DESIRED_VERSION="v2.8.2" bash

USER apb

COPY entrypoint.sh /usr/bin/hbb-entrypoint.sh

ENTRYPOINT ["hbb-entrypoint.sh"]
