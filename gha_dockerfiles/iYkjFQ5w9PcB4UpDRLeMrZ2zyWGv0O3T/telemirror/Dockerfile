FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Clonning repo
COPY . .

# Install requirements
RUN pip3 install -U -r requirements.txt
# Run
CMD python3 app/telemirror.py
