class Train:
  #class variable
  number_of_trains = 0

  def __init__(self, name, speed, length):
    Train.number_of_trains += 1
    self.name = name
    self.speed = speed
    self.length = length
  
  def get_name(self):
      return self.name

  def get_num_trains(self):
      return Train.number_of_trains

  def __eq__(self, other):
      return (self.name == other.name) and (self.speed == other.speed)

  # repr is used for returning a human readable representation of the object
  # by default it just return the memory address but we've defined it ourselves here
  # to return the name and speed

  # if __str__ isn't defined by the programmer then print() will use this
  def __repr__(self) -> str:
      return f"{self.name}, {self.speed}"

  # str is used for returning a pretty human readable representation
  # print() will use str (if it's defined by the programmer) over repr
  def __str__(self):
      return f"Train name: {self.name}, top speed: {self.speed}"
  
  def __len__(self):
      return self.length
  
  # defines a way to call an instance as if it were a function
  def __call__(self, scale):
      return Train(self.name, self.speed * scale, self.length)


train1 = Train("Thomas", 100, 5)
train2 = Train("Thomas", 100, 5)
# number_of_trains is 2

# showing how to use __call__
train1(2)
# showing how to use __len__
len(train1)
# showing how to use __eq__
train1 == train2 
# this will be true even though they're in different places in memory, because
# we defined __eq__ to be something else instead of equality by memory location
