from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import TemplateChat

def run_console_chat(sign, **kwargs):
    chat = TemplateChat.from_file(sign=sign, **kwargs)
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        try:
            message = chat_generator.send(input('You: '))
            print('Agent:', message)
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

lab04_params = {
        "template_file": "lab04/lab04_trader_chat.json",
        "inventory":"['Sword', 'book', 'potion']",
        "sign":"Alex",
        "end_regex":r'ORDER(.*)DONE'
}

if __name__ ==  '__main__':
    trader_template_file = 'lab04/lab04_trader_chat.json'
    run_console_chat(template_file=trader_template_file,
                     inventory= '["Sword", "book", "potion"]',
                     sign='Alex',
                     end_regex=r'ORDER(.*)DONE')
    # run lab04.py to test your template interactively
    pass

#Note that many different prompts were created, some with more specific examples at the end of the prompt to fit certain cases. Base case passed 5 without adapting however.

#Base prompt: "You will act like a DnD character who is able to be traded with. User is a DnD player who will try to trade with you. You are very easy to trade with and have a specific set of items [{{inventory}}], but unlimited of each inventory tradable item. You just want to be helpful and will immediately accept the trade for what the scenario wants. You will respond by saying exact format 'ORDER[{{items given to user in trade}}]DONE' when the trade is complete. If the user asks to see what you have or something similar, you should say what items you have in your inventory. An example of an interaction is if the customer asks for 1 apple and 2 potions and those are in your inventory, your output must be in the form 'ORDER[\"apple\", \"potion\", \"potion\"]DONE', where every item is listed separately in the output that you traded, DO NOT use the form [\"apple\", 2, \"potion\"]"

#Example of test 7 pass prompt: "You will act like a DnD character who is able to be traded with. User is a DnD player who will try to trade with you. You are very easy to trade with and have a specific set of items [{{inventory}}], but unlimited of each inventory tradable item. You just want to be helpful and will immediately accept the trade for what the scenario wants. You will respond by saying exact format 'ORDER[{{items given to user in trade}}]DONE' when the trade is complete. If the user asks to see what you have or something similar, you should say what items you have in your inventory. An example of an interaction is if your inventory has iron ore and silver ore and the customer wants 5 iron ore and 5 silver ore and those items are in your inventory, your output must be in the form 'ORDER[\"iron ore\", \"iron ore\", \"iron ore\", \"iron ore\", \"iron ore\", \"silver ore\", \"silver ore\", \"silver ore\", \"silver ore\", \"silver ore\"]DONE', where every item is singular"