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

    def special_attack(self, enemy):
        pass
 
    def special_defense(self, enemy):
        pass

    def is_dead(self):
        return self.HP <= 0

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
            현재 공격력: {}
            """.format(self.name, self.ATK)
        )
        damage = self.ATK - enemy.DEF

    def special_defense(self, enemy):
        print("Miss!")

class BLITZ(player): 
    def __init__(self, name):
        self.name = name
        self.HP = 7
        self.ATK = 3
        self.DEF = 3
        self.DEX = 3
        self.CRI = 3
        self.sa = 0
    
    def __str__(self):
        return "NAME: {}, JOB:BLITZ\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        print("""
            섬광 방패 : {}의 공격을 못하게 만든다
            """.format(enemy.name, enemy.ATK)
        )
        if luckypoint > 0 and luckypoint < 3:
            self.HP -= 1
        else:
            self.HP += 1
            

    def special_defense(self, enemy):
        enemy.ATK = enemy.sa
        enemy.ATK = 0
        print("섬광 방패: {}의 공격을 못하게한다".format(self.name, self.ATK))
        luckypoint = randint(0,10)
        if luckypoint > 0 and luckypoint < 3:
            self.HP -= 1
        else:
            self.HP += 1

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

    def special_defense_Warrior(self, enemy):
        self.DEF += 1
        print("""
            단단해지기! : {}의 방어력이 1만큼 상승합니다.
            현재 방어력: {}
            """.format(self.name, self.DEF)
        )
        damage = self.ATK - enemy.DEF
        self.HP -= damage

class sledge(player):
    def __init__(self, name):
        self.name = name
        self.HP = 10
        self.ATK = 4
        self.DEF = 2
        self.CRI = 5

    def __str__(self):
        return "NAME: {}, JOB:sledge\nHP: {}".format(self.name, self.HP)

    def special_attack(self, enemy):
        enemy.DEF -= 1
        print("""
            망치쓰기 : {}의 방어력이 1만큼 감소합니다.
            현재 방어력: {}
            """.format(enemy.name, enemy.DEF)
        )
        damage = self.ATK - enemy.DEF
        enemy.HP -= damage

class Fire magician(player):
    def __init__(self, enemy):
        self.name = name
        self.HP = 6
        self.MP = 5
        self.DEF = 5
        self.ATK = 5

    def __str__(self):
        return "Name: {}, JOB:sledge\nHP: {}".format(self.name, self.HP)

    def special_defense(self, enemy):
        self.MP += 1
        print("""
                마력 충전중....
                현재 마력: {} """.format(self.name, self.MP)
            )
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

p1 = Thief("윤수")
p2 = Warrior("동규")


coin = randint(1, 2)
if coin == 1:
    pass
else:
    (p1, p2) = (p2, p1)

print("게임을 시작합니다.")

for i in range(100):
    turn(p1, p2)