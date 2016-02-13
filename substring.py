def find_sub_string(word, string):
        len_word = len(word)  #returns 3

        for i in range(len(string)-1):
            if string[i: i + len_word] == word:
            	return True

        else:
            	return False

print find_sub_string("aaa","lalalaaaa")

