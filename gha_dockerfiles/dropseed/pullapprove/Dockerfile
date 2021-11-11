FROM python:3

RUN pip install -U pip && pip install pullapprove==3.15.0

RUN echo '#!/bin/sh -ex\npullapprove $@' > /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
