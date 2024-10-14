import random
tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagit = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
secim=[tas,kagit,makas]

win=0
lose=0
while True:
    pc = random.randint(0, 2)
    kullanıcı = int(input("0-Taş 1-Kağıt 2-Makas'den birini seçiniz: "))
    print(f"Siz: {secim[kullanıcı]}")
    print(f"Bilgisayar: {secim[pc]}")

    if kullanıcı == 0 and pc == 2:
        print("Kazandınız")
        win+=1
        print(f"{win}-{lose}")
    elif pc == 0 and kullanıcı == 2:
        print("Kaybettiniz")
        lose+=1
        print(f"{win}-{lose}")
    elif kullanıcı < pc:
        print("Kaybettiniz")
        lose+=1
        print(f"{win}-{lose}")
    elif pc < kullanıcı:
        print("kazandınız")
        win+=1
        print(f"{win}-{lose}")
    else:
        print("Berabere")
        print(f"{win}-{lose}")
        pass

    if win==3:
        print("KAZANDINIZ!!!")
        exit()
    if lose==3:
        print("KAYBETTİNİZ:(:(:(")
        exit()
