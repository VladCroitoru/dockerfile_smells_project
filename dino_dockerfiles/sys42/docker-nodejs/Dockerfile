FROM sys42/docker-build-essentials:1.1.0

MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>

COPY _install_nvm_and_node_ /

RUN chmod +x _install_nvm_and_node_ \
 && sudo -iu app /_install_nvm_and_node_ \
 && rm _install_nvm_and_node_

ENTRYPOINT ["my_init", "--"]
