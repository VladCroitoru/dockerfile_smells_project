FROM registry.novisci.com/nsstat/statocker/haskell:8.10.4

COPY cabal.project .
COPY hasklepias-core/hasklepias-core.cabal hasklepias-core/hasklepias-core.cabal
COPY hasklepias-templates/hasklepias-templates.cabal hasklepias-templates/hasklepias-templates.cabal
COPY hasklepias-main/hasklepias-main.cabal hasklepias-main/hasklepias-main.cabal
COPY cohort-collector/cohort-collector.cabal cohort-collector/cohort-collector.cabal
COPY edm/edm.cabal edm/edm.cabal
COPY stype/stype.cabal stype/stype.cabal

RUN cabal update
RUN cabal build all --only-dependencies