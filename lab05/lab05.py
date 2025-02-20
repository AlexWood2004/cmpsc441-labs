from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

import random
from util.llm_utils import run_console_chat, tool_tracker

# beauty of Python
@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def roll_for(skill, dc, player):
    n_dice = 1
    sides = 20
    roll = sum([random.randint(1, sides) for _ in range(n_dice)])
    if roll >= dc:
        return f'{player} rolled {roll} for {skill} and succeeded!'
    else:
        return f'{player} rolled {roll} for {skill} and failed!'

def process_response(self, response):
    # Fill out this function to process the response from the LLM
    # and make the function call 

        ###
        if response.message.tool_calls:
         self.messages.append({'role': 'tool',
                          'name': response.message.tool_calls[0].function.name, 
                          'arguments': response.message.tool_calls[0].function.arguments,
                          'content': process_function_call(response.message.tool_calls[0].function)
                         })
         response = self.completion()
         ###

        return response

run_console_chat(template_file='lab05/lab05_dice_template.json',
                 process_response=process_response)

#Successful Example produced: Agent: Welcome, adventurer! I am your Dungeon Master, guiding you through the realms of fantasy and danger. Our journey begins in the land of Eldoria, a realm of wonder and terror. The village of Oakwood lies before us, nestled at the edge of a vast forest. Rumors have been circulating about strange happenings in the village: livestock gone missing, eerie lights seen in the forest, and some 
#villagers whispering about an ancient evil stirring.
#
#You are a brave adventurer seeking fortune, fame, and danger. You stand outside the village inn, where travelers and locals gather to share tales and enjoy a pint of ale. The sun is setting, casting a warm orange glow over the village.
#
#What would you like to do?
#
#(Note: feel free to ask me about your character's abilities, equipment, or any other aspect of your adventure. I'll be happy to help!)
#You: I want to jump a canyon, need to roll for success
#
#
#Tools Called:
#defaultdict(<class 'list'>, {'process_function_call_calls': [{'name': 'process_function_call', 'args': (Function(name='roll_for', arguments={'dc': 5, 'player': 'canyon jumper', 'skill': 'Athletics'}),), 'kwargs': {}, 'result': 'canyon jumper rolled 19 for Athletics and succeeded!'}]})
#
#
#Agent: You've decided to take the leap of faith and jump across the canyon. You've got your trusty rope and grappling hook, and you're feeling confident in your abilities.
#
#As you stand at the edge of the canyon, you take a deep breath and prepare yourself for the jump. The wind rushes past you, whipping your hair into a frenzy. You focus on the landing spot below, visualizing the successful outcome.
#
#You sprint towards the edge of the canyon, your feet pounding against the rocky ground. You leap off the edge, soaring through the air with your rope and grappling hook at the ready. Time seems to 
#slow down as you plummet towards the canyon floor.
#
#Rolling for Athletics: **19**
#
#With a successful roll, you manage to time your jump perfectly, using your grappling hook to snag onto a nearby rock outcropping just as you're about to hit the ground. You swing across the canyon, the wind whipping through your hair, and land with a thud on the rocky floor.
#
#You've made it across the canyon! The villagers will be impressed by your daring feat. As you catch your breath, you notice that the canyon walls seem to be... shifting? The rocks appear to be moving, as if something is trying to get your attention.
#
#What do you do next?
#
#(Note: feel free to ask about your character's abilities, equipment, or any other aspect of your adventure!)
#You: /exit
