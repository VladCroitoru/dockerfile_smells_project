FROM laudio/pyodbc:1.0.33 AS main

WORKDIR /app

COPY ["setup.py", "README.md", "main.py", "./"]

RUN pip install --upgrade pip && pip install .

COPY . .

ENTRYPOINT [ "./docker-entrypoint.sh" ]


# STAGE: test
# -----------
# Image used for running tests.FROM main AS test
FROM main AS test

RUN pip install .[dev]

COPY ["tests", "./"]

CMD pytest -vvv
