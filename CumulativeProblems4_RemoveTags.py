# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(words):
    #way 1
    start = -1
    end = -1
    for c in words:
        if c == '<':
            start = words.index('<')
        elif c == '>':
            end = words.index('>')
        if start != -1 and end != -1:
            words = words[:start] + ' ' + words[end+1:]
            start = -1
            end = -1
    return words.split()
    
    #way 2
    start = words.find('<')
    while start != -1:
        words = words[:start] + ' ' + words[words.find('>',start)+1:]
        start = words.find('<')
    return words.split()



print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
