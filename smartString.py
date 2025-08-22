class smartString:
    def __init__(self,text):
        self.string=text
    def to_title_case(self):
        return self.string.title()
    def to_lower_case(self):
        return self.string.lower()
    def to_upper_case(self):
        return self.string.upper()
    def reverse(self):
        return self.string[::-1]
    def __str__(self):
        return self.string
    def remove_vowels(self):
        return ''.join(c for c in self.string if c.lower() not in 'aeiou')
    def __len__(self):
        return len(self.string)

def main():
    string=input('Enter a string:\n')
    s= smartString(string)
    print(s.to_title_case()+'\n')
    s.reverse()
    print(s.to_lower_case()+'\n')
    print(s.remove_vowels()+'\n')

if __name__ == '__main__':
    main()