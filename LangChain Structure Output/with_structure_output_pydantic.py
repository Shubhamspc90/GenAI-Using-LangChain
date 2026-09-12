from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOllama(
    model="llama3",
    temperature=0
)


class Review(BaseModel):

    key_themes: list[str] = Field(
        description="Write all key themes discussed in the review as a list"
    )

    summary: str = Field(
        description="Provide a brief summary of the review"
    )

    sentiment: Literal["pos", "neg", "neutral"] = Field(
        description="Return the sentiment as positive, negative, or neutral"
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="List all the advantages or positive points"
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="List all the disadvantages or negative points"
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the reviewer"
    )

structured_model = model.with_structured_output(Review)

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

print("Reviewer Name:", result.name)
print("Summary:", result.summary)
print("Sentiment:", result.sentiment)
print("Key Themes:", result.key_themes)
print("Pros:", result.pros)
print("Cons:", result.cons)