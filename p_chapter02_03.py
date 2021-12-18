# Chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car Class 
    Author : skh
    Date : 2021/11/21
    Description : Class, Static, Instance Method
    """
    
    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0
        
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
        
    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company,self._details.get('price'))
        
    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company,self._details.get('price') * Car.price_per_raise)
    
    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Secceed! price increased.')
        
    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry, This car is not bmw.'
            
        
# Self 의미
car1 = Car('Ferrari', {'color': 'White','horsepower': 400,'price': 8000})
car2 = Car('Bmw', {'color': 'White','horsepower': 400,'price': 5000})

car1.detail_info()
car2.detail_info()

# 가격정보(직접 접근)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격정보(클래스 메소드 미사용)
Car.price_per_raise = 1.4
# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 인스턴스로 호출(스테틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출(스테틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))


















