from langchain import PromptTemplate

# Prompt template for LinkedIn
linkedin_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Please generate LinkedIn content about {topic}."
)

# Prompt template for Instagram
instagram_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Please generate Instagram content about {topic}."
)

# Prompt template for Facebook
facebook_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Please generate Facebook content about {topic}."
)

# Prompt template for Twitter
twitter_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Please generate Twitter content about {topic}."
)

# Prompt template for YouTube script creator
youtube_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Your job is to write a script for YouTube based on the following preference provided by the user: {topic}."
)
