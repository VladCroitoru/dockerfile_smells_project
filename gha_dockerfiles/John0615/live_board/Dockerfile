FROM registry2.leangoo.com:4443/library/alpine_base:3.12.3 as app_base

# ---------------------------------------------------------
# 准备依赖包并预先对依赖包进行编译
# 只要依赖包没有发生变化，这一步能够节省40%~50%总编译时间
FROM registry2.leangoo.com:4443/library/elixir_base:1.12.2-alpine as base_deps

# 支持通过构建命令行指定 MIX_ENV, 并固化到环境变量中, 缺省为 prod
ARG MIX_ENV
ENV MIX_ENV=${MIX_ENV:-"prod"}
RUN echo "DEBUG: MIX_ENV => ${MIX_ENV}"

RUN mkdir /app
COPY mix.exs /app
COPY mix.lock /app

WORKDIR /app
RUN mix deps.get \
 && mix deps.compile

# ---------------------------------------------------------
# asset 依赖基本
FROM node:14 as asset_deps

WORKDIR /build/apps/live_board/assets
COPY assets/package.json .
COPY assets/package-lock.json .
RUN npm install


# ---------------------------------------------------------
# 用node打包js资源
FROM asset_deps as asset_builder

WORKDIR /build/apps/live_board/assets
COPY assets .
# 此处需要把phoenix的依赖包复制到相应的路径中
COPY --from=base_deps /app/deps/phoenix /build/apps/live_board/deps/phoenix
COPY --from=base_deps /app/deps/phoenix_html /build/apps/live_board/deps/phoenix_html
RUN npm run deploy

# ---------------------------------------------------------
# application release 构建
FROM base_deps as app_builder

# ARG SECRET_KEY_BASE

RUN mkdir -p /app
COPY . /app
WORKDIR /app

COPY --from=asset_builder /build/apps/live_board/priv/static priv/static
RUN mix phx.digest
RUN mix do release

# ---------------------------------------------------------
# 打包成最终镜像
FROM app_base
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk upgrade --no-cache && \
    apk add --no-cache bash openssl libgcc libstdc++ ncurses-libs

# 支持通过构建命令行指定 MIX_ENV, 并固化到环境变量中, 缺省为 prod
# ARG不会跨层传递，此处需要重新指定
ARG MIX_ENV
ENV MIX_ENV=${MIX_ENV:-"prod"}

RUN echo "DEBUG: MIX_ENV => ${MIX_ENV}"

WORKDIR /app
COPY --from=app_builder /app/_build/$MIX_ENV/rel/live_board .

CMD ["/app/bin/live_board", "start"]