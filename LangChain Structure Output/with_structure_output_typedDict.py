from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated,Optional,Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="llama3",
    temperature=1.5
)

# # SIMPLE Schema creation for Dictionary
#### This is used to define the structure/schema of a dictionary that you expect your LLM or Python function to return.
# class Review(TypedDict):
#     summary: str
#     sentiment: str


# # ANNOTATED Schema creation for Dictionary
#### This part is used to tell the LLM exactly what kind of structured information you want back from a normal text input.
# class Review(TypedDict):
#     summary: Annotated[str,"A brief about Summary"]
#     sentiment: Annotated[str,"Return Sentiment of review either  positive,negative or Neutral"]


# more Complex with pros and cons  Schema creation for Dictionary
# schema
####  Annotated isliye use hota hai taaki field ke type ke saath us field ki extra information/description bhi de saken.
class Review(TypedDict):

    key_themes: Annotated[
        list[str],
        "Write down all the key themes discussed in the review in a list"
    ]

    summary: Annotated[
        str,
        "A brief summary of the review"
    ]

    sentiment: Annotated[
        Literal["positive", "negative", "neutral"],
        "Return sentiment of the review as positive, negative or neutral"
    ]

    pros: Annotated[
        Optional[list[str]],
        "Write down all the pros inside a list"
    ]

    cons: Annotated[
        Optional[list[str]],
        "Write down all the cons inside a list"
    ]

    name: Annotated[
        Optional[str],
        "Write the name of the reviewer"
    ]
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say,
it is an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes
everything lightning fast—whether I am gaming, multitasking, or editing
photos. The 5000mAh battery easily lasts a full day even with heavy use,
and the 45W fast charging is a lifesaver.

The S Pen integration is a great touch for note-taking and quick sketches,
though I don't use it often. What really blew me away is the 200MP camera.
The night mode is stunning, capturing crisp and vibrant images even in
low light. Zooming up to 100x actually works well for distant objects,
but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed
use. Also, Samsung's One UI still comes with bloatware. I don't understand
why there are multiple Samsung apps for things that Google already provides.
The $1,300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor, great for gaming and productivity
- Stunning 200MP camera with incredible zoom capabilities
- Long battery life with fast charging
- S Pen support is unique and useful

Cons:
- Bulky and heavy, not great for one-handed use
- Bloatware still exists in One UI
- Expensive compared to competitors

Review by Shubham Chauhan
""")


print("\n========== COMPLETE RESULT ==========")
print(result)

print("\n========== INDIVIDUAL FIELDS ==========")

print("Reviewer Name:", result["name"])
print("Summary:", result["summary"])
print("Sentiment:", result["sentiment"])
print("Key Themes:", result["key_themes"])
print("Pros:", result["pros"])
print("Cons:", result["cons"])


# OUTPUT


# ========== COMPLETE RESULT ==========
# {'key_themes': ['Powerful processor', 'Impressive camera', 'Long battery life', 'Bulky size', 'Bloatware', 'Expensive'], 'summary': 'Overall, the Samsung Galaxy S24 Ultra is a powerful device with impressive camera capabilities and long battery life, but it also has some drawbacks such as its bulky size and the presence of bloatware.', 'sentiment': 'neutral', 'pros': ['Insanely powerful processor, great for gaming and productivity', 'Stunning 200MP camera with incredible zoom capabilities','Long battery life with fast charging', 'S Pen support is unique and useful'], 'cons': ['Bulky and heavy, not great for one-handed use', 'Bloatware still exists in One UI', 'Expensive compared to competitors'], 'name': 'Shubham Chauhan'}

# ========== INDIVIDUAL FIELDS ==========
# Reviewer Name: Shubham Chauhan
# Summary: Overall, the Samsung Galaxy S24 Ultra is a powerful device with impressive camera capabilities and long battery life, but it also has some drawbacks such as its bulky size and the presence of bloatware.
# Sentiment: neutral
# Key Themes: ['Powerful processor', 'Impressive camera', 'Long battery life', 'Bulky size', 'Bloatware', 'Expensive']
# Pros: ['Insanely powerful processor, great for gaming and productivity', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S Pen support is unique and useful']
# Cons: ['Bulky and heavy, not great for one-handed use', 'Bloatware still exists in One UI', 'Expensive compared to competitors']