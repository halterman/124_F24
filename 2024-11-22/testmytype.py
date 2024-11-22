from mytype import MyType

mt = MyType()
mt2 = MyType()
print(f'mt = {mt.get()}')
print(f'mt2 = {mt2.get()}')
mt.inc()
print(f'mt = {mt.get()}')
print(f'mt2 = {mt2.get()}')
for i in range(10):
    mt2.inc()
print(f'mt = {mt.get()}')
print(f'mt2 = {MyType.get(mt2)}')
