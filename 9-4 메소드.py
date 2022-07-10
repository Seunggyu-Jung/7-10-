# 메소드 함수 = 클래스 내의 모든 함수의 이름(attack, damaged)

class attackunit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} 유닛 : {1}방향으로 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 파괴되었습니다.".format(self.name))

firebat1 = attackunit("파이어벳", 50, 20)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)