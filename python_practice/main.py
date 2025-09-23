class Counter:
    def __init__(self):
        self._value=0
    def increment(self):
        self._value+=1
    def decrement(self):
        self._value-=1
    def reset(self):
        self._value=0
    def get(self):
        return self._value
def main():
    counter =Counter()
    for i in range(10) :
        counter.increment()
    print(counter.get())

if __name__ == '__main__':
    main()