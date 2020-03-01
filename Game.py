# Game
# AUthor : Kimyunsoo
# Version : 0.1.0

from random import randint
from enum import Enum
from time import sleep
from sys import exit
luckypoint = 0

class player:
    def __init__(self, name, job):   
        self.HP = 0
        self.name = name
              
    def __str__(self):
        pass

    def attack(self, enemy):
        print("{}이 {}를 공격!".format(self.name, enemy.name))
        chance = randint(1, 10)
        if chance <= self.CRI:
            print("특수 공격 발동!")
            self.special_attack(enemy)
        else:
            chance2 = randint(1, 10)
            if chance2 <= enemy.DEX:
                print("특수 방어 발동!")
                enemy.special_defense(self)
            else:
                damage = self.ATK - enemy.DEF
                enemy.HP -= damage
        if self.HP < 0:
            self.HP = 0
        else:
            self.HP = self.HP
        if enemy.HP < 0:
            enemy.HP = 0
        else:
            enemy.HP = enemy.HP

    def special_attack(self, enemy):
        pass
 
    def special_defense(self, enemy):
        pass

    def is_dead(self):
        return self.HP <= 0

######################################################################
Thief
######################################################################
class Thief(player):
    def __init__(self, name):
        self.name = name
        self.HP = 5
        self.ATK = 3
        self.DEF = 1
        self.DEX = 8
        self.CRI = 3
        self.sa = 0
    
    def __str__(self):
        return "NAME: {}, JOB:Thief\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        self.ATK += 1
        enemy.ATK -= 1
        print("""
            공격력을 뺏았는다! : {}의 공격력을 1만큼 갈취해서 자신의 공격력에 더합니다.
            현재 공격력: {}, 상대의 공격력: {}
            """.format(self.name, self.ATK, enemy.ATK)
        )
        damage = self.ATK - enemy.DEF

    def special_defense(self, enemy):
        print("Miss!")
