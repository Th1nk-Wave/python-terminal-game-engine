class vec3:
  def __init__(self,x=0.0,y=0.0,z=0.0):
    self.x = x
    self.y = y
    self.z = z

  def __neg__(self):
    return vec3(-self.x,-self.y,-self.z)

  def __add__(self,val2):
    if type(val2) == int or type(val2) == float:
      return vec3(self.x + val2,self.y + val2, self.z + val2)
    else:
      return vec3(self.x + val2.x,self.y + val2.y, self.z + val2.z)

  def __iadd__(self,val2):
    if type(val2) == int or type(val2) == float:
      self.x += val2
      self.y += val2
      self.z += val2
    else:
      self.x += val2.x
      self.y += val2.y
      self.z += val2.z
    return self

  def __sub__(self,val2):
    if type(val2) == int or type(val2) == float:
      return vec3(self.x - val2,self.y - val2, self.z - val2)
    else:
      return vec3(self.x - val2.x,self.y - val2.y, self.z - val2.z)

  def __isub__(self,val2):
    if type(val2) == int or type(val2) == float:
      self.x -= val2
      self.y -= val2
      self.z -= val2
    else:
      self.x -= val2.x
      self.y -= val2.y
      self.z -= val2.z
    return self

  def __mul__(self,val2):
    if type(val2) == int or type(val2) == float:
      return vec3(self.x * val2,self.y * val2, self.z * val2)
    else:
      return vec3(self.x * val2.x,self.y * val2.y, self.z * val2.z)

  def __rmul__(self,val2):
    return vec3(self.x * val2,self.y * val2, self.z * val2)

  def __imul__(self,val2):
    if type(val2) == int or type(val2) == float:
      self.x *= val2
      self.y *= val2
      self.z *= val2
    else:
      self.x *= val2.x
      self.y *= val2.y
      self.z *= val2.z
    return self

  def __truediv__(self,val2):
    if type(val2) == int or type(val2) == float:
      return vec3(self.x / val2,self.y / val2, self.z / val2)
    else:
      return vec3(self.x / val2.x,self.y / val2.y, self.z / val2.z)

  def __idiv__(self,val2):
    if type(val2) == int or type(val2) == float:
      self.x /= val2
      self.y /= val2
      self.z /= val2
    else:
      self.x /= val2.x
      self.y /= val2.y
      self.z /= val2.z
    return self

  def __floordiv__(self,val2):
    if type(val2) == int or type(val2) == float:
      return vec3(self.x // val2,self.y // val2, self.z // val2)
    else:
      return vec3(self.x // val2.x,self.y // val2.y, self.z // val2.z)

  def __ifloordiv__(self,val2):
    if type(val2) == int or type(val2) == float:
      self.x //= val2
      self.y //= val2
      self.z //= val2
    else:
      self.x //= val2.x
      self.y //= val2.y
      self.z //= val2.z
    return self