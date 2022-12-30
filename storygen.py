import random 
name = ["Kaya", "Abhinav", "Michaele", "John", "Cyrus"]
location = ["Barcelona", "Ghana", "Delhi", "Switzerland", "Paris"]
job = ["attender",'philospher','professor','doctor','engineer']
short_story = ['came to a restaurant', 'lived happily forever', 'was confused', 'got a degree', 'decided to leave']
story = random.choice(name)+ " lives in " +random.choice(location)+ " works as a " +random.choice(job) + " and " +random.choice(short_story)+" end of the story "
print(story)