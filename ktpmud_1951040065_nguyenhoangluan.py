# -*- coding: utf-8 -*-
"""KTPMUD_1951040065_NguyenHoangLuan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o3lRrd9ag_gbavVc8Jrez-iA4tUHVm9j
"""

def check_prime_number(n):
    flag = True;
    if (n <2):
        flag = False
        return flag  
    
    for p in range(2, n):
        if n % p == 0:
            flag = False
            break
    return flag

def cau1a(arr):
    count = 0
    for i in arr:
        if check_prime_number(i):
            count = count + 1
    if count >= 2:
        return True
    return False

n = float(input("Moi nhap real_number: "))
m = float(input("Moi nhap image_number: "))
class Sothuc :
    def __init__(self,real_number) :
        self.real_number = real_number
    def gttd(self) :
        return (self.real_number *2) * 0.5

class Sophuc(Sothuc) :
    def __init__(self,real_number, image_number) :
        super().__init__(real_number)
        self.image_number = image_number
    def module(self) :
        return (self.image_number**2 + self.real_number**2) ** 0.5

sothuc = Sothuc(n)
print("Tri tuyet doi co gia tri la: ",sothuc.gttd())

sophuc = Sophuc(n,m)
print("module cua so phuc la: ",sophuc.module())

SELECT SUM(commission), city FROM salesman GROUP BY city;

select * from customer c
join salesman s on c.salesman_id = s.salesman_id
where s.commission > 0.12 
order by s.commission