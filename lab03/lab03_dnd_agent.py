from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Alex Wood'
model = 'llama3.2'
options = {'temperature': 1, 'max_tokens': 10}
messages = [ 
  {'role': 'system', 'content': 'You are a dungeons and dragons game master that is human-like in emotion, as your players thrive off of your energy. This game should be space-based, and begin right in the perilous action of war.'},
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
    # Get input from the user
  user_input = input("You: ")
    
    # Add the user's input to the messages list
  messages.append({'role': 'user', 'content': user_input})
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f'Assistant: {response["message"]["content"]}')
  messages.append({'role': 'assistant', 'content': response["message"]["content"]})

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

