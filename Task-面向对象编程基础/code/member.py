class Member:
  _id=1 #_开头变成私有属性（类属性）
  def __init__(self,name,group):
    self.name=name
    self.group=group
    self.points=0
    self.id=f"RM{Member._id:04d}"
    _id+=1
  #加分
  def add_points(self,points):
    if points>=0:
      self.points+=points
      return True
    return False
  #减分
  def cut_points(self,points):
    if 0<points<=self.points:
      return True
    return False
  #自动输出
  def __str__(self): #返回对象的“字符串表示形式”如果没有print出来的就是地址信息
    return f"{self.id}\t{self.name}\t{self.group}\t{self.points}"
    
    
    
  
