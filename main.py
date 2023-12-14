from character import Character

def main():
    player1 = Character('Krutoy')
    player2 = Character('Bob', damage=5)
    print(player1, end='\n\n')
    print(player2)
    print()

    while player1.is_alive() and player2.is_alive():
        p1_damage = player1.attack(player2)
        print(f'{player1.name} атакував '
              f'{player2.name} і наніс '
              f'{p1_damage} шкоди')
        if not player2.is_alive():
            break

        p2_damage = player2.attack(player1)
        print(f'{player2.name} відповів '
              f'{player1.name} і наніс '
              f'{p2_damage} шкоди')
        if not player1.is_alive():
            break

    print()
    print(player1, end='\n\n')
    print(player2)

if __name__ == "__main__":
    main()