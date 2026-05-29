class Member:
  _id=1 #_开头变成私有属性（类属性）
  def __init__(self,name,group):
    self.name=name
    self.group=group
    self.points=0
    self.id=f"RM{Member._id:04d}"
    _id+=1

