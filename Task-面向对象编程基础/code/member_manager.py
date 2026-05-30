class MemberManager:
  groups=["视觉","电控","机械","运营"]
  def __init__(self):
    self.members=[]
  #判断组别是否正确
  def _judgegroup(self,group):
    return group in self.groups
  #判断姓名是否重复
  def _judgename(self,name):
    for i in self.members:
      if 
