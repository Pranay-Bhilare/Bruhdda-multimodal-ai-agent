from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from core.prompts import CHARACTER_PROMPT
from graph.utils.helper import get_chat_model


def get_character_response_chain(summary:str = ""):
    model = get_chat_model()
    system_message = CHARACTER_PROMPT
    if summary:
        system_message += f"\n\nSummary of conversation earlier between Bruhdda and the user: {summary}"

    prompt = ChatPromptTemplate.from_messages([("system", system_message), MessagesPlaceholder(variable_name="messages")])
    return prompt | model 