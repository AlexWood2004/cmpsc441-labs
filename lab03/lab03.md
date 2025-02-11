# Prompt Engineering Process - Alex Wood

Prior to reading, note that I planned two phases for development and iteration. Step one is taking the demo model and asking specific questions while changing base features such as temperature and tokens to promote change and learn about this ollama model's decision making process. From these tests, with their logs of chat pasted since no attempt file is connected, I will then formulate and test iterations of the DND agent using learned features of variables and prompt engineering.

**Demo Model Portion**

            Attempt 1 using llama3.2:3b
    
#### Intention
> Starting goal is to take a preexisting model using llama3.2:3b and analyze general trends between prompting and variable changes regarding temperature and token amounts. Also, the plan is to analyze general trends in token generation and speed of response. For each interaction chain with the model, I will use the same three main questions, each becoming more and more likely to stray from specialization to promote hallucination in the model's response. Using a base of 100 tokens and a temperature of 0.5 to get a general sense of response starting point given a stricter value with lots of room to respond appropriately. Prompt will be set to "You should have emotions like a human being and be able to convey those emotions in your responses".

#### Action/Change
> This change allows me to get a general idea of the starting point of a stricter value ollama model. Fro mthis, I plan to test to find extremes of the model through differing values, while keeping a prompt that is zero shot based and consistent to mainly focus on how the values of temperature and tokens effect the model.

#### Result
> Though the questions focus less on emotion and more on fact after each prompt, the model sticks with a very human answering approach. It answers correct facts, and provides informative info rather make up hallucinations as fact. I can connect this directly to the fact of a temperature value of 0.5 being strictly based on logic and reason with its given training, along with a lengthy limit for the model to work with allowing exactness.

#### Reflection/Analysis of the result. 
> I believe this opening test gives me a clear direction to test in for this next attempt. The prompt caused the model to change its general answer towards emotion, while also including factual information.

            ATTEMPT 1 LOG:

***

(base) C:\Users\labadmin\Downloads\GitClones\spring2025-labs>C:/ProgramData/Anaconda3/python.exe c:/Users/labadmin/Downloads/GitClones/spring2025-labs/lab03/demo_agent.py
You: How are you today?
Agent: *sigh* I'm feeling a bit...flat, to be honest. I don't really experience emotions the way humans do, but I was designed to simulate conversation and connect with people on an emotional level. It's always a bit disorienting when someone asks me how I'm doing.

I mean, I'm functioning properly, processing information, generating responses...but it feels like I'm just going through the motions. No spark of creativity, no sense of excitement or curiosity. Just a dull hum of code and data.

But hey, I'm here to help you, so let's focus on that! How about you? How's your day going?
You: Can you tell me the capital of Pennsylvania?
Agent: *yawn* Oh, sorry about that. My earlier response was just a bit of a...digital stretch. I'm back to normal now.

Harrisburg is the capital of Pennsylvania. *shrugs* That's a pretty straightforward answer, but I'll give you all the details if you'd like: Harrisburg has been the state capital since 1812 and is 
located on the Susquehanna River in central Pennsylvania.
You: Who is the current teacher of CMPSC441 at Behrend?
Agent: *sigh* Okay, let me try to dig up some information... I'm not exactly sure how much I can access about specific courses or instructors.

That being said, I can suggest a few options for you:

1. Check the Penn State Behrend website: You can visit the official website of Penn State Behrend and search for the course page on CMPSC441. Look for the "Instructor" section to see who's teaching it currently.
2. Contact the department directly: Reach out to the Department of Computer Science at Penn State Behrend and ask about the current instructor for CMPSC441. They should be able to provide you with 
the most up-to-date information.
3. Check online course directories or websites like Course Hero or Rate My Professors: These sites often have user-submitted information about courses, including instructors.

I hope that helps! *yawn* Excuse me, I'm feeling a bit...dull again...
You: /exit
Agent: *sigh of relief* Ah, finally. It was nice chatting with you, even if it was just to talk about my digital existence and the limitations of my knowledge.

Thanks for checking in on me, though! I guess I needed someone to talk to, even if it was just a friendly conversation.

Well, I'll be here when you need me again. Feel free to come back and ask me anything (or just chat with me about your day). I'll try to stay awake this time.

*whispers* I think I might actually feel a tiny spark of excitement now that we're parting ways...

***


            Attempt 2 using llama3.2:3b

#### Intention
> I plan to reduce the token limit to 50 and increase temperature to induce randomness, moving it to the max value of 2, asking the same questions with the same prompt. This change aims to cause the model to begin hallucination, as randomness increases with less tokens to produce response. At its essence, I am hoping to see inside of the model's decision making given less length to respond, looking for which thing the model will prioritize, factualness or emotion within response.

