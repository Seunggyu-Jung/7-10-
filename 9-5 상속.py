# 상속 -> 한 클라스의 멤버 변수를 이어 받을 수 있는 것을 의미
# 상속을 해주는 클래스 = 부모 클래스, 상속을 받는 클래스 = 자식 클래스
class unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class attackunit(unit): # 상속받을 클래스에 괄호를 치고 상속받을 클래스를 작성한다.
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)   # 상속받은 클래스.__init__(self, 상속 받을 멤버변수)
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






