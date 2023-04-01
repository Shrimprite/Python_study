#game 1.0.0
import time as t ,random as r , turtle as tur
fbx_att=r.uniform(100,100001)
mss_cure=r.randint(100,1001)
byg_life=r.uniform(0.01,100000)
byg_att=r.uniform(0.01,100000)
gtx_att=r.choice([10000,17500,22500])
zs_att=r.randint(10,10000001)
heros={'拳击手':[10000,25000],
       '铁巨人':[20000,10000],
       '黑骑士':[15000,15000],
       '飞镖侠':[10000,fbx_att],
       '大石头':[100000,100],
       '魔法师':[15000,10000,mss_cure],
       '变异怪':[byg_life,byg_att],
       '钢铁侠':[17500,gtx_att],
       '失败的man':[10000,99999],
       '张三':[1000,zs_att]}

s1 = 0
s2 = 0
s3 = 0
print('—————————————————HEROS LIST—————————————————')
t.sleep(s1)

print('''1、拳击手：
血量：10000
攻击：20000\n''')
t.sleep(s2)
print('''他每一次挥出的铁拳都是致命的！
唯一的短板在于血量有那么亿点点low。。。
尝试巧妙的搭配出场顺序
让他打出爆发伤害吧!\n\n''')
t.sleep(s3)

print('''2、铁巨人：
血量：20000
攻击：10000\n''')
t.sleep(s2)
print('''身躯为钢铁般坚硬，
铁巨人来也！
他是队友们最坚实的后盾，
也是你的英雄里最冤种的肉盾。\n\n''')
t.sleep(s3)

print('''3、黑骑士:
血量：15000
攻击：15000\n''')
t.sleep(s2)
print('''他是黑骑士，白骑士的死敌，
最最最万金油的角色，
顶均衡，
但是十分的万金油，两项都一般(￣_￣|||)\n\n''')
t.sleep(s3)

print('''4、飞镖侠：
血量：10000
攻击：N/A\n''')
t.sleep(s2)
print('''馊儿！一道寒光背后，便是你的死期。
随便摸出一把飞镖就打的飞镖侠！( ¯(∞)¯ )
从不按套路出牌，
攻击完全随机，难搞的一个对手\n\n''')
t.sleep(s3)

print('''5、大石头：
血量：100000
攻击：100\n''')
t.sleep(s2)
print('''。。。。。。
大石头！
。。。。。。
血量贼高，攻击贼低!\n\n''')
t.sleep(s3)

print('''6、魔法师：
血量：15000
攻击：10000
特长：治愈（100~1000）\n''')
t.sleep(s2)
print('''半吊子魔法师
血量攻击都不高，
但是会治愈魔咒，
这让他提升了一个LEVEL\n\n''')
t.sleep(s3)

print('''7、变异怪：
血量：(+_+)?
攻击：(+_+)?\n''')
t.sleep(s2)
print('''变变变！
变异怪登场！
不管攻击血量，
每局都不一样~~~\n\n''')
t.sleep(s3)


print('''8、钢铁侠：
血量：17500
攻击：10000 or 17500 or 22500\n''')
t.sleep(s2)
print('''托尼·斯塔克请求出战！
钢铁的战甲，
三种巨型炮弹，
足以让他（在安排合理的情况下）打出巨额伤害！\n\n''')
t.sleep(s3)


print('''9、失败的man：
血量：10000
攻击：99999\n''')
t.sleep(s2)
print('''能力越大，
食量越大！（doge）
虽然一击有90%杀，
但是输赢靠运气！\n\n''')
t.sleep(s3)


print('''10、张三：
血量：1000
攻击：(x_x)\n''')
t.sleep(s2)
print('''法外狂徒————张三，
小到乱扔垃圾，大到杀人放火，
什么事情也做得出来。
（本作者温馨提示：不想被罗老师判的话千万别和他学哦！）\n\n''')
t.sleep(s3)


print('我们有这些英雄:')
for intro in heros.keys():
   t.sleep(s1)
   print('\t'+intro)
   
e_heros=[]
e_len=0
while e_len<3:
   c_choi=r.choice(list(heros.keys()))
   if c_choi in e_heros:
      continue
   e_heros.append(c_choi)
   e_len=len(e_heros)
print('这是电脑的选择：'+'\t\n'+e_heros[0]+'\t\n'+e_heros[1]+'\t\n'+e_heros[2]+'\n')

p_heros=[]
h_len=len(p_heros)
while h_len<3:
   ans=input('请输入你的第{}个英雄：'.format(h_len+1))
   if ans in p_heros:
      print ('你已经有这个英雄了，请重新输入！') 
      continue
   elif ans not in heros.keys():
       print ('不好意思，我们还没有这个英雄。请重新输入！')
   elif ans in e_heros:
      print ('哎呀！敌人已经选这个英雄了，请重新输入！')
   else:  
      p_heros.append(ans)
      h_len=len(p_heros)
      continue

print ("你的英雄有："+"\t\n"+p_heros[0]+"\t\n"+p_heros[1]+"\t\n"+p_heros[2])


round_num=0
start = 1
while start:
   print ('——————————————————round{}——————————————————'.format(round_num+1))
   