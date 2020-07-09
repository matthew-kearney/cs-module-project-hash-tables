def no_dups(s):
    # Your code here
    non_dup_keys = []
    if s == '':
        #empty string if there
        return ''
      #splits string
    l = s.split(' ')
    #turns list into a dict as keys and removes duplicates
    a = dict.fromkeys(l) 
    # loops through keys and appends them to the list of keys
    for key in a.keys(): 
        non_dup_keys.append(key)
    # joins together and returns with a space between each entry    
    return ' '.join(non_dup_keys) 



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))