def my_push(item):
      my_stack.append(item)

def my_pop():
      if len(my_stack)!=0:
            item=my_stack.pop(-1)
            return item

my_stack=[]
my_push('apple')
my_push('pear')
my_push('mango')
      
print(my_stack)

my_pop()
print(my_stack)
