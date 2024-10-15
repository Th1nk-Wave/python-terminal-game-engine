from typing import Any, List
from engine.types.color import color
from engine.soft_error import handler
import engine.enums.errors as error_enums
from engine.graphics.graphics import window

class UIdim:
  xpixel: int
  xpercent: float
  ypixel: int
  ypercent: float
  _absolute_xpixel: int
  _absolute_ypixel: int
  def __init__(self,xpixel:int,xpercent:float,ypixel:int,ypercent:float):
    self.xpixel = xpixel
    self.xpercent = xpercent
    self.ypixel = ypixel
    self.ypercent = ypercent
  def get_x_absolute(self,parent_width: float|int) -> int:
    absolute = self.xpixel + (parent_width * self.xpercent).__floor__()
    self._absolute_xpixel = absolute
    return absolute
  def get_y_absolute(self,parent_height: float|int) -> int:
    absolute = self.ypixel + (parent_height * self.ypercent).__floor__()
    self._absolute_ypixel = absolute
    return absolute
  def get_absolute(self,width,height):
    return UIdim(
      self.get_x_absolute(width),
      0,
      self.get_y_absolute(height),
      0
    )

  def __neg__(self):
    return UIdim(-self.xpixel,-self.xpercent,-self.ypixel,-self.ypercent)

  def __add__(self,val2):
    return UIdim(
      self.xpixel + val2.xpixel,
      self.xpercent + val2.xpercent,
      self.ypixel + val2.ypixel,
      self.ypercent + val2.ypercent
    )

  def __sub__(self,val2):
    if isinstance(val2,(int,float)):
      return UIdim(
        round(self.xpixel - val2),
        self.xpercent - val2,
        round(self.ypixel - val2),
        self.ypercent - val2
      )
    return UIdim(
      self.xpixel - val2.xpixel,
      self.xpercent - val2.xpercent,
      self.ypixel - val2.ypixel,
      self.ypercent - val2.ypercent
    )

  def __mul__(self,val2):
    if isinstance(val2,(int,float)):
      return UIdim(
        round(self.xpixel * val2),
        self.xpercent * val2,
        round(self.ypixel * val2),
        self.ypercent * val2
      )
    return UIdim(
      self.xpixel * val2.xpixel,
      self.xpercent * val2.xpercent,
      self.ypixel * val2.ypixel,
      self.ypercent * val2.ypercent
    )
  

class gui_element:
  position: UIdim
  size: UIdim
  anchor: UIdim
  z_index: int
  children: List[Any]
  parent: Any
  fill_color: color
  def __init__(self, position:UIdim, size:UIdim, anchor:UIdim, z_index:int, fill_color:color):
    self.position = position
    self.size = size
    self.anchor = anchor
    self.z_index = z_index
    self.fill_color = fill_color
    self.children = []
  
  def link_parent(self,parent):
    self.parent = parent

  def append(self,child):
    self.children.append(child)
  
  def get_children(self, sorted=True) -> List:
    if sorted: self.children.sort(key= lambda child: child.z_index)
    return self.children

  def get_position_local(self,parent=None) -> UIdim:
    if parent: self.link_parent(parent)
    elif self.parent: parent = self.parent
    else: handler.handle_error(error_enums.gui_error.no_parent); return UIdim(0,0,0,0)
    
    return UIdim(
      self.position.get_x_absolute(parent.size.get_x_absolute()),
      0,
      self.position.get_y_absolute(parent.size.get_y_absolute()),
      0
    )

  def draw_func(self, window, absolute_pos, absolute_size, anchor):
    pass


class frame(gui_element):
  fill_color: color
  border_color: color
  def draw_func(self, window, absolute_pos, absolute_size, anchor):
    top_left_corner = absolute_pos - anchor
    bottem_right_corner = (top_left_corner + absolute_size) - 1
    window.box(top_left_corner.xpixel,
                    top_left_corner.ypixel,
                    bottem_right_corner.xpixel,
                    bottem_right_corner.ypixel,
                    (self.fill_color.x,self.fill_color.y,self.fill_color.z)
                   )

class line(gui_element):
  def draw_func(self, window, absolute_pos, absolute_size, anchor):
    top_left_corner = absolute_pos - anchor
    bottem_right_corner = (top_left_corner + absolute_size) - 1
    window.line(top_left_corner.xpixel,top_left_corner.ypixel,bottem_right_corner.xpixel,bottem_right_corner.ypixel,(self.fill_color.x,self.fill_color.y,self.fill_color.z))

class text_box(gui_element):
  def __init__(self, text:str, position: UIdim, size: UIdim, anchor: UIdim, z_index: int, text_style = {0:[color(255,255,255),None]}):
    self.position = position
    self.size = size
    self.anchor = anchor
    self.z_index = z_index
    self.children = []
    self.text = text
    self.text_style = text_style

  def draw_func(self, window, absolute_pos, absolute_size, anchor):
    text_len = len(self.text)
    absolute_pos = absolute_pos - anchor
    current_color = (255,255,255)
    words = self.text.split(" ")

    current_pos_x = 0
    current_pos_y = 0
    for word in words:
      word_len = len(word)
      if (current_pos_x + word_len > absolute_size.xpixel*2) and (word_len < absolute_size.xpixel*2): current_pos_y += 1; current_pos_x = 0
      if current_pos_y > absolute_size.ypixel-1: return
      for letter in word:
        if current_pos_x > absolute_size.xpixel*2-1: 
          current_pos_y+=1; current_pos_x = 0
          if current_pos_y > absolute_size.ypixel-1: return
        window.add_text(current_pos_x+absolute_pos.xpixel*2,current_pos_y+absolute_pos.ypixel,letter,(255,255,255))
        current_pos_x+=1
      current_pos_x+=1


class gui:
  def __init__(self, graphics_window:window):
    self.window = graphics_window
    self.width = graphics_window.width
    self.height = graphics_window.height
    self.children = []

  def append(self, element:gui_element):
    self.children.append(element)

  def get_children(self, sorted=True) -> List[gui_element]:
    if sorted: self.children.sort(key= lambda child: child.z_index)
    return self.children

  def decend_tree_and_plot(self):
    self.window.remove_text()
    def inner(parent,parent_pos,parent_size):
      for child in parent.get_children():
        absolute_pos = (child.position + parent_pos).get_absolute(parent_size.xpixel,parent_size.ypixel)
        absolute_size = child.size.get_absolute(parent_size.xpixel,parent_size.ypixel)
        anchor = child.anchor.get_absolute(absolute_size.xpixel,absolute_size.ypixel)
        
        child.draw_func(self.window,absolute_pos,absolute_size,anchor)
        inner(child, absolute_pos - anchor, absolute_size)

    
    for child in self.get_children():
      absolute_pos = child.position.get_absolute(self.width,self.height)
      absolute_size = child.size.get_absolute(self.width,self.height)
      anchor = child.anchor.get_absolute(absolute_size.xpixel,absolute_size.ypixel)
      
      child.draw_func(self.window,absolute_pos,absolute_size,anchor)
      inner(child, absolute_pos - anchor, absolute_size)