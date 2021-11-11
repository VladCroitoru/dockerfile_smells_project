FROM srp33/wishbuilder-cli-environment

WORKDIR /WishBuilder-CLI

ADD LICENSE /WishBuilder-CLI/
ADD README.md /WishBuilder-CLI/
ADD *.py /WishBuilder-CLI/
ADD run.sh /WishBuilder-CLI/

RUN chmod 777 /WishBuilder-CLI -R

CMD ["bash", "run.sh"]
