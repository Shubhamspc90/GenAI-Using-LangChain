from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(
    model='llama3',
    temperature=0.5
)

prompt=PromptTemplate(
    template="Geenerate 5 interseting fact about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt|model|parser

result = chain.invoke({'topic':'Green House Effect'})

print(result)

# Draws the chain as an ASCII diagram in the terminal
# chain.get_graph().draw_ascii()

# Generates a PNG image of the chain graph
# chain.get_graph().draw_png()




# output

# Here are 5 interesting facts about the Greenhouse Effect:

# 1. **The Greenhouse Effect is not new**: The concept of the Greenhouse Effect has been around for centuries. In the 19th century, French physicist Joseph Fourier was one of the first scientists to propose that the Earth's atmosphere traps heat, similar to the way a greenhouse works. He even coined the term "greenhouse effect" to describe this process.

# 2. **Greenhouse Gases are everywhere**: You might think that greenhouse gases are only found in the atmosphere, but they'reactually present in many everyday objects. For example, the insulation in your home is made up of materials like fiberglass, which is a natural insulator that traps heat. Similarly, the plastic wrap on your food is made up of polyethylene, which is a type of greenhouse gas. Who knew that your lunch was contributing to global warming?

# 3. **The Greenhouse Effect is essential for life**: While the Greenhouse Effect does contribute to global warming, it's also crucial for life on Earth. Without the Greenhouse Effect, the Earth's average temperature would be around -17°C (1°F), making it impossible for most life forms to exist. The Greenhouse Effect helps to keep the Earth warm enough for liquid water to exist, which is essential for life.

# 4. **The Greenhouse Effect is not just about carbon dioxide**: While carbon dioxide is the most well-known greenhouse gas, it's not the only one. Other gases like methane, nitrous oxide, and water vapor also trap heat in the atmosphere. In fact, water vapor is the most abundant greenhouse gas, making up around 60% of the total. So, while reducing carbon dioxide emissions is important, it's not the only solution to mitigating the effects of the Greenhouse Effect.

# 5. **The Greenhouse Effect is accelerating**: The concentration of greenhouse gases in the atmosphere has been increasing rapidly over the past century, largely due to human activities like burning fossil fuels and deforestation. This accelerationof the Greenhouse Effect is causing the Earth's average temperature to rise at an unprecedented rate. In fact, the 20 warmest years on record have all occurred since 1981, with the past five years being the warmest five-year period on record.



