class TestResistance(object):
  def __init__(self):
    self._test_val = 0
    self._getset_val = 5
  
  @property
  def test_val(self):
    return self._test_val

  @test_val.setter
  def test_val(self, value):
    self._test_val = value
  
  #User用の出力
  def __str__(self):
    return "Resutl for User"
  
  #デバック用の出力
  def __repr__(self):
    return "Result for Debug"
  
  def __get__(self, instance, instance_type):
    return "instance: " + str(self._getset_val) + " " + str(instance) + ":" + str(instance_type)
  
  def __set__(self, instance, value):
    self._getset_val = value

class Test2(object):
  hogehoge = TestResistance()

if __name__ == "__main__":
  c1 = TestResistance()
  c1.test_val = 10
  val = c1.test_val
  print("get setter val: ", str(val))
  print(str(c1))
  print(repr(c1))

  c2 = Test2()
  print(c2.hogehoge)
  c2.hogehoge = 10
  print(c2.hogehoge)

  