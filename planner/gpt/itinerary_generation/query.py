"""Functions to query LLM to plan a holiday."""
import json

from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from planner.gpt.itinerary_generation.format_instructions import get_format_instructions

def query(place_name: str):
    """Prompt to ask gpt to plan a holiday."""
    partial_variables = {
        "format_instructions": get_format_instructions(),
        "place_name": place_name}

    chat_template = ChatPromptTemplate(
        partial_variables=partial_variables,
        messages= [
        ("system", "Answer the user query.\n{format_instructions}."),
        ("user", ("Plan a three day family holiday to {place_name}. "
                 "Suggest up to six once in a lifetime activities that are near "
                  "to the location and explore the local area."
                  "For the activity_full_description field, write a paragraph"
                  "to really sell the activity.")),
    ])

    chain = ({"context": {},
             "question": RunnablePassthrough()}
            | chat_template
            | ChatOpenAI()
            | StrOutputParser())

    response = chain.invoke(input=place_name)

    return json.loads(response)
