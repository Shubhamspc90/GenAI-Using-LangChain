from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOllama(
    model="llama3",
    temperature=0
)


# schema
json_schema = {
    "title": "Review",
    "type": "object",

    "properties": {

        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the key themes discussed in the review in a list"
        },

        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },

        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg", "neutral"],
            "description": "Return sentiment of the review as positive, negative, or neutral"
        },

        "pros": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "Write down all the pros inside a list"
        },

        "cons": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "Write down all the cons inside a list"
        },

        "name": {
            "type": ["string", "null"],
            "description": "Write the name of the reviewer"
        }
    },

    "required": [
        "key_themes",
        "summary",
        "sentiment",
        "pros",
        "cons",
        "name"
    ]
}


structured_model = model.with_structured_output(json_schema)

review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say,
it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes
everything lightning fast—whether I’m gaming, multitasking, or editing
photos.

The 5000mAh battery easily lasts a full day even with heavy use, and
the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches,
though I don't use it often.

What really blew me away is the 200MP camera—the night mode is stunning,
capturing crisp, vibrant images even in low light. Zooming up to 100x
actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use.
Also, Samsung’s One UI still comes with bloatware—why do I need five different
Samsung apps for things Google already provides?

The $1,300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor
- Stunning 200MP camera
- Long battery life with fast charging
- S-Pen support is unique and useful

Review by Shubham Chauhan
"""


result = structured_model.invoke(review)
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
# {'key_themes': ['Samsung Galaxy S24 Ultra', 'Performance', 'Camera', 'Battery', 'S-Pen', 'One UI', 'Price'],
# 'summary': "The reviewer, Shubham Chauhan, shares their experience with the Samsung Galaxy S24 Ultra. 
# They praise the device's powerful processor, long battery life, and impressive camera capabilities. 
# However, they also mention some drawbacks, such as the device's weight and size making it uncomfortable for one-handed use,
# the presence of bloatware in One UI, and the high price tag.Overall, the reviewer highlights the device's pros and cons, 
# providing a balanced review.", 'sentiment': 'neutral', 'pros':['Insanely powerful processor', 'Stunning 200MP camera', 
# 'Long battery life with fast charging', 'S-Pen support is unique and useful'], 
# 'cons': ['Weight and size make it uncomfortable for one-handed use', 'Bloatware in One UI', 'High price tag'], 
# 'name': 'Shubham Chauhan'}

# ========== INDIVIDUAL FIELDS ==========
# Reviewer Name: Shubham Chauhan
# Summary: The reviewer, Shubham Chauhan, shares their experience with the Samsung Galaxy S24 Ultra. They praise the device'spowerful processor, long battery life, and impressive camera capabilities. However, they also mention some drawbacks, such as the device's weight and size making it uncomfortable for one-handed use, the presence of bloatware in One UI, and the high price tag. Overall, the reviewer highlights the device's pros and cons, providing a balanced review.
# Sentiment: neutral
# Key Themes: ['Samsung Galaxy S24 Ultra', 'Performance', 'Camera', 'Battery', 'S-Pen', 'One UI', 'Price']
# Pros: ['Insanely powerful processor', 'Stunning 200MP camera', 'Long battery life with fast charging', 'S-Pen support is unique and useful']
# Cons: ['Weight and size make it uncomfortable for one-handed use', 'Bloatware in One UI', 'High price tag']