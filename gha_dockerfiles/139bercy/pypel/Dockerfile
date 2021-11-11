FROM python:3.8 as build

WORKDIR /code

COPY . .

RUN ["python", "setup.py", "sdist", "bdist_wheel"]

FROM python:3.8 as production

COPY --from=build /code/dist/pypel-*.whl /code/

RUN pip install /code/pypel-*.whl

CMD ["python", "-c", "import pypel"]
