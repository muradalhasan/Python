#contructor overloading and methods overloading
class SentenceAnalyzer:
    def __init__(self,a=None):
        self.str=a
    def set_sentence(self,str1):
        self.str=str1
    def get_word_count(self,a=None):
        if a==None:
            lst=self.str.split(" ")
            print(f"Number of words in the sentence: {len(lst)}")
        else:
            count=0
            lst=self.str.split(" ")
            for i in lst:
                if len(i)==a:
                    count+=1
            print(f"Number of words with {a} characters in the sentence: {count} ")
            
            
            
analyzer1 = SentenceAnalyzer()


analyzer1.set_sentence("That's an easy one")
print("1--------------------------")
analyzer1.get_word_count()
print("2--------------------------")
analyzer2 = SentenceAnalyzer("Like I said it's easy")


print("3--------------------------")
analyzer2.get_word_count()


print("4--------------------------")
analyzer2.get_word_count(4)
print("5--------------------------")
analyzer1.get_word_count(5)
