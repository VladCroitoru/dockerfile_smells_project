FROM quay.io/packit/base

ENV USER=packit \
    HOME=/home/packit

COPY files/install-deps.yaml /src/files/
RUN cd /src/ \
    && ansible-playbook -vv -c local -i localhost, files/install-deps.yaml \
    && dnf clean all

COPY setup.py setup.cfg files/recipe.yaml /src/
# setuptools-scm
COPY .git /src/.git
COPY packit_service_fedmsg/ /src/packit_service_fedmsg/

RUN cd /src/ \
    && ansible-playbook -vv -c local -i localhost, recipe.yaml \
    && rm -rf /src/

CMD ["listen-to-fedora-messaging"]