######################################################################
BLITZ
######################################################################
class BLITZ(player): 
    def __init__(self, name):
        self.name = name
        self.HP = 7
        self.ATK = 3
        self.DEF = 3
        self.DEX = 3
        self.CRI = 3
            
    def __str__(self):
        return "NAME: {}, JOB:BLITZ\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        print("""
            섬광 방패 : {}의 공격을 못하게 만든다
            """.format(enemy.name)
        )
        luckypoint = randint(1,10)
        if luckypoint > 0 and luckypoint < 3:
            self.HP -= 1
        else:
            self.HP += 1
        
    def special_defense(self, enemy):
        enemy.ATK = 0
        print("섬광 방패: {}의 공격을 못하게한다".format(self.name, self.ATK))
        luckypoint = randint(0,10)
        if luckypoint > 0 and luckypoint < 3:
            self.HP -= 1
        else:
            self.HP += 1
######################################################################
Warrior
######################################################################        
class Warrior(player):
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 4
        self.DEF = 2
        self.DEX = 5
        self.CRI = 3

    def __str__(self):
        return "NAME: {}, JOB:Warrior\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        enemy.DEF -= 1
        print("""
            물렁해지기! : {}의 방어력이 1만큼 감소합니다.
            현재 방어력: {}
            """.format(enemy.name, enemy.DEF)
        )
        damage = self.ATK - enemy.DEF
        enemy.HP -= damage
        if self.DEF < 0:
            self.DEF = 0
        else:
            self.DEF = self.DEF

    def special_defense(self, enemy):
        self.DEF += 1
        print("""
            단단해지기! : {}의 방어력이 1만큼 상승합니다.
            현재 방어력: {}
            """.format(self.name, self.DEF)
        )
        damage = self.ATK - enemy.DEF
        self.HP -= damage
######################################################################
Sledge
######################################################################
class sledge(player):

    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 4
        self.DEF = 2
        self.CRI = 5
        self.DEX = 5

    def __str__(self):
        return "NAME: {}, JOB:sledge\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        print("무쇠망치")
        damage = 1
        enemy.HP -= damage

    def special_defense(self, enemy):
        print("36계 줄행량")
######################################################################
Firemagician
######################################################################
class Firemagician(player):

    def __init__(self, name):
        self.name = name
        self.HP = 6
        self.MP = 5
        self.DEF = 2
        self.CRI = 5
        self.DEX = 5
        self.ATK = 3
        self.sk1 = 6
        self.SK2 = 9
        self.SK3 = 10

    def __str__(self):
        return "Name: {}, JOB:Firemagician\nHP: {}".format(self.name, self.HP)

    def special_defense(self, enemy):
        self.MP += abs(self.DEF - enemy.ATK)
        print("""
                마력 충전중....
                현재 마력: {} """.format(self.MP)
            )
    
    def special_attack(self, enemy):
        N = randint(1,10)
        if N < self.sk1:
            if self.MP >= 1:
                print("파이어볼")
                damage = 2
                enemy.HP -= damage
                self.MP -= 1
            else:
                print("마력이 없다....")
        elif self.sk1 < N < self.SK2:
            if self.MP >= 2:
                print("메테오!")
                damage = 3
                enemy.HP -= damage
                self.MP -= 2
            else:
                print("메테오를 날렸지만 약해 데미지가 없었다...")
        elif self.SK2 < N < self.SK3:
            if self.MP >= 5:
                print("폭발은 예술이다!")
                damage = 10
                enemy.HP -= damage
                self.MP -= 5
            else: 
                print("힘이..없다...")
######################################################################
Berserker
######################################################################
class Berserker(player):
    def __init__(self, name):
        self.name = name
        self.HP = 8
        self.ATK = 5
        self.DEF = 4
        self.CRI = 3
        self.DEX = 3
    
    def __str__(self):
        return "Name: {}, JOB:berserker\nHP: {}".format(self.name, self.HP)
    
    def special_attack(self, enemy):
        self.ATK += 1
        print("""
            버서커의 분노: {}의 공격력이 1만큼 증가합니다.
            현재 공격력: {}
            """.format(self.name, self.ATK)
        )    
    def special_defense(self,enemy):
        print("""
            복수: 일정 HP이하일시 공격력의 두배로 공격 합니다.
            """
        )
        if self.HP < 3:
            self.ATK *= 2
            self.HP += 1
        else:
            self.ATK = self.ATK
######################################################################
Healer
######################################################################
class Healer(player):
    def __init__(self, name):
        self.name = name
        self.ATK = 2
        self.DEF = 4
        self.CRI =4
        self.DEX =5
        self.HP = 7

    def __str__(self):
        return "Name: {}, JOB:Healer\nHP: {}".format(self.name, self.HP)
    
    def special_attack(self, enemy):
        print("그런거 없어요!")
        damage = 1
        enemy.HP -= damage
    
    def special_defense(self, enemy):
        print("영웅은 죽지 않아요!")
        self.HP += 3
######################################################################
Tanker
######################################################################
class Tanker(player):

    def __init__(self, name):
        self.name = name
        self.HP = 15
        self.ATK = 2
        self.DEF = 5
        self.DEX = 3
        self.CRI = 3

    def __str__(self):
        return "Name: {}, JOB:Tanker\nHP:{}".format(self.name, self.HP)
    
    def special_attack(self, enemy):
        enemy.DEF -= 2
        print("""
            돌진!!
            상대방에게 돌진하여 방어력을 2만큼 낮춤니다.
            현재 방어력: {}
            """.format(enemy.DEF)
            )
    
    def special_defense(self, enemy):
        self.DEF += 2
        print("자신의 방어력을 2만큼 올립니다")

    def turn(p1, p2):
    print("=========================================")
    print("{}의 차례".format(p1.name))
    sleep(1)
    p1.attack(p2)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
####################################################################
    if p2.is_dead():
        print("{}는 사망하셨습니다.".format(p2.name))
        print("{}의 승리!".format(p1.name))
        exit(1)
#####################################################################
    sleep(2)
    print("===================================================")
    print("{}의 차례".format(p2.name))
    sleep(1)
    p2.attack(p1)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    ######################################################
    if p1.is_dead():
        print("{}는 사망하셨습니다.".format(p1.name))
        print("{}의 승리!".format(p2.name))
        exit(1)
    print("======================================================")
    sleep(2)

p1 = Firemagician("A")
p2 = sledge("B")


coin = randint(1, 2)
if coin == 1:
    pass
else:
    (p1, p2) = (p2, p1)

print("게임을 시작합니다.")

for i in range(100):
    turn(p1, p2)
    if i < 15:
        pass
    else:
        self.HP -= 1
        enemy.HP -= 1