FROM ubuntu:14.04.4

COPY run.sh /code/run.sh
COPY run_python_workers.py /code/run_python_workers.py

WORKDIR /code

# Make sure this is the exec form of ENTRYPOINT (not the shell form) so that `run.sh` is PID 1
ENTRYPOINT ["./run.sh"]
