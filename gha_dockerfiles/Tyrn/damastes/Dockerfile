FROM python:3.9.6-slim AS base

ARG user=damastes project=damastes src=src

# Non-root user.
RUN useradd -ms /bin/bash "$user"
USER $user
WORKDIR /home/$user
ENV PATH=/home/$user/.local/bin:$PATH

# Project.
RUN pip install poetry==1.1.11 --user && \
    mkdir /home/$user/$project
WORKDIR /home/$user/$project
COPY $src ./$src/
COPY pyproject.toml poetry.lock README.rst ./

# Build.
RUN poetry config virtualenvs.create true && \
    poetry install --no-dev && \
    poetry build -f sdist

FROM python:3.9.6-slim

ARG user=damastes project=damastes

# Non-root user.
RUN useradd -ms /bin/bash "$user"
USER $user
WORKDIR /home/$user
ENV PATH=/home/$user/.local/bin:$PATH

COPY --from=base /home/$user/$project/dist/ ./dist/
RUN pip install ./dist/* --user && \
    echo 'alias dm=damastes' >> .bashrc

CMD ["bash"]
