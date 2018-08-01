#!python3
'''
Find common typos such as multiple   spaces between words, 
accidentally accidentally repeated words, 
or   multiple exclamation marks at the
end of sentences. Those are annoying!!
'''
import re,pyperclip
text= pyperclip.paste()
lines= text.split('\n')

multiSpaceRegex = re.compile(r"\s+")
doubleWordRegex = re.compile(r"([A-Za-z]+) \1")
multiExclaimMarks = re.compile(r"!!+$")
newtext=[]
for line in lines:
	line = multiSpaceRegex.sub(" ",line)
	line = doubleWordRegex.sub(r'\1',line)
	line = multiExclaimMarks.sub(r'!',line)
	newtext.append(line)

pyperclip.copy('\n'.join(newtext))
print("Copied to clipboard:")
for i in newtext:
	print(i)