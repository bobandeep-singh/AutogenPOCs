import os

from autogen import ConversableAgent
# import autogen


config_list = [
    {"model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF", "api_key": "lm-studio",
        "base_url": "http://localhost:1234/v1"}
]

agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": config_list},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"content": "Tell me 10 jokes.", "role": "user"}])
print(reply)