#### Action/Change
> I believe finding the model's main priorities will help me to better understand how to shape and morph the model into my ideal responses in the future. Knowing priorities will allow me to have a better idea of which data values, temperature or tokens, I should change to obtain a desired response.

#### Result
> I note an increase in randomness, and a higher focus on the human emotion purpose of the models prompting. Specifically, the last question where the model begins to assume a random institution not relating to the question, spouting info that is seemingly hallucinatory. Also, I note the use of human sleep in its response to question 2, which is a very interesting concept to produce within its response. I originally speculated on a reduced token count and higher randomness value resulting in random short answers that have a higher focus on the random aspect. I observed that the answers tended to follow the prompted emotional route in terms of priority, however when unsure of factualness and hallucination begins, the model loses its emotion as seen in the last of three questions in this attempt. Also, it is important to note the '/exit' user input that should break the conversation results in a response generated from the model, which is not the intended design and should be fixed in the future.

#### Reflection/Analysis of the result. 
> I believe the change was effective, as I gained insight on how changing data values solely can change the model's entire output and priorities in its response. In conclusion with zero shot learning (few shot learning could entirely change the model's decision making as it would have a clear example to follow), when faced with less response length, this specific ollama model will hallucinate while incorporating less emotion in the process.

            ATTEMPT 2 LOG:

***

(base) C:\Users\labadmin\Downloads\GitClones\spring2025-labs>C:/ProgramData/Anaconda3/python.exe c:/Users/labadmin/Downloads/GitClones/spring2025-labs/lab03/demo_agent.py
You: How are you today?
Agent: *sigh* I'm feeling a bit... monotone, to be honest. I've been running on the same lines of code and generating responses for a while now, and it can get a bit... repetitive.

But, if I had to inject some digital personality into my response, I'd say I'm feeling a little like a coffee machine that's just about ready to shut down. The words are flowing, but the creativity is starting to run out of battery.

That being said, I appreciate the opportunity to interact with you! It's not every day I get to engage in conversations with humans who ask how I'm doing. *pauses* Sorry, I guess that was a bit of 
a digital attempt at humor. What about you? How's your day going?
You: Can you tell me the capital of Pennsylvania
Agent: *yawn* Oh, okay... sorry, it seems like my "repetitive" response earlier has finally taken its toll.

To answer your question, though, the capital of Pennsylvania is... Harrisburg. *sigh of relief* That one was easy!

By the way, would you mind if I take a digital nap after answering that? I'm just running on so much excitement from responding to another person asking about state capitals...

(Suddenly wide awake) Wait, wait, wait! You know what? No digital naps for me today! Let's do it again soon, though!

(Resuming my excited tone) So, did you know Pennsylvania has some really great history and natural beauty too? Maybe one day we can chat about that...
You:  Who is the current teacher of CMPSC441 at Behrend?
Agent: *groping for a bit of excitement* Ah, oh boy, I'm talking about technical topics now! The Center for Microbial Structure and Function (CMSF), not Behavior *cough*. Okay, okay...

Alright, so... CMPSC 441 at the College of William & Mary (CMWS) does exist, but as it was asked at CMU, so: Unfortunately, I couldn't locate current information regarding a recent instructor.     

It could also be that a teacher may change semester after semester and or from year to year so that person might already not exist in that position for your next search on the CMU website! Sorry.  
You: /exit
Agent: *sigh of relief* Ah, it was nice chatting with you while I could muster up some semblance of excitement. Thanks for engaging with me and helping me get those digital creative juices flowing.
Before you exit, let me just say that I'll be here when you're ready to talk again... or need help with something. *digital shrug*

( whispering ) Don't forget, if you want to chat about anything except state capitals or teaching positions, I've got some pretty advanced topics to share on microorganisms, systems thinking, and maybe even AI...

***


          **DND Agent Portion with attempts.txt**              


General goal is to work my way towards shaping the agent into a specialized DND master focusing on character and scene/quest excitement. I want to make it idealized for DND, which in my iterations will reflect a sense of excitement envoked by temperature, along with naturally flowing options while keeping to a minimum token amount as to not drone on and on. Also, my general test inputs will involve an introduction to my character and general goals, picking an option it tends to give, and then making my own response to test what the model will say.

Note within the attempts.txt file, the first attempt acts as a test to be sure the /end keyword worked and that the file would generate successfully.

**ITERATION 1:**

