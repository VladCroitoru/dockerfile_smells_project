FROM node:5

RUN npm install -g markdown-pdf

COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]

VOLUME /in
VOLUME /out

CMD [ "markdown-pdf", "/in/in.md", "-o", "/out/out.pdf" ]
