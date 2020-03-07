import os
names = os.listdir(os.getcwd())
text = ""
for name in names:
  
  text += """<a href=""><img src="imgs/urdu_novels/"""+name+""""></a> \n"""

print(text)
