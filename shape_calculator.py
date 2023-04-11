class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ''
    for i in range(0, self.height):
      for j in range(0, self.width):
        picture += '*'
      picture += '\n'

    return picture

  def get_amount_inside(self, shape):
    """
    Use 2 while loops, one with the condition that the big shape heigh >= shape.heigh and inside it we use another one with big shape width >= shape.width, inside we add 1 to a count variable and then from big shape widh extract shape.width, the on the fist while we finish with extracting from the big shape heigh the shape.heigh and then reseting the width of the big shape
    """
    width = self.width
    height = self.height
    count = 0

    while height >= shape.height:
      while width >= shape.width:
        count += 1
        width -= shape.width
      height -= shape.height
      width = self.width

    return count

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

  def __init__(self, length):
    super().__init__(length, length)
    self.width = length
    self.height = length

  def set_side(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    return f'Square(side={self.width})'
