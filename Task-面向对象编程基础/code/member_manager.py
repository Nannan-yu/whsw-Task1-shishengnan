class member import Member
class MemberManager:
  groups=["视觉","电控","机械","运营"]
  def __init__(self):
    self.members=[]
  #判断组别是否正确,正确True
  def _judgegroup(self,group):
    return group in self.groups
  #判断姓名是否重复，重复True
  def _judgename(self,name):
    for i in self.members:
      if i.members ==name:
        return True
    return False
  #增加成员
  def add_member(self,name,group):
    if not _judgegroup(group):#if后面为True则执行
      print("×，没有这个组")
      return False
    if _jugdename(name):
      print(f"×，队员{name}已存在")
      return False
    member=Member(name,group)
    self.member.append(member)
    print(f"✔添加成功！队员编号：{member.__nextid},姓名：{member.name},组别：{member.group},初始加分：{member.points}")
    return True
  #查看所有队员
  def all_member(self):
    if not self.members:
      print("暂无队员数据")
      return None
    print("\n编号\t姓名\t组别\t积分")
    print("——"*30)
    for m in self.members:
      print(m)
  #加分
  def add_ponts
      
