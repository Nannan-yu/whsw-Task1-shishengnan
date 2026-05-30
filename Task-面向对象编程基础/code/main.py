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
