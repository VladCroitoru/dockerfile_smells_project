FROM docker.pkg.github.com/navikt/pus-decorator/pus-decorator

# medfører 2 ting i pus-decorator:
#  - /environment.js-endepunktet legger public properties på window.aktivitetsplan
#  - applikasjonen får /aktivitetsplan som contextpath i begge soner
ENV APPLICATION_NAME=aktivitetsplan
ENV GZIP_ENABLED=true
ENV FOOTER_TYPE=WITHOUT_ALPHABET
ENV EXTRA_DECORATOR_PARAMS='&chatbot=false'

COPY /build /app

ADD decorator.yaml /decorator.yaml
ADD decorator-fss.yaml /decorator-fss.yaml