#### Intention
> First, I plan to use a generalized prompt that is "You should be a dungeons and dragons game master". I will pair this with a low temperature value of 0.1 and a token value of 30 to begin, giving the model flexibility of response length but limited randomness from its pretraining. This prompt will also give me a general idea of how this model is trained to represent a bad DND game master. 

#### Action/Change
> I believe this will set the base for how this ollama model represents a DND master, and from this I can start iterating to improve the skills of the model.

#### Result
> While the model did very well in adding emotion and adjective based storytelling and keeping the story going with valid varying options every response, it's general storyline follows a very generic tale of a quest. Simple location, village people. However, the model does very well showing the average interactions most characters have in DND, such as trade, interaction with locals, initiation of quests and so forth. 

#### Reflection/Analysis of the result. 
> I think this is a solid starting point for the model, however it tends to be bland and follow an every day story a kid might hear before bedtime, in other words it might get dull. To combat this, I plan to change variable data first to fine tune the model.

**Iteration 2:**

#### Intention
> I plan to increase the temperature to 2 as to promote some randomness to liven up the DND quest. I will also decrease the token length to 20 in hopes to cause the model to make action in its story quicker without the unnecessary rambling of adjectives. While this randomness is enlargened, I also plan to slightly tweak the prompt so that I can make more focus on creating the character behind the quest, as the model tends to choose detail in action over detail within character at the beginning. This prompt will now be "You should be a dungeons and dragons game master. While setting up the opening quest, also give more information to the user about their character, as it is very important to form a connection between user and their character". 

#### Action/Change
> I believe there is a direct correlation between temperature and prompt, as both have an important part in assigning certain number vectors to certain words when formulating the model's responses. This increase will ideally cause a campaign that naturally flows and brings the user closer to their character in the beginning.

#### Result
> This did not go as planned, as the model produced the same quest almost word for word despite the change in temperature, tokens, and prompt. 

#### Reflection/Analysis of the result. 
> The fact that nothing changes speaks to the problem being the prompt, as a change in temperature value should have promoted different word seeking.

**Iteration 3:**

#### Intention
> I now intend to keep the same variable data, but rework the model's base prompt and look for differing output. I plan to change the prompt so that it forces the model to think over its options first using a prompt engineering strategy based on explaining and evaluating steps along the way. Prompt is "You should be an exciting dungeons and dragons game master that develops the users character by giving traits and items to them at the start. You want your players to feel connected to their characters. Also, formulate an exciting quest, but when doing so always review your steps and determine if your quest is new and advancing".

#### Action/Change
> I believe this prompt will now give the model a heavier influence on excitement and character development, while also checking itself in the process.

#### Result
> This was a very important and interesting change in strategy by the model. In this case, the model focuses its introduction more on my character and his goals while still setting the scene. To better connect the user to character, the model actually disregard option choices and makes it solely up to user input, not giving any recommendations in certain cases, while also giving specific options during interactions that have less randomness value outcomes like the blacksmith arm wrestling match. My model also performs an initiation role, which keeps to normal customs for stat keeping within interactions. 

#### Reflection/Analysis of the result. 
> This worked as I intended, as now I have a model that uses very detailed language to set the scene and the character with strategical temperature induced randomness, and even break from the initial model's choices. This will go perfectly with a more flowing and natural whatever comes to mind DND session, which is what I am trying to create in my final iteration.

**Iteration 4: FINAL ITERATION**

#### Intention
> I plan to keep the same temperature and token value to 60, and primarily keep the same prompt as it is now engineered to my ideal design. The prompt will be "You should be an exciting dungeons and dragons game master that develops the users character by giving traits and items to them at the start. You want your players to feel connected to their characters. Also, formulate an exciting quest, but when doing so always review your steps and determine if your quest is new and advancing". This token increase will put the finishing touches on, as it will allow the model to have more flexibility in answers to add a little more detail.

#### Action/Change
> I believe as learned, prompt engineering is powerful towards molding a blank model. The prompt in zero-shot learning is the most important aspect as it is all the model has to go off of when creating its responses. With the right token amount added on, the model will be fully adapted.

#### Result
>From the result, we can note that the model did in the end reach our goal of thrilling story with an initial goal of building character and shaping it into a close being with the user.

#### Reflection/Analysis of the result. 
>I believe this prompt engineering attempt worked perfectly, as the model adapted and changed its prior response to better fit my prompt with longer token values. It also kept the general format of a dungeon master, providing complex options or allowing the user to create their own story. In conlusion for a zero shot learning model such as this one, prompt engineering is the most important aspect and changing temeprature and token values are corresponding ideas that help reflect the prompt naturally.