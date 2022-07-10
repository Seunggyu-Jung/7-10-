# class -> 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계면(붕어빵 틀)
# object -> 클래서에서 만들어 내는 피조물 
# 하나의 클래스를 통해서 서로 다른 다양한 값을 도출할 수 있는 것이다.
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







