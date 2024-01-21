class Rectangle:

  def __init__(self, width, height):
    self.width = int(width)
    self.height = int(height)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = int(width)

  def set_height(self, height):
    self.height = int(height)

  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    self.perimeter = 2 * self.width + 2 * self.height
    return self.perimeter

  def get_diagonal(self):
    self.diagonal = ((self.width**2 + self.height**2)**.5)
    return self.diagonal

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      n = 0
      h = ""
      l1 = ("*" * self.width) + '\n'  #primeira linha do retan.
      while n < (self.height - 2):
        #h+="*"+' '*(self.width-2)+'*\n' código para imprimir rect OCO
        h += '*' + "*" * (self.width - 2) + '*\n'
        n += 1
      l2 = "*" * self.width + "\n"  #ultima linha do retan.

      return l1 + h + l2

  def get_amount_inside(self, shape):

    amount_inside = self.get_area() // shape.get_area()
    return amount_inside


class Square(
    Rectangle
):  # HERANÇA: a classe square está herdando os métodos da classe rectangle

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"


