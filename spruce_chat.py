import os
from langchain.chat_models import ChatVertexAI
from langchain.llms import VertexAI
from langchain import SQLDatabase, SQLDatabaseChain
from langchain.chains import SQLDatabaseSequentialChain
from chainlit import AskUserMessage, Message, on_chat_start, on_message, langchain_factory
from langchain.callbacks import HumanApprovalCallbackHandler

#crowdpulse-inc.prometheus_llm_spruce
spruce_llm_url = 'bigquery://crowdpulse-inc/prometheus_llm?'

callbacks = HumanApprovalCallbackHandler()

@on_chat_start
async def main():
        await Message(
            content=f"Ask questions of the Spruce Maplayers, focused primarily on location-based aggregations",
        ).send()


@langchain_factory(use_async=False)
def load_model():
    spruce_llm_db = SQLDatabase.from_uri(spruce_llm_url, sample_rows_in_table_info=3)
    vertexai_llm = VertexAI(verbose=True, temperature=0.5) #NOTE see how temperature changes responses
    vertexai_llm_chain = SQLDatabaseSequentialChain.from_llm(llm=vertexai_llm, database=spruce_llm_db, top_k=500, verbose=True, return_intermediate_steps=True, tags=None, use_query_checker=False, return_direct=False)

    return vertexai_llm_chain
