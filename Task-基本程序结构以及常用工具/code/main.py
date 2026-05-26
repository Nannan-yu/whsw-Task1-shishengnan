import random
#查看区间有几个小数
def num(s):
  if '.' in s:
    return len(s.split(".")[1])
  else ：
    return 0

#将输入的区间分开
def divi(s):
  a,b=s.split("-")
  c=max(num(a),num(b))
  return float(a),float(b),c

#生成随机数
def r(f,e,l):
  if l==0:
    return random.randint(int(f),int(e))
  else :
    return round(random.randint(f,e),2)
    
#游戏过程
def play():
  while True:
    try:
      f,e,l=divi(input("请输入区间范围，例如：100.00-200.000"))
      if f<e:
        break
     except:
        pass
  number=r(f,e,l)
  max_try=int(input("输入最大重试次数"))
  a=[]
  for i in range (1,max_try+1):
    while True:
      try:
        print(f"还剩{max_try-i+1}次")
        guess=int(input({"请输入"+l+"位小数点以内的数字"))
        break
      except:pass
    a.append(guess)
    if guess==number:
      print(f"恭喜你猜对了，一共试了{i}次")
      break
    elif guess<number:
      print("太小了")
    else :
      print("太大了")
else:
  print(f"游戏结束，答案是{number}")

#描述路径
if not a:
  pass
else:
  result=str(a[0])
  for i in range (1,len(a)):
    if a[i]>a[i-1]:
      b="↑"
    else:
      b="↓"
    result+=f"{a}→{a[i]}"
  if a[-1]==number:
    result+="√"
  print("轨迹："，result)
  
#主函数
while input("是否重新开始（YES/N0）")=="YES":
  play()
      
