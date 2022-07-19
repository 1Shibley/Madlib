import madlib_template
class madlibs:
    def __init__(self,word_category,template):
        self.word_categories=word_category
        self.template=template
def to_get_user_inputs(word_category):
    word=[]
    for category in word_category:
        print("enter one ",end='')
        user_input=input(category+' ')
        word.append(user_input)
    return word
#story
def create_story(template,word):
    story=template.format(*word)
    return story

template= "{} is a normal {}. Then one day, a {} explodes, causing a {} to blow up, a nearby {} erupts into a {} of flames. He realized that he is being chased by the government, who is trying to {} him. "
word=to_get_user_inputs(["A Man's name","Occupation","Noun","Noun","Noun","shape","verb"])
story=create_story(template,word)
print(story)