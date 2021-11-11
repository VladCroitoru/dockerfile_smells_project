FROM fpco/stack-build:lts-9.10

RUN mkdir ~/.stack/global-project
COPY stack.yaml ~/.stack/global-project/

RUN stack setup 8.0.2

RUN stack install \
    QuickCheck \
    aeson \
    aeson-casing \
    attoparsec \
    bytestring \
    constraints \
    data-default \
    doctest \
    doctest-discover \
    extensible \
    hashable \
    hspec \
    hspec-discover \
    hspec-wai \
    hspec-wai-json \
    http-api-data \
    lens \
    lens-aeson \
    mtl \
    operational \
    optparse-generic \
    pipes \
    pipes-postgresql-simple \
    postgresql-simple \
    product-profunctors \
    profunctors \
    quickcheck-instances \
    random \
    resource-pool \
    safe \
    scientific \
    servant \
    servant-docs \
    servant-server \
    text \
    time \
    transformers \
    unordered-containers \
    uuid \
    uuid-types \
    wai \
    wai-logger \
    warp

CMD ["bash"]