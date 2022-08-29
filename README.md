# 클래스
# 1. 클래스 정의
- 클래스 : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계면(붕어빵 틀)
- object : 클래서에서 만들어 내는 피조물 
- 하나의 클래스를 통해서 서로 다른 다양한 값을 도출할 수 있는 것
- 클래스를 만들때, 맴버 변수 앞에 항상 self를 적는다
```
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
->
마린 유닛이 생성되었습니다.
체력 40, 공격력 5
마린 유닛이 생성되었습니다.
체력 40, 공격력 5
탱크 유닛이 생성되었습니다.
체력 150, 공격력 30
```

# 2. __init__함수 
- 생성자, 객체 변수와 동일한 수 만큼 넣어야한다.(self 제외)
```
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
->
마린 유닛이 생성되었습니다.
체력 40, 공격력 5
마린 유닛이 생성되었습니다.
체력 40, 공격력 5
탱크 유닛이 생성되었습니다.
체력 150, 공격력 30
```

# 3. 멤버 변수 
- 클래스 내에서 정의된 변수(name, hp, damage)

# 4. 메소드 함수
- 클래스 내의 모든 함수의 이름(attack, damaged)
```
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
->
파이어벳 유닛이 생성되었습니다.
체력 50, 공격력 20
파이어벳 유닛 : 5시방향으로 공격합니다.
파이어벳 : 25 데미지를 입었습니다.
파이어벳 : 현재 체력은 25 입니다.
파이어벳 : 25 데미지를 입었습니다.
파이어벳 : 현재 체력은 0 입니다.
파이어벳이 파괴되었습니다.
```

# 5. 상속
- 한 클라스의 멤버 변수를 이어 받을 수 있는 것을 의미
- 상속을 해주는 클래스 : 부모 클래스
- 상속을 받는 클래스 : 자식 클래스
- 상속받을 클래스에 괄호를 치고 상속할 클래스를 작성한다.
```
class unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class attackunit(unit): 
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)   
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
->
파이어벳 유닛이 생성되었습니다.
체력 50, 공격력 20
파이어벳 유닛 : 5시방향으로 공격합니다.
파이어벳 : 25 데미지를 입었습니다.
파이어벳 : 현재 체력은 25 입니다.
파이어벳 : 25 데미지를 입었습니다.
파이어벳 : 현재 체력은 0 입니다.
파이어벳이 파괴되었습니다.
```

# 6. 다중 상속
- 한 클래스가 여러 클래스에 상속되어 있는 것
- 상단에 from sys import flags 를 입력

```
from sys import flags


class unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class attackunit(unit): # 상속받을 클래스에 괄호를 치고 상속받을 클래스를 작성한다.
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)   # 상속받은 클래스.__init__(self, 상속 받을 멤버변수)
        self.damage = damage
       

    def attack(self, location):
        print("{0} 유닛 : {1}방향으로 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 파괴되었습니다.".format(self.name))

class flyable:
     def __init__(self, flying_speed):
        self.flying_speed = flying_speed

     def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, damage)
        flyable.__init__(self, flying_speed)

valkryie1 = flyableattackunit("발키리", 200, 6, 5)
valkryie1.fly(valkryie1.name, "3시")
->
발키리 : 3시방향으로 날아갑니다. [속도 : 5]
```

# 7. 메소드 오버라이딩
- 부모클래스의 멤버 변수가 아닌 자식클래스의 멤버 변수를 사용하고 싶을때 사용하는 방법
```
class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))


class attackunit(unit): 
    def __init__(self, name, hp, speed, damage):
        unit.__init__(self, name, hp, speed)   
        self.damage = damage
       

    def attack(self, location):
        print("{0} 유닛 : {1}방향으로 공격합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}이 파괴되었습니다.".format(self.name))

class flyable:
     def __init__(self, flying_speed):
        self.flying_speed = flying_speed

     def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

class flyableattackunit(attackunit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        attackunit.__init__(self, name, hp, 0, damage)  #지상 speed = 0
        flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = attackunit("벌처", 80, 10, 20)

battlecruiser = flyableattackunit("배틀크루저", 500, 25, 3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name ,"9시")
battlecruiser.move("9시")  # 자식 클래스의 함수를 통해 재정의
->
[지상 유닛 이동]
벌처 : 11시 방향으로 이동합니다. [속도 : 10]
[공중 유닛 이동]
배틀크루저 : 9시방향으로 날아갑니다. [속도 : 3]
```

# 8. pass
- 일단은 넘어간다는 것을 의미, 오류가 발생하지 않는다.
```
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
-> [알림] 새로운 게임을 시작합니다.
```

# 9. super
- 클래스를 보다 간단하게 상속받고자 할 때 사용
- super는 함수 옆에 ()와 변수에 self 를 쓰지 않는다는 것을 알아둬야함
```
class buildingunit(unit):
    def __init__(self, name, hp, location):
       #unit.__init__(self, name, hp, 0)
       super().__init__(name, hp, 0) 
       self.location = location
```

- 다중상속일 경우, super는 다중상속 중 맨 앞의 내용만을 가져온다.
```
class unit:
    def __init__(self):
        print("unit 생성자")

class flyable:
    def __init__(self) :
        print("flyable 생성자")

class flyableunit(unit,flyable):
    def __init__(self):
        super().__init__()

dropship = flyableunit()
-> unit 생성자
```



