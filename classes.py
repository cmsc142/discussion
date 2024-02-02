class Train:
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

  def __repr__(self) -> str:
      return f"{self.name}, {self.speed}"

  def __str__(self):
      return f"Train name: {self.name}, top speed: {self.speed}"
  
  def __len__(self):
      return self.length
  
  def __call__(self, scale):
      return Train(self.name, self.speed * scale, self.length)


train1 = Train("Thomas", 100, 5)
train1(2)