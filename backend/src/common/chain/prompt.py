from langchain import PromptTemplate

# Prompt template for LinkedIn
linkedin = PromptTemplate(
    input_variables=["topic"],
    template="Please generate LinkedIn content about {topic}."
)

# Prompt template for Instagram
instagram = PromptTemplate(
    input_variables=["topic"],
    template="Please generate Instagram content about {topic}."
)

# Prompt template for Facebook
facebook = PromptTemplate(
    input_variables=["topic"],
    template="Please generate Facebook content about {topic}."
)

# Prompt template for Twitter
twitter = PromptTemplate(
    input_variables=["topic"],
    template="Please generate Twitter content about {topic}."
)

# Prompt template for YouTube script creator
youtube = PromptTemplate(
    input_variables=["topic"],
    template="Your job is to write a script for YouTube based on the following preference provided by the user: {topic}."
)

# Dictionary to store all prompt templates
prompts = {
    "linkedin": linkedin,
    "instagram": instagram,
    "facebook": facebook,
    "twitter": twitter,
    "youtube": youtube
}








# from langchain import PromptTemplate

# # Prompt template for LinkedIn
# linkedin= PromptTemplate(
#     type=['type'],
#     input_variables=["topic"],
#     template="Please generate LinkedIn content about {topic}."
# )

# # Prompt template for Instagram
# instagram = PromptTemplate(
#     type=['type'],
#     input_variables=["topic"],
#     template="Please generate Instagram content about {topic}."
# )

# # Prompt template for Facebook
# facebook= PromptTemplate(
#     type=['type'],
#     input_variables=["topic"],
#     template="Please generate Facebook content about {topic}."
# )

# # Prompt template for Twitter
# twitter= PromptTemplate(
#     type=['type'],
#     input_variables=["topic"],
#     template="Please generate Twitter content about {topic}."
# )

# # Prompt template for YouTube script creator
# youtube= PromptTemplate(
#     type=['type'],
#     input_variables=["topic"],
#     template="Your job is to write a script for YouTube based on the following preference provided by the user: {topic}."
# )
