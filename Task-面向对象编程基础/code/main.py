from member_manager import MemberManager
def print_menu():
  print("\n======== RoboMaster 队员积分管理系统 ========")
  print("1. 添加队员")
  print("2. 查看所有队员")
  print("3. 为队员加分")
  print("4. 为队员扣分")
  print("5. 按积分排名")
  print("6. 删除队员")
  print("7. 退出系统")
def add_member(mgr):
  print("\n--- 添加队员 ---")
  name = input("请输入队员姓名：").strip()
  group = input("请输入组别（视觉/电控/机械/运营）：").strip()
  mgr.add_member(name, group)
def list_member(mgr):
  print("\n--- 所有队员 ---")
  mgr.all_member()
def add_memberpoints(mgr):
  print("\n--- 为队员加分 ---")
  member_id = input("请输入队员编号：").strip()
  points = int(input("请输入要加的分数："))
  mgr.add_points(member_id, points)
def cut_memberpoints(mgr):
  print("\n--- 为队员扣分 ---")
  member_id = input("请输入队员编号：").strip()
  points = int(input("请输入要扣的分数："))
  mgr.cut_points(member_id, points)
def rank_members(mgr):
  print("\n--- 积分排行榜 ---")
  mgr.show_rankings()
def delete_members(mgr):
  print("\n--- 删除队员 ---")
  member_id = input("请输入要删除的队员编号：").strip()
  mgr.delete_member(member_id)

