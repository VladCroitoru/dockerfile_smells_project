# vim:set ft=dockerfile:
FROM vertexproject/synapse:v0.0.55

COPY storm-tutorial/ /storm-tutorial/
RUN python /storm-tutorial/ingest.py sqlite:////storm-tutorial/tutorial-core.db /storm-tutorial/ingests/

ENTRYPOINT ["/bin/bash", "/storm-tutorial/entrypoint.sh"]
