FROM ternandsparrow/natcap-invest-docker:1.1.4_3.8.9 AS withDeps

WORKDIR /app/
ADD docker/setup1.sh docker/setup1.sh
ADD requirements.txt .
RUN /bin/bash docker/setup1.sh


FROM withDeps
ADD . /app/
RUN docker/setup2.sh
USER nidfuser:nidfuser
ENTRYPOINT [ "/bin/bash", "docker/run.sh" ]
