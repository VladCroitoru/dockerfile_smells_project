FROM python:3.8-slim AS build

LABEL "org.opencontainers.image.source" = "https://github.com/ahmubashshir/genshin-check-in"
LABEL "maintainer" = "Mubashshir <ahmubashshir@gmail.com>"

WORKDIR /build

RUN addgroup --system user && adduser --system --no-create-home --ingroup user user
RUN chown user:user .
RUN chmod 755 .
USER user

COPY genshin_check_in ./genshin_check_in
COPY poetry.lock      .
COPY pyproject.toml   .

RUN python3 -m venv venv
ENV PATH="/build/venv/bin:$PATH"
ENV HOME=/build

RUN pip --no-cache-dir --disable-pip-version-check --no-input install poetry
RUN poetry build
RUN rm -rf venv
RUN python3 -m venv venv
RUN pip --no-cache-dir --disable-pip-version-check install dist/genshin-check-in-$(sed -nE 's/^version = "([0-9.]+)"/\1/p' pyproject.toml).tar.gz



FROM python:3.8-slim
COPY --from=build /build/venv /dist

RUN addgroup --system user && adduser --system --no-create-home --ingroup user user
#RUN chmod -R 755 /dist/bin
ENV PATH="/dist/bin:$PATH"
USER user

ENTRYPOINT ["python3", "/dist/bin/genshin"]
