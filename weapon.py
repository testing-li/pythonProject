class Weapon():
    def __init__(self, damage, bullet_count):
        self.damage = damage
        self.bullet_count = bullet_count

    def attack(self):
        self.bullet_count -= 1
        print('发射一个子弹，攻击力为' + str(self.damage))
