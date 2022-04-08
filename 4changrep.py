import basc_py4chan
import re
import os

#def clean_text(text):
#    return re.sub(">>\d\d\d\d\d\d\d\d", "", text).replace("\n", " ").replace(":", "").replace(">", "").replace("-", "").replace(",", "").replace("\"", "").replace("*", "").replace("[", "").replace("]", "").replace("\'", "").replace("`", "").replace("&", "and").strip()

def clean_text(text):
    return re.sub('[^A-Za-z0-9]+',' ', re.sub(">>\d\d\d\d\d\d\d\d", "", text))

def clean_file():
    with open(board + ".yml", "r+") as f:
        d = []
        d = f.readlines()
        i = 0
        while i < len(d):
            if re.match("- - ", d[i]):
                if not i+2 > len(d):
                    if not re.match("  - ", d[i+1]):
                        
                        d.pop(i)
                    else:
                        i+=1
                else:
                    d.pop(i)
                    i+=1
            else:
                i+=1
        i = 0
        while i < len(d):
            if d[i] == "- - \n" or d[i] == "  - \n":
                d.pop(i)
            elif d[i] == "- -  \n" or d[i] == "  -  \n":
                d.pop(i)
            else:
                i+=1
        f.truncate(0)
        f.seek(0)
        for text in d:
            f.write(text)

board = input("what board? ")
b = basc_py4chan.Board(board)
file = open(board + ".yml", "a+")
file.write("categories:\n- " + board + "\nconversations:")
print("generating...")
for thread in b.get_all_threads(expand=True):
    if not thread.sticky and len(thread.replies) > 0:
        for mpost in thread.posts:
            if not clean_text(mpost.text_comment).isdigit() and not clean_text(mpost.text_comment) == '':
                print("pulling: " + str(thread.id));
                file.write("\n- - " + clean_text(mpost.text_comment))
                for rpost in thread.posts:
                    if not clean_text(rpost.text_comment).isdigit() and not clean_text(mpost.text_comment) == '':
                        if ">>" + str(mpost.post_id) in rpost.text_comment:
                            file.write("\n  - " + clean_text(rpost.text_comment))

print("\ncleaning file...")
file.close()
file = open(board + ".yml", "r+")
clean_file()