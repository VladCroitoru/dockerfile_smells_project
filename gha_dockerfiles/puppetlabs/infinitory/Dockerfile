FROM python:3.10-rc-buster
ADD README.md /
ADD generate.py /
ADD setup.py /
ADD infinitory /infinitory
ENV TOKEN $TOKEN
ENV BUCKET $BUCKET
ENV GOOGLE_APPLICATION_CREDENTIALS $GOOGLE_APPLICATION_CREDENTIALS
RUN pip install --upgrade pip
RUN python setup.py install
ENTRYPOINT python generate.py ${PDB_HOST} ${TOKEN} ${BUCKET}