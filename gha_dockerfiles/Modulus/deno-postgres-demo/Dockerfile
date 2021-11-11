FROM denoland/deno:1.14.1 as builder

WORKDIR /opt/app

COPY . . 

RUN deno cache src/main.ts
# CMD deno run --allow-env=DATABASE_URL --allow-net=loremricksum.com,postgres,localhost src/main.ts
RUN deno compile --allow-env=DATABASE_URL --allow-net=loremricksum.com,postgres,localhost,postgres.demo.svc.cluster.local -o quotes src/main.ts


FROM gcr.io/distroless/cc-debian10

LABEL app=deno-demo

WORKDIR /opt/app

COPY --from=builder /opt/app .

# CMD ["/busybox/sh", "-c", "./quotes"]
ENTRYPOINT [ "/opt/app/quotes" ]

