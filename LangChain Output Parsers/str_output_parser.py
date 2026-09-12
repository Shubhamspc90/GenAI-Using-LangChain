from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(
    model="llama3",
    temperature=0
)

# Output Parser
parser = StrOutputParser()


# ---------------- FIRST PROMPT ----------------

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Chain: Prompt → Model → String Output Parser
chain1 = template1 | model | parser

result1 = chain1.invoke({
    "topic": "black hole"
})

print("FIRST RESULT:")
print(result1)


# ---------------- SECOND PROMPT ----------------

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"]
)

# Chain: Prompt → Model → String Output Parser
chain2 = template2 | model | parser

result2 = chain2.invoke({
    "text": result1
})

print("\nSUMMARY:")
print(result2)




# Overall Flow

#            USER INPUT
#                │
#                ▼
#           "black hole"
#                │
#                ▼
#       ┌─────────────────┐
#       │ PromptTemplate  │
#       │   template1     │
#       └────────┬────────┘
#                │
#                ▼
#   "Write a detailed report
#      on black hole"
#                │
#                ▼
#       ┌─────────────────┐
#       │    ChatOllama   │
#       │     Llama3      │
#       └────────┬────────┘
#                │
#                ▼
#          AIMessage
#                │
#                ▼
#     ┌────────────────────┐
#     │  StrOutputParser   │
#     └─────────┬──────────┘
#               │
#               ▼
#       Plain Python String
#               │
#               ▼
#       Detailed Report
#               │
#               │
#               ▼
#       ┌─────────────────┐
#       │ PromptTemplate  │
#       │   template2     │
#       └────────┬────────┘
#                │
#                ▼
#      "Write a 5 line summary
#       on the following text"
#                │
#                ▼
#       ┌─────────────────┐
#       │    ChatOllama   │
#       │     Llama3      │
#       └────────┬────────┘
#                │
#                ▼
#          AIMessage
#                │
#                ▼
#     ┌────────────────────┐
#     │  StrOutputParser   │
#     └─────────┬──────────┘
#               │
#               ▼
#       Plain Python String
#               │
#               ▼
#         5 Line Summary


# # OUTPUT
# FIRST RESULT:
# **Report: Black Holes**

# **Introduction**

# Black holes are among the most fascinating and mysterious objects in the universe. These regions of spacetime are characterizedby an incredibly strong gravitational pull, so intense that nothing, not even light, can escape once it falls within a certain radius, known as the event horizon. In this report, we will delve into the properties, formation, and effects of black holes, aswell as the latest research and discoveries in this field.

# **Properties of Black Holes**

# Black holes are formed when a massive star collapses under its own gravity, causing a massive amount of matter to be compressedinto an incredibly small point, known as a singularity. This singularity is surrounded by an event horizon, which marks the boundary beyond which nothing, including light, can escape the gravitational pull of the black hole.

# The properties of black holes can be described as follows:

# * **Mass**: Black holes can have masses ranging from a few solar masses to supermassive black holes with masses millions or even billions of times that of the sun.
# * **Spin**: Black holes can rotate, and their spin can affect the way they interact with their surroundings.
# * **Charge**: Black holes can have an electric charge, which affects their behavior in the presence of other charged objects.
# * **Event Horizon**: The event horizon is the boundary beyond which nothing, including light, can escape the gravitational pullof the black hole.
# * **Singularity**: The singularity is the point at the center of the black hole where the curvature of spacetime is infinite and the laws of physics as we know them break down.

# **Formation of Black Holes**

# Black holes are formed through the collapse of massive stars. When a star with a mass at least three times that of the sun runsout of fuel, it begins to collapse under its own gravity. If the star is massive enough, its core will collapse into a singularity, forming a black hole.

# There are several ways that black holes can form, including:

# * **Direct Collapse**: A massive star collapses directly into ablack hole.
# * **Indirect Collapse**: A massive star collapses into a neutron star, which then collapses into a black hole.
# * **Mergers**: Two black holes merge to form a more massive black hole.

# **Effects of Black Holes**

# Black holes have a profound impact on the surrounding environment. Their strong gravitational pull can:

# * **Distort Light**: The strong gravity of a black hole can distort the light passing near it, creating a phenomenon known as gravitational lensing.
# * **Affect the Motion of Nearby Objects**: The gravity of a black hole can affect the motion of nearby objects, such as stars or planets.
# * **Create a Region of Spacetime Known as the Ergosphere**: Theergosphere is a region around a rotating black hole where the rotation of the black hole creates a kind of "gravitational drag"that can affect the motion of nearby objects.

# **Detection and Study of Black Holes**

# Black holes are difficult to detect directly, as their strong gravity pulls in all forms of radiation, including light. However, astronomers have developed several indirect methods to detect and study black holes, including:

# * **X-rays and Gamma Rays**: Telescopes can detect X-rays and gamma rays emitted by hot gas swirling around black holes.
# * **Radio Waves**: Radio telescopes can detect radio waves emitted by matter as it spirals into a black hole.
# * **Gravitational Waves**: The detection of gravitational wavesby the Laser Interferometer Gravitational-Wave Observatory (LIGO) and Virgo have confirmed the existence of black holes and provided a new way to study them.
# * **Astrometry**: Astronomers can use the motion of nearby stars to detect the presence of a black hole.

# **Recent Research and Discoveries**

# Recent research and discoveries in the field of black holes include:

# * **First Image of a Black Hole**: In 2019, astronomers released the first-ever image of a black hole, located at the center ofthe galaxy Messier 87 (M87).
# * **Detection of Black Hole Mergers**: LIGO and Virgo have detected numerous black hole mergers, providing insights into the properties of black holes and the behavior of gravity.
# * **Study of Black Hole Formation**: Astronomers have made significant progress in understanding the formation of black holes, including the role of binary star systems and the impact of supernovae explosions.
# * **Search for Black Hole Formation in the Early Universe**: Astronomers are searching for evidence of black hole formation in the early universe, which could provide insights into the evolution of the universe and the formation of the first stars.

# **Conclusion**

# Black holes are fascinating and complex objects that continue to capture the imagination of scientists and the public alike. Through the study of black holes, we can gain insights into the fundamental laws of physics, the behavior of gravity, and the evolution of the universe. As new research and discoveries are made,our understanding of these enigmatic objects will continue to grow, and we will likely uncover even more surprising and fascinating properties of black holes.

# SUMMARY:
# Here is a 5-line summary of the report on black holes:

# Black holes are regions of spacetime with incredibly strong gravitational pull, where nothing, including light, can escape onceit falls within a certain radius. 
# They are formed when a massive star collapses under its own gravity, creating a singularity surrounded by an event horizon.
# Black holes have various properties, including mass, spin, charge, and event horizon, and can affect the surrounding environment through gravitational lensing and motion of nearby objects.
# Astronomers have developed indirect methods to detect and study black holes, including X-rays, radiowaves, and gravitational waves. 
# Recent research and discoverieshave shed light on the properties and behavior of black holes, including the first-ever image of a black hole and the detectionof black hole mergers.