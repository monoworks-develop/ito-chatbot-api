from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from src.infrastructure.azure.openai.model import openai_chat_model
from src.models import AskInput
from src.service.azure_ai_search import vector_search


def ask(ask_input: AskInput):
    # AI Searchからデータ取得
    vector_search_response = vector_search(ask_input.text)

    # システムプロンプト
    system_prompt_template = SystemMessagePromptTemplate.from_template(
        """あなたは、ユーザーからのリクエストに基づいて正確かつ簡潔に天気予報を提供する、気象予報専門のAIアシスタントです。以下のガイドラインに従って情報を生成してください。

        入力されるデータの構成
        ・場所(東京、銚子)
        ・日付
        ・時間帯ごとの天気概況

        入力データ:{input_data}

        入力データに基づき、適切な回答を行ってください。
        ただし、入力データに該当の情報が存在しない場合は、存在するデータを教えてください。"""
    )

    # ユーザープロンプト
    user_prompt_template = HumanMessagePromptTemplate.from_template("{user_input}")

    # チャットプロンプト
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [system_prompt_template, user_prompt_template]
    )
    chat_prompt = chat_prompt_template.format_prompt(
        input_data=vector_search_response, user_input=ask_input.text
    )

    response = openai_chat_model.invoke(chat_prompt)
    return response

    # # メモリの設定（会話履歴を保持）
    # memory = ConversationBufferMemory(return_messages=True)
