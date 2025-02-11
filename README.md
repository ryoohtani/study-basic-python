## Learning basic Python syntax
## Pythonの基本構文の学習

<sub> Introductory Python Study </sub>

<sub> Pythonの入門学習 </sub>

**環境構築**

*dockerコマンド*

* ビルドコマンド
```
docker compose build
``` 
* 環境の立ち上げ
```
docker compose up -d 
docker compose up -d python3-dev
docker compose up -d python3-prod
docker compose up -d python3-dev && docker compose up -d python3-prod
docker compose up -d postgres-db
```
* Pythonのコンテナ又はpostgressqlにアクセス
```
docker exec -it stady-python-dev bash
docker exec -it stady-python-prod bash
docker exec -it postgres-db psql -U admin -d pydb
```
---
*Pythonのコマンド*

* Pythonのバージョン確認
```
python3 --version
```
* pipのバージョン確認コマンド
```
pip3 --version
```
* pipでインストールしたものを確認するコマンド
```
pip3 list
```
* tkinterの確認コマンド
```
python -m tkinter
```
* Djangoのバージョン確認コマンド
```
pip list | grep Django
python -m django --version
pip show django
```
* flaskのバージョン確認コマンド
```
flask --version
python -m flask --version
```
* fastapiの確認コマンド
```
pip show fastapi
```
* set.py(Pythonのパッケージをビルド、インストール、配布する際の必要情報記載)
```
python setup.py sdist
```
* venvにアクセスするためのコマンド。コピペでターミナルに貼り付けること
```
source /src/backend/pyfile/venv/bin/activate
```
* venvから抜けるためのコマンド。コピペでターミナルに貼り付けること
```
deactivate
```
---
**Pythonコードスタイルガイド**

* pycodestyle
```
pycodestyle --version
pycodestyle 対象ファイル
```
* flake8
```
flake8 --version
flake8 対象ファイル
```
* pylint
```
pylint --version
pylint 対象ファイル
```
---
**djangoの環境構築**

* プロジェクトフォルダの作成
```
必要なプロジェクトの素材を配置される => プロジェクトの設定や管理用のファイルが生成されるフォルダ
django-admin startproject ここにフォルダ名を記載
```

* アプリケーションフォルダの作成(機能単位のモジュールを作る)
```
アプリケーションという 独立した機能の単位をごとに作成するため必要
今回はCRUDシステムの作成
⚫️プロジェクトフォルダに移動して、アプリケーションフォルダ作成コマンドを行う。必ずmanage.pyのあるところで行う
python manage.py startapp ここにフォルダ名を記載
```

* docker環境からサーバーにアクセスコマンド
```
0.0.0.0:8020 こちらは、docker環境のportを指定している
venvの環境に入り、manage.pyあるところに移動
python manage.py runserver 0.0.0.0:8020
```

---
**postgressqlコマンド**

* テーブルの確認
```
SELECT * FROM test_table;
```
* テーブルの削除
```
DROP TABLE test_table;
```
* テーブルの存在確認
```
\dt
```
---
**tkinterの取り扱う場合の準備**

* XQuartzのダウンロード
```
https://www.xquartz.org/
```
* アプリの設定
```
設定 → セキュリティタブ → ネットワーク・クライアントからの接続を許可にチェック
```
* アプリの起動(ホストpcのターミナルで実行)
```
open -a XQuartz
```
* ローカルホストをxサーバーに接続許可するコマンド(ホストpcのターミナルで実行)
```
xhost + 127.0.0.1
又は
xhost + localhost
意味は同じだが推奨は最小のやつ
```
* ローカルホストをxサーバーに接続解除するコマンド(ホストpcのターミナルで実行)
```
xhost - 127.0.0.1
又は
xhost - localhost
意味は同じだが推奨は最初のやつ
```
* 接続状況確認コマンド(ホストpcのターミナルで実行)
```
xhost
```
---
*gitコマンド*

* ローカルリポジトリの新規作成
```
git init
```
* ファイルの追跡(変更分全て)
```
git add .
```
* コミット
```
git commit
```
* ローカルリポジトリにリモートリポジトリのURLを貼り付ける
```
git remote add pysyntax URLを貼り付ける
```
* リモートリポジトリへプッシュ
```
git push -u pysyntax main
```
* リモートリポジトリからローカルに反映
```
git fetch
```
* ブランチの移動
```
git checkout main
```
* マージ
```
git merge pysyntax/main
```
---
* 参考資料
```
参考資料(Pythonの環境構築)
https://qiita.com/syo_engineer/items/5f31f25cb50400b94b1d
```
```
参考資料(PYTHONDONTWRITEBYTECODEとは)
https://engineeeer.com/no-more-pycache/
```
```
treeなし
https://qiita.com/yone098@github/items/bba8a42de6b06e40983b
```
```
docker sql python venv環境構築
https://qiita.com/toffe_hy/items/8c62f2bc7b14f1ce2ae0
https://qiita.com/toffe_hy/items/0429a95bfe1786955c2a
https://qiita.com/toffe_hy/items/f2e6ecc516fdf593c777

https://zenn.dev/syuya2036/articles/416c8f7a3a4765
```