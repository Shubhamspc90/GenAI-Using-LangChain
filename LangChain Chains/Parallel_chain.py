from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import os
load_dotenv()

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

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text: {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text: {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document. Notes: {notes} Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()


# Parallel Chain
parallel_chain = RunnableParallel({
    "notes": prompt1 | model | parser,
    "quiz": prompt2 | model | parser
})


# Merge Chain
merge_chain = prompt3 | model | parser


# Complete Chain
chain = parallel_chain | merge_chain


text = """
Support vector machines (SVMs) are a set of supervised learning methods
used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than
the number of samples.

Uses a subset of training points in the decision function called
support vectors, so it is also memory efficient.

Versatile: different Kernel functions can be specified.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples,
avoid over-fitting in choosing Kernel functions and regularization
term is crucial.

SVMs do not directly provide probability estimates.
"""


result = chain.invoke({
    "text": text
})

print(result)

# Display chain structure
chain.get_graph().print_ascii()

##====== OUTPUT ==========##

# Here is the merged document:

# **Advantages and Disadvantages of Support Vector Machines (SVMs)**

# **Advantages:**

# * Effective in high-dimensional spaces
# * Works well with few samples and many features
# * Memory-efficient due to use of support vectors
# * Versatile with different kernel functions
# * Effective in cases where number of dimensions is greater than number of samples

# **Disadvantages:**

# * Can overfit if not careful with kernel functions and regularization term
# * Does not provide direct probability estimates

# **Quiz:**

# **Q1: What are support vector machines (SVMs) used for?**
# **A1:** SVMs are used for classification, regression, and outliers detection.

# **Q2: What is an advantage of SVMs in high-dimensional spaces?**
# **A2:** SVMs are effective in high-dimensional spaces.

# **Q3: What makes SVMs memory efficient?**
# **A3:** SVMs use a subset of training points in the decision function, called support vectors, making them memory efficient.

# **Q4: What is a potential disadvantage of SVMs when dealing with many features?**
# **A4:** If the number of features is much greater than the number of samples, choosing the right Kernel functions and regularization term is crucial to avoid over-fitting.

# **Q5: Do SVMs provide probability estimates?**
# **A5:** No, SVMs do not directly provide probability estimates.
#             +---------------------------+            
#             | Parallel<notes,quiz>Input |            
#             +---------------------------+            
#                  **               **                 
#               ***                   ***              
#             **                         **            
# +----------------+                +----------------+ 
# | PromptTemplate |                | PromptTemplate | 
# +----------------+                +----------------+ 
#           *                               *          
#           *                               *          
#           *                               *          
#   +------------+                    +------------+   
#   | ChatOllama |                    | ChatOllama |   
#   +------------+                    +------------+   
#           *                               *          
#           *                               *          
#           *                               *          
# +-----------------+              +-----------------+ 
# | StrOutputParser |              | StrOutputParser | 
# +-----------------+              +-----------------+ 
#                  **               **                 
#                    ***         ***                   
#                       **     **                      
#            +----------------------------+            
#            | Parallel<notes,quiz>Output |            
#            +----------------------------+            
#                           *                          
#                           *                          
#                           *                          
#                  +----------------+                  
#                  | PromptTemplate |                  
#                  +----------------+                  
#                           *                          
#                           *                          
#                           *                          
#                    +------------+                    
#                    | ChatOllama |                    
#                    +------------+                    
#                           *                          
#                           *                          
#                           *                          
#                 +-----------------+                  
#                 | StrOutputParser |                  
#                 +-----------------+                  
#                           *                          
#                           *                          
#                           *                          
#               +-----------------------+              
#               | StrOutputParserOutput |              
#               +-----------------------+     


