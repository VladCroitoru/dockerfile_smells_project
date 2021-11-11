FROM vikraman/ghc-mutable-cnf

ADD . /root/cnf-mutable-tests
WORKDIR /root/cnf-mutable-tests

ENV STACK_YAML stack-cnf.yaml

RUN stack build
RUN stack test
