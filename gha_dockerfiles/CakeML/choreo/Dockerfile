FROM cakeml/cakeml

RUN mkdir bakery/
COPY --chown=cake . bakery/

RUN cd bakery/semantics && Holmake
RUN cd bakery/semantics/proofs && Holmake
RUN cd bakery/projection && Holmake
RUN cd bakery/projection/proofs && Holmake bakery_to_endpointProofTheory.{sml,ui,uo}
