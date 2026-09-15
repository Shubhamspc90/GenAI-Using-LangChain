from langchain_ollama import ChatOllama
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
import os
load_dotenv()

model1 = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={
        "headers": {
            "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
        }
    },
    temperature=0
)

# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     pipeline_kwargs={
#         "temperature": 0.5,
#         "max_new_tokens": 100
#     }
# )

# model2 = ChatHuggingFace(llm=llm)

promp1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)
promp2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet':RunnableSequence(promp1|model1|parser),
    'linkedIn':RunnableSequence(promp2|model1|parser)
})

print(chain.invoke({'topic':'AI'}))

# output  
# {'tweet': '🤖✨ AI is turning imagination into reality—one algorithm at a time. From art to medicine,the future is
# learning faster than ever.What will you create with the power of intelligence? #AI #FutureTech #CreativityUnleashed',
# 'linkedIn': '🚀 **The AI Revolution Isn’t Coming – It’s Already Here** 🚀  \n\nOver the past 12 months I’ve watched 
# three things happen at lightning speed:\n\n1️⃣ **Decision‑making is becoming data‑first.** From predictive analytics 
# to real‑time recommendation engines, AI is turning raw data into actionable insights faster than any human could.\n\n
# 2️⃣ **Productivity is getting a turbo‑boost.** Teams are automating repetitive tasks (think document triage, scheduling, 
# code reviews) and freeing up brain‑power for creative problem‑solving.\n\n3️⃣ **New roles are emerging.
# ** “Prompt Engineer,” “AI Ethics Lead,” and “Human‑AI Collaboration Designer” are now on the hiring radar, proving that 
# the skill set of the future is a blend of technical fluency and human empathy.\n\n💡 **What does this mean for us?**  
# \n- **Embrace continuous learning.**Platforms like Coursera, Udacity, and even free resources from OpenAI 
# are making it easier to upskill.  \n- **Start small, think big.** Pilot an AI‑powered workflow in one department,
# measure impact, then scale.  \n- **Prioritize ethics and transparency.** Trust is the currency of AI adoption—clear 
# governance frameworks are non‑negotiable.\n\n🔗 **My takeaway:** AI is not a “nice‑to‑have” add‑on; it’s a strategic
# imperative. The organizations that embed AI thoughtfully into their DNA will outpace the competition, attract top
# talent, and deliver richer customer experiences.\n\n👥 **Let’s start a conversation:**  \nWhat AI initiative has made 
# the biggest difference in your work? What challenges are you facing as you scale AI across your organization? Drop a
# comment or DM—let’s learn from each other!\n\n#ArtificialIntelligence #MachineLearning #DigitalTransformation 
# #FutureOfWork #AILeadership #ContinuousLearning#EthicalAI'}