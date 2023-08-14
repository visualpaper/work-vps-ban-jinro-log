# ban-jinro-log

* python 3.8.1
* poerty 1.2.2

## Setup

### poetry

#### initialize

- poetry new xxxx  
  ※ ひな形が必要ない場合、poetry init で pyproject.toml のみ作成する。  
  ※ poetry はデフォルトでパッケージごとに仮想環境が作成される。  
     後続コマンドでは仮想環境上で実施されるので、venv と競合する場合 `python -m pip uninstall virtualenv` で venv を uninstall すること。  
  ※ 生成される xxxx フォルダを "src" に変更する。  
  ※ name / version / description は必須、authors は匿名にしておく必要があれば匿名にしておくこと。以下例  

```
name = "xxxx"
version = "0.1.0"
description = ""
authors = ["visualpaper"]
```

- poetry config virtualenvs.in-project true  
  ※ vscode との連携都合、仮想環境作成場所をフォルダ直下にします。

<br>

#### Formatter

- poetry add --group dev black  
  ※ コマンドは Task Runner 欄に記載する。

<br>

#### Linter

- poetry add --group dev flake8  
  ※ コマンドは Task Runner 欄に記載する。  
  ※ flake8 が portry [未対応](https://github.com/PyCQA/flake8/issues/234) だが flake8 を使っている。  
  ※ python バージョンによって制限がかかることがあるため、以下のように version の指定を変更している。

```
[tool.poetry.dependencies]
python = ">=3.8.1"
```

<br>

#### Test

- poetry add --group dev pytest pytest-mock pytest-cov  
  ※ pytest-mock は mock 用、pytest-cov はカバレッジ表示用に入れています。  
  ※ src と tests フォルダがフラットに並んでいる場合 (src 配下に tests がない場合) 以下を toml ファイルに追加する必要があります。  
  ※ python 標準 unittest は原則利用が必要な場面でのみ利用する形で進めていますが、制限ではないです。

```
[tool.pytest.ini_options]
# tests が src と同階層にいる場合、tests から src を参照するために必要
pythonpath = [
  ".", "src"
]

[tool.coverage.report]
# pytest カバレッジ用の設定
## show_missing: test がない行を表示する (結果が長くなるのでデフォルトは false としています)
## skip_empty: 空ファイルを除外する (主に __init__.py 除外目的です)
show_missing = false
skip_empty = true
```

<br>

#### Task Runner

- poetry add --group dev taskipy  
  ※ python バージョンによって制限がかかることがあるため、以下のように version の指定を変更している。  
  ※ 以下を Task に追加する。  

```
[tool.poetry.dependencies]
python = ">=3.8.1,<4.0"
```

```
[tool.taskipy.tasks]
# skip-string-normalization で ' を " に変えることを抑制しています。
# ※ PEP8 では規定されていないが好みだと思うので抑制しています。
format = "black src tests --skip-string-normalization"

# max-line-length で black の定義 88 に合わせています。
# (参照) https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length
#
# W503 と E203 は black の定義と合わせています。
# (参照) https://rcmdnk.com/blog/2019/11/04/computer-python/
#        https://org-technology.com/posts/python-black.html
lint = "flake8 src tests --ignore=E203,W503 --max-line-length=88"

# -s: テスト実行中に print 文の出力を標準出力に書き出す。
# -v: テストごとの Success/Failed を表示する。
# --cov: カバレッジを表示する。
test = "pytest tests -s -vv --cov"
```

<br><br>

### VSCode

#### extensions

以下、VSCode 拡張をインストールする。

```
    "recommendations": [
        // https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
        "ms-python.vscode-pylance",
        // https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter
        "ms-python.black-formatter",
        // https://marketplace.visualstudio.com/items?itemName=ms-python.flake8
        "ms-python.flake8",
    ]
```

<br>

#### defaultInterpreterPath

CTRL + SHIFT + P で「Python Select Interpreter」を選択し Poetry にて作成された venv の場所を指定すること。  
※ こうしないと Global (/home/python など) の場所を見て import などの解決がされてしまうためコンパイルができない。

<br>

#### formatter

- black  
  ※ PEP8 準拠していない場合など自動修正してくれるようになる。

```
    // formatter
    // 以下に沿って、VSCode 拡張をインストールする。
    // https://github.com/microsoft/vscode-python/wiki/Migration-to-Python-Tools-Extensions
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
    },
    "black-formatter.args": [
        // skip-string-normalization で ' を " に変えることを抑制している。
        // # ※ PEP8 では規定されていないが好みだと思うので抑制している。
        "skip-string-normalization"
    ],
```

<br>

#### linter

- flake8

```
    // linter
    // 以下に沿って、VSCode 拡張をインストールする。
    // https://github.com/microsoft/vscode-python/wiki/Migration-to-Python-Tools-Extensions
    "flake8.args": [
        // black の定義 88 に合わせています。
        // (参照) https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length
        "--max-line-length=88",
        // W503 と E203 は black の定義と合わせています。
        // (参照) https://rcmdnk.com/blog/2019/11/04/computer-python/
        //        https://org-technology.com/posts/python-black.html
        "--ignore=E203,W503"
    ],
```

※ PEP8 準拠していない場合など警告が出るようになる。

<br>

#### type hints

- Pylance  
  ※ 入力補完、自動インポートなど。  

```
    // Pylance 拡張機能での型チェックを行うようにする。
    "python.analysis.typeCheckingMode": "basic"
```

<br><br>

### Library

#### pydantic

- poetry add pydantic  
  ※ 型ヒントを元に Validation を行うために必要  
  ※ Pylance は静的解析レベルで、pydantic は型を元に Validation エラーまで出してくれる。    

- poetry add pydantic-settings  
  ※ Env から設定を読み込む際に利用している。  
  ※ 元々 pydantic V1 では不要だったが V2 から別途必要になったので入れている。

<br>

#### Env

- poetry add python-dotenv  
  ※ 開発時には .env ファイルを利用する。  
  ※ テスト時には Setting を override する。  
  ※ デプロイ時には環境変数を指定して override する。  
  ※ gitignore より `.env` を対象にするよう変更すること。

```
# Environments
#.env ← をコメントアウトし commit 対象とすること。
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
```

<br><br>

### FastAPI

#### initialize

- poetry add fastapi uvicorn  
  ※ uvicorn は Local で動かすために必要なサーバで、本体は fastapi のみ。

<br>

#### Graphql

- poetry add strawberry-graphql  
  ※ 実態は https://strawberry.rocks/

<br>

#### Rate Limit

- poetry add slowapi  
  ※ Alpha 版だが、非常に使いやすいので採用している。  
  ※ limit デコレータはデコレータする関数の直上に記載しなければいけない点に注意すること。  
  (参照) https://slowapi.readthedocs.io/en/latest/

<br><br>

## Build

- poetry install
- poetry run task codegen
- poetry run task format
- poetry run task lint
- poetry run task test
- poetry run task start  
  ※ http://localhost:8000/docs or http://localhost:8000/redoc で OAS 参照可能
