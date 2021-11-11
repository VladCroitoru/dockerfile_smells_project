FROM microsoft/azure-cli
MAINTAINER Isaac Stefanek <isaac@wirestorm.us>

ENV AZURE_CONFIG_MODE asm

COPY utilities /utilities
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["azure"]
