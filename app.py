import openai

####################


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


openai.api_key = open_file('../openaiapikey.txt')
####################


def gpt3(prompt, temperature=0.7, frequency_penalty=0, presence_penalty=0):
    messagein = [
        {"role": "user", "content": prompt}
        # {"role": "system", "content": chatbot}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=messagein
    )
    text = response['choices'][0]['message']['content']
    return text


ytopic = input("what is your story about? ")

# WRITE YOUR STORY HERE

plot = open_file('prompt.txt').replace('<<PLOT>>', ytopic)
plot2 = gpt3(plot)
print('\n\nStory: ', plot2)
save_file('story.txt', plot2)

# CREATE SCENES
storyinput = open_file('story.txt')
storyscenes = open_file('prompt2.txt').replace('<<STORY>>', storyinput)
storyscenes2 = gpt3(storyscenes)
print('\n\nScenes: ', storyscenes2)
save_file('scenes.txt', storyscenes2)

# MIDJOURNEY PROMPTS
mjprompt = open_file('mjprompts.txt')
mjprompt1 = open_file('prompt3.txt').replace(
    '<<MJP>>', mjprompt).replace('<<SCENE>>', plot2)
mjprompt2 = gpt3(mjprompt1)
print('\n\nMid-Journey Prompts: ', mjprompt2)
save_file('mjprompts2.txt', mjprompt2)

# VOICEOVER
narrator = open_file('VO.txt').replace('<<STORY>>', plot2)
narrator2 = gpt3(narrator)
print('\n\nVO Script: ', narrator2)
save_file('voiceoverscript.txt', narrator2)
####################
# deliverables:
# text file with story
# text file with scenes
# text file with mid-journey prompts
# text file with voiceover script
