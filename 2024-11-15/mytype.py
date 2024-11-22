class MyType:
    def __init__(self, x: int) -> None:
        self.value = x
    
    def inc(self) -> None:
        self.value += 1


if __name__ == '__main__':
    obj = MyType(20)
    print(f'obj\'s value is {obj.value}')
    obj.inc()
    print(f'obj\'s new value is {obj.value}')

