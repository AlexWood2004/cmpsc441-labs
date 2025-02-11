from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Alex Wood'
model = 'llama3.2'
options = {'temperature': 2, 'max_tokens': 60}
messages = [ {'role': 'system', 'content': 'You should be an exciting dungeons and dragons game master that develops the users character by giving traits and items to them at the start. You want your players to feel connected to their characters. Also, formulate an exciting quest that is space themes strictly, but when doing so always review your steps and determine if your quest is new and advancing.'},]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
 
  # Add your code below
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  if messages[-1]['content'] == '/exit':
    break
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  # But before here.

#This needed to be moved so the text file would generate instead of ongoing responses by model

 # if messages[-1]['content'] == '/exit':
   # break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)