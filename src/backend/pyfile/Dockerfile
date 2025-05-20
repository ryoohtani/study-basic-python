# 開発環境と本番環境の共通部分 baseはただの名前
FROM ubuntu:24.10 AS base
USER root

# コンテナの初期設定
# 開発環境と本番環境共に共通設定
WORKDIR /src/backend/pyfile
EXPOSE 8020
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# パッケージの更新とリナックスコマンドの導入
#RUN apt update && apt install -y vim less sudo tree curl
RUN apt update && apt install -y \
    vim \
    less \
    sudo \
    tree \
    curl
# 日本語化のパッケージ
# RUN apt install -y fonts-takao-gothic
RUN apt update && apt install -y fonts-noto-cjk
# PostgreSQLを使用するための開発パッケージをインストール
RUN apt update && apt install -y libpq-dev
# x11-appsのインストール(tkinterを使う場合必要又はドッカーからホストに対して通信を行う場合)
RUN apt update && apt install -y x11-apps
# Pythonのインストール
RUN apt update && apt install -y python3.12
# pipのインストール
RUN apt update && apt install -y python3-pip
# python3-tkのインストール(tkinterを使う場合必要)
RUN apt update && apt install -y python3-tk
# パッケージインストールのためにvenvの仮想環境を準備
# 下記も3.13にするとエラーになる。推測だがまだPython3.13が新しくてvenvが3.13が安定していなくてDLできないかも
RUN apt update && apt install -y python3.12-venv
# venv(仮想環境)の作成先 
RUN python3 -m venv /src/backend/pyfile/venv
# dockerファイルと同じ階層にrequirements.txt配置すること
COPY ./requirements.txt /src/backend/pyfile/
# venvからdocker環境内にあるrequirements.txtをインストールする処理
RUN /src/backend/pyfile/venv/bin/pip install -r /src/backend/pyfile/requirements.txt
# ホストPCのカレントディレクトリまたはコンテナ側からファイル等をコピー
COPY . /src/backend/pyfile/
# キャッシュクリーンアップと不要なリストの削除
RUN apt clean && rm -rf /var/lib/apt/lists/*

# 下記二つはマルチステージングビルドの内容
# 開発環境用
FROM base AS development
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 本番環境用
FROM base AS production
# 必要なら下記を行う参考用
CMD ["python3", "/src/backend/pyfile/prod_kidou/kidou.py"]

# 下記保留 内容わすれた
# RUN pip install --upgrade setuptools
# コンテナからホストpcつまりmacと通信ができる。compose側で定義しているから不要。compuseを使用しないなら必要。DISPLAY変数にhost.docker.internal:0.0の値を代入している(tkinterを使う場合必要又はドッカーからホストに対して通信を行う場合)
#ENV DISPLAY host.docker.internal:0.0