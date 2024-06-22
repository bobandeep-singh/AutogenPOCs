from autogen import ConversableAgent

config_list = [
    {"model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF", "api_key": "lm-studio",
        "base_url": "http://localhost:1234/v1"}
]

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="Cathy, tell me a joke.", max_turns=3)
