import re

def create_prompt(emoji_dict):
    prompt = input("Enter your message: ")
    # Parse emojis
    for emoji, code in emoji_dict.items():
        prompt = re.sub(emoji, code, prompt)
    return prompt

emoji_dict = {':)': '😊', ':(': '😔'}
prompt = create_prompt(emoji_dict)
print(prompt)

# import re

def create_prompt(emoji_dict):
    prompt = input("Enter your message: ")
    # Parse emojis
    for emoji, code in emoji_dict.items():
        prompt = re.sub(emoji, code, prompt)
    return prompt

emoji_dict = {':)': '😊', ':(': '😔'}
prompt = create_prompt(emoji_dict)
print(prompt)
