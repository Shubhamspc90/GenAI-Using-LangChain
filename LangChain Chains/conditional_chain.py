from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
import os

load_dotenv()


# -----------------------------
# 1. Ollama Model
# -----------------------------

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={
        "headers": {
            "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
        }
    },
    temperature=0
)


# -----------------------------
# 2. Output Parsers
# -----------------------------

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


parser2 = PydanticOutputParser(
    pydantic_object=Feedback
)


# -----------------------------
# 3. Classification Prompt
# -----------------------------

prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback text
into exactly one of these two categories:
positive or negative.

Feedback:
{feedback}

{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    }
)


# -----------------------------
# 4. Classifier Chain
# -----------------------------

classifier_chain = prompt1 | model | parser2


# -----------------------------
# 5. Positive Feedback Prompt
# -----------------------------

prompt2 = PromptTemplate(
    template="""
Write an appropriate response to this positive feedback:

{feedback}
""",
    input_variables=["feedback"]
)


# -----------------------------
# 6. Negative Feedback Prompt
# -----------------------------

prompt3 = PromptTemplate(
    template="""
Write an appropriate response to this negative feedback:

{feedback}
""",
    input_variables=["feedback"]
)


# -----------------------------
# 7. Branching
# -----------------------------

branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        prompt2 | model | parser
    ),

    (
        lambda x: x.sentiment == "negative",
        prompt3 | model | parser
    ),

    RunnableLambda(
        lambda x: "Could not find sentiment"
    )
)


# -----------------------------
# 8. Complete Chain
# -----------------------------

chain = classifier_chain | branch_chain


# -----------------------------
# 9. Invoke
# -----------------------------

result = chain.invoke({
    "feedback": "This is a very Expansive phone"
})

print(result)


# -----------------------------
# 10. Display Graph
# -----------------------------

chain.get_graph().print_ascii()

# # output 
# Thank you so much for your kind words! We’re thrilled to hear that you had a positive experience, and your feedback truly brightens our day.
# If there’s anything else we can do for you or any suggestions you’d like to share, please let us know—we’re always here to help. Thanks again for your support!
#     +-------------+      
#     | PromptInput |      
#     +-------------+      
#             *            
#             *            
#             *            
#    +----------------+    
#    | PromptTemplate |    
#    +----------------+    
#             *            
#             *            
#             *            
#      +------------+      
#      | ChatOllama |      
#      +------------+      
#             *            
#             *            
#             *            
# +----------------------+ 
# | PydanticOutputParser | 
# +----------------------+ 
#             *            
#             *            
#             *            
#        +--------+        
#        | Branch |        
#        +--------+        
#             *            
#             *            
#             *            
#     +--------------+     
#     | BranchOutput |     
#     +--------------+    