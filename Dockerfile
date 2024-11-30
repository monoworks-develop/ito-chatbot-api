FROM python:3-slim-bookworm

WORKDIR /app

# poetryからrequirements.txtを生成するために必要なファイルをコピー
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

# poetryからrequirements.txtを生成し、それを使ってパッケージをインストール
RUN pip install poetry && \
  poetry export -f requirements.txt -o requirements.txt --without-hashes && \
  pip install --no-cache-dir --upgrade -r requirements.txt

# アプリケーションの起動
COPY ./src ./src
EXPOSE 80
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
