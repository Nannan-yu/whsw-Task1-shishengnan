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
  #查找队员
  def find_id(self,member_id):
    for m in self.member:
      if m.id==member.id:
        return m
    return False
  #加分
  def add_ponts(self,member_id,points):
    member=self.find_id(member_id)
    if not member:
      print(f"×未找到编号{member_id}的队员")
      return False
    member.add_points(points)
    print(f"✔成功为{member.name}增加了{points}，当前积分为{member.points}")
  #减分
  def cut_ponts(self,member_id,points):
    member=self.find_id(member_id)
    if not member:
      print(f"×未找到编号{member_id}的队员")
      return False
    member.cut_points(points)
    print(f"✔成功为{member.name}扣除了{points}，当前积分为{member.points}")  
  #排名
  def get_points(self):
    return m.points
  return sorted(self.member,key=get_points,reverse=True)
  def show_rankings(self):
    ranked = self.get_points()
    if not ranked:
      print("暂无队员数据")
      return
    print("\n积分排行榜")
    print("排名\t编号\t姓名\t组别\t积分")
    print("——" * 30)
    for idx, m in enumerate(ranked, 1):
      print(f"{idx}\t{m.id}\t{m.name}\t{m.group}\t{m.points}")
  #删除
  def delete_member(self, member_id):
    member = self.find_id(member_id)
    if not member:
      print(f"×，未找到编号 {member_id} 的队员")
      return False
    print(f"⚠ 即将删除：{member.id} {member.name} {member.group} {member.points}分")
    if self._confirm_deletion():
      self.members.remove(member)
      print(f"✔，队员 {member.id} {member.name} 已删除")
      return True
    else:
      print("已取消删除")
      return False
  def _confirm_deletion(self):
    return input("确认删除？(y/n)：").strip().lower() == 'y'
