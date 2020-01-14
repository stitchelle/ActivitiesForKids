# Function and variable names are snake case instead of camel case
def run(name):
    return f"{name} was running."

def swing(name):
    return f"{name} was swinging."

def slide(name):
    return f"{name} going down the slide."

def hide_and_seek(name):
    return f"{name} is playing hide and seek."

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for x in running_kids:
  print(run(x))

for x in swinging_kids:
  print(swing(x))

for x in sliding_kids:
  print(slide(x))

for x in hiding_kids:
  print(hide_and_seek(x))