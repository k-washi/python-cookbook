class LazyDB(object):
  def __init__(self):
    self.exists = 5
  def __getattr__(self, name):
    value = 'Value for {}'.format(name)
    setattr(self, name, value)
    return value

class LoggingLazyDB(LazyDB):
  def __getattr__(self, name):
    print('Called __getattr__{}'.format(name))
    return super().__getattr__(name)



if __name__ == '__main__':
  data = LazyDB()
  print(data.__dict__)
  print(data.foo)
  print(data.__dict__)
  print(data.foo)

  print("-"*30)

  data = LoggingLazyDB()
  print(data.__dict__)
  print(data.foo)
  print(data.__dict__)
  print(data.foo)

  