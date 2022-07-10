# 멤버 변수 -> 클래스 내에서 정의된 변수(name, hp, damage)


class unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#marin1 = unit("마린", 40 , 5)
#marin2 = unit("마린", 40 , 5)
#tank = unit("탱크", 150, 30)

wraith1 = unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력: {1}".format(wraith1.name,wraith1.damage))  # 변수의 .을 붙임으로써 멤버 변수를 끌어 올 수 있다.

wraith2 = unit("NTR 레이스", 80, 5)

wraith2.clocking = True         # 클래스 외부에서 멤버변수(.clocking)를 확장 할 수 있으며, 확장된 변수는 확장 시킨 객체에서만 적용된다. 기존의 변수에는 적용되지 않는다.
if wraith2.clocking == True:
    print("{0}은 클로킹 상태 입니다.".format(wraith2.name))

