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
RUN apt update && apt install -y vim less sudo tree curl
# postgresを使用するために必要なパッケージ
RUN apt update && apt install -y libpq-dev
# Pythonのインストール
RUN apt install -y python3.12
# pipのインストール
RUN apt install -y --upgrade python3-pip
# パッケージインストールのためにvenvの仮想環境を準備
RUN apt update && apt install -y python3.12-venv
# dockerファイルと同じ階層にrequirements.txt配置すること
COPY ./requirements.txt /src/backend/pyfile/
# venv(仮想環境)の作成先    
RUN python3 -m venv /src/backend/pyfile/venv
# venvからdocker環境内にあるrequirements.txtをインストールする処理
RUN /src/backend/pyfile/venv/bin/pip install -r /src/backend/pyfile/requirements.txt
# ホストPCのカレントディレクトリまたはコンテナ側からファイル等をコピー
COPY . /src/backend/pyfile/
# キャッシュクリーンアップと不要なリストの削除
RUN apt clean && rm -rf /var/lib/apt/lists/*

# 下記二つはマルチステージングビルドの内容 #
# 開発環境用
FROM base AS development
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 本番環境用
FROM base AS production
# 必要なら下記を行う参考用
CMD ["python3", "/src/backend/pyfile/app1_answer.py"]


    
# 下記保留 内容わすれた
# RUN pip install --upgrade setuptools