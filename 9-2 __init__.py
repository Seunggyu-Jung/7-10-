#__init__함수 : 생성자, 객체 변수와 동일한 수 만큼 넣어야한다.(self 제외)


class unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marin1 = unit("마린", 40 , 5)
marin2 = unit("마린", 40 , 5)
tank = unit("탱크", 150, 30)
