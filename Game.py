from tkinter import*
import random
from PIL import  ImageTk

def change_card_element():
    list = ["Fire", "Water", "Wood", "Metal"]
    effects = ['heal', 'poison', 'freezing', 'damage']
    damage_metal = [100, 115, 130, 145, 160]
    damage_water = [100, 115, 130, 145, 160]
    damage_fire = [100, 115, 130, 145, 160]
    damage_wood = [100, 115, 130, 145, 160]

    element_card = list[random.randint(0, 3)]
    return element_card

def change_card_damage():
    card_element = change_card_element()
    damage_metal = [100, 115, 130, 145, 160]
    damage_water = [100, 115, 130, 145, 160]
    damage_fire = [100, 115, 130, 145, 160]
    damage_wood = [100, 115, 130, 145, 160]

    if card_element == "Water":
        damage_card = str(damage_water[random.randint(0, 4)])
    if card_element == "Fire":
        damage_card = str(damage_fire[random.randint(0, 4)])
    if card_element == "Metal":
        damage_card = str(damage_metal[random.randint(0, 4)])
    if card_element == "Wood":
        damage_card = str(damage_wood[random.randint(0, 4)])
    return damage_card

def change_card_effect():
    effects = ['heal', 'poison', 'freezing','damage']
    effect_card = effects[random.randint(0,3)]
    return effect_card

def end_of_turn():
    global player_hp,cards,boss_damage,player1_card1,player1_card2,player1_card3,player1_card4,player_hp_label,boss_pick_up_card,Freezing_active

    if boss_pick_up_card == 1:
        player1_card1['state'] = 'active'
        boss_pick_up_card = 0
    if boss_pick_up_card == 2:
        player1_card2['state'] = 'active'
        boss_pick_up_card = 0
    if boss_pick_up_card == 3:
        player1_card3['state'] = 'active'
        boss_pick_up_card = 0
    if boss_pick_up_card == 4:
        player1_card4['state'] = 'active'
        boss_pick_up_card = 0

    lenght = len(cards)

    if lenght == 0:
        player_hp -= boss_damage

    if lenght == 1:
        if Freezing_active == 1:
            Freezing_active = 0
        else:
            player_hp -= boss_damage
        use_card = cards[0]
        if use_card == "player1_card3" or "player1_card4":
            effect_new_card = 'damage'
            element_new_card = change_card_element()
            damage_new_card = change_card_damage()
        else:
            damage_new_card = change_card_damage()
            effect_new_card = change_card_effect()
            element_new_card = change_card_element()
        if element_new_card == 'Fire':
            if effect_new_card == 'poison':
                add_image = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card == 'heal':
                add_image = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card == 'freezing':
                add_image = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card == 'Metal':
            if effect_new_card == 'poison':
                add_image = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card == 'heal':
                add_image = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card == 'freezing':
                add_image = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card == "Wood":
            if effect_new_card == 'poison':
                add_image = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card == 'heal':
                add_image = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card == 'freezing':
                add_image = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card == 'poison':
                add_image = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card == 'heal':
                add_image = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card == 'freezing':
                add_image = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if use_card == "player1_card1":
            player1_card1.configure(image=add_image)
            player1_card1['state'] = 'active'
        elif use_card == "player1_card2":
            player1_card2.configure(image=add_image)
            player1_card2['state'] = 'active'
        elif use_card == "player1_card3":
            player1_card3.configure(image=add_image)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image)
            player1_card4['state'] = 'active'

    elif lenght == 2:
        if Freezing_active == 1:
            Freezing_active  = 0
        else:
            player_hp -= boss_damage * 2
        use_card1 = cards[0]
        if use_card1 == "player1_card3" or "player1_card4":
            effect_new_card1 = 'damage'
            element_new_card1 = change_card_element()
            damage_new_card1 = change_card_damage()
        else:
            damage_new_card1 = change_card_damage()
            effect_new_card1 = change_card_effect()
            element_new_card1 = change_card_element()
        use_card2 = cards[1]
        if use_card2 == "player1_card3" or "player1_card4":
            effect_new_card2 = 'damage'
            element_new_card2 = change_card_element()
            damage_new_card2 = change_card_damage()
        else:
            damage_new_card2 = change_card_damage()
            effect_new_card2 = change_card_effect()
            element_new_card2 = change_card_element()
        if element_new_card1 == 'Fire':
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card1 == 'Metal':
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card1 == "Wood":
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if element_new_card2 == 'Fire':
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card2 == 'Metal':
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card2 == "Wood":
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if use_card1 == "player1_card1":
            player1_card1.configure(image=add_image1)
            player1_card1['state'] = 'active'
        elif use_card1 == "player1_card2":
            player1_card2.configure(image=add_image1)
            player1_card2['state'] = 'active'
        elif use_card1 == "player1_card3":
            player1_card3.configure(image=add_image1)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image1)
            player1_card4['state'] = 'active'

        if use_card2 == "player1_card1":
            player1_card1.configure(image=add_image2)
            player1_card1['state'] = 'active'
        elif use_card2 == "player1_card2":
            player1_card2.configure(image=add_image2)
            player1_card2['state'] = 'active'
        elif use_card2 == "player1_card3":
            player1_card3.configure(image=add_image2)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image2)
            player1_card4['state'] = 'active'
    elif lenght == 3:
        if Freezing_active == 1:
            Freezing_active = 0
        else:
             player_hp -= boss_damage * 3
        use_card1 = cards[0]
        if use_card1 == "player1_card3" or "player1_card4":
            effect_new_card1 = 'damage'
            element_new_card1 = change_card_element()
            damage_new_card1 = change_card_damage()
        else:
            damage_new_card1 = change_card_damage()
            effect_new_card1 = change_card_effect()
            element_new_card1 = change_card_element()
        use_card2 = cards[1]
        if use_card2 == "player1_card3" or "player1_card4":
            effect_new_card2 = 'damage'
            element_new_card2 = change_card_element()
            damage_new_card2 = change_card_damage()
        else:
            damage_new_card2 = change_card_damage()
            effect_new_card2 = change_card_effect()
            element_new_card2 = change_card_element()
        use_card3 = cards[2]
        if use_card3 == "player1_card3" or "player1_card4":
            effect_new_card3 = 'damage'
            element_new_card3 = change_card_element()
            damage_new_card3 = change_card_damage()
        else:
            damage_new_card3 = change_card_damage()
            effect_new_card3 = change_card_effect()
            element_new_card3 = change_card_element()
        if element_new_card1 == 'Fire':
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card1 == 'Metal':
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card1 == "Wood":
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if element_new_card2 == 'Fire':
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card2 == 'Metal':
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card2 == "Wood":
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if element_new_card3 == 'Fire':
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card3 == 'Metal':
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card3 == "Wood":
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if use_card1 == "player1_card1":
            player1_card1.configure(image=add_image1)
            player1_card1['state'] = 'active'
        elif use_card1 == "player1_card2":
            player1_card2.configure(image=add_image1)
            player1_card2['state'] = 'active'
        elif use_card1 == "player1_card3":
            player1_card3.configure(image=add_image1)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image1)
            player1_card4['state'] = 'active'
        if use_card2 == "player1_card1":
            player1_card1.configure(image=add_image2)
            player1_card1['state'] = 'active'
        elif use_card2 == "player1_card2":
            player1_card2.configure(image=add_image2)
            player1_card2['state'] = 'active'
        elif use_card2 == "player1_card3":
            player1_card3.configure(image=add_image2)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image2)
            player1_card4['state'] = 'active'
        if use_card3 == "player1_card1":
            player1_card1.configure(image=add_image3)
            player1_card1['state'] = 'active'
        elif use_card3 == "player1_card2":
            player1_card2.configure(image=add_image3)
            player1_card2['state'] = 'active'
        elif use_card3 == "player1_card3":
            player1_card3.configure(image=add_image3)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image3)
            player1_card4['state'] = 'active'
    elif lenght == 4:
        if Freezing_active == 1:
            Freezing_active = 0
        else:
            player_hp -= boss_damage * 4
        use_card1 = cards[0]
        if use_card1 == "player1_card3" or "player1_card4":
            effect_new_card1 = 'damage'
            element_new_card1 = change_card_element()
            damage_new_card1 = change_card_damage()
        else:
            damage_new_card1 = change_card_damage()
            effect_new_card1 = change_card_effect()
            element_new_card1 = change_card_element()
        use_card2 = cards[1]
        if use_card2 == "player1_card3" or "player1_card4":
            effect_new_card2 = 'damage'
            element_new_card2 = change_card_element()
            damage_new_card2 = change_card_damage()
        else:
            damage_new_card2 = change_card_damage()
            effect_new_card2 = change_card_effect()
            element_new_card2 = change_card_element()
        use_card3 = cards[2]
        if use_card3 == "player1_card3" or "player1_card4":
            effect_new_card3 = 'damage'
            element_new_card3 = change_card_element()
            damage_new_card3 = change_card_damage()
        else:
            damage_new_card3 = change_card_damage()
            effect_new_card3 = change_card_effect()
            element_new_card3 = change_card_element()
        use_card4 = cards[3]
        if use_card4 == "player1_card3" or "player1_card4":
            effect_new_card4 = 'damage'
            element_new_card4 = change_card_element()
            damage_new_card4 = change_card_damage()
        else:
            damage_new_card4 = change_card_damage()
            effect_new_card4 = change_card_effect()
            element_new_card4 = change_card_element()
        if element_new_card1 == 'Fire':
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card1 == 'Metal':
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card1 == "Wood":
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card1 == 'poison':
                add_image1 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card1 == 'heal':
                add_image1 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card1 == 'freezing':
                add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image1 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if element_new_card2 == 'Fire':
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card2 == 'Metal':
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card2 == "Wood":
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card2 == 'poison':
                add_image2 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card2 == 'heal':
                add_image2 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card2 == 'freezing':
                add_image2 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image2 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if element_new_card3 == 'Fire':
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card3 == 'Metal':
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card3 == "Wood":
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card3 == 'poison':
                add_image3 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card3 == 'heal':
                add_image3 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card3 == 'freezing':
                add_image3 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image3 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if element_new_card4 == 'Fire':
            if effect_new_card4 == 'poison':
                add_image4 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
            elif effect_new_card4 == 'heal':
                add_image4 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
            elif effect_new_card4 == 'freezing':
                add_image4 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
            else:
                add_image4 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
        elif element_new_card4 == 'Metal':
            if effect_new_card4 == 'poison':
                add_image4 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
            elif effect_new_card4 == 'heal':
                add_image4 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
            elif effect_new_card4 == 'freezing':
                add_image4 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
            else:
                add_image4 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
        elif element_new_card4 == "Wood":
            if effect_new_card4 == 'poison':
                add_image4 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
            elif effect_new_card4 == 'heal':
                add_image4 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
            elif effect_new_card4 == 'freezing':
                add_image4 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
            else:
                add_image4 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
        else:
            if effect_new_card4 == 'poison':
                add_image4 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
            elif effect_new_card4 == 'heal':
                add_image4 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
            elif effect_new_card4 == 'freezing':
                add_image4 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
            else:
                add_image4 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
        if use_card1 == "player1_card1":
            player1_card1.configure(image=add_image1)
            player1_card1['state'] = 'active'
        elif use_card1 == "player1_card2":
            player1_card2.configure(image=add_image1)
            player1_card2['state'] = 'active'
        elif use_card1 == "player1_card3":
            player1_card3.configure(image=add_image1)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image1)
            player1_card4['state'] = 'active'
        if use_card2 == "player1_card1":
            player1_card1.configure(image=add_image2)
            player1_card1['state'] = 'active'
        elif use_card2 == "player1_card2":
            player1_card2.configure(image=add_image2)
            player1_card2['state'] = 'active'
        elif use_card2 == "player1_card3":
            player1_card3.configure(image=add_image2)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image2)
            player1_card4['state'] = 'active'
        if use_card3 == "player1_card1":
            player1_card1.configure(image=add_image3)
            player1_card1['state'] = 'active'
        elif use_card3 == "player1_card2":
            player1_card2.configure(image=add_image3)
            player1_card2['state'] = 'active'
        elif use_card3 == "player1_card3":
            player1_card3.configure(image=add_image3)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image3)
            player1_card4['state'] = 'active'
        if use_card4 == "player1_card1":
            player1_card1.configure(image=add_image3)
            player1_card1['state'] = 'active'
        elif use_card4 == "player1_card2":
            player1_card2.configure(image=add_image3)
            player1_card2['state'] = 'active'
        elif use_card4 == "player1_card3":
            player1_card3.configure(image=add_image3)
            player1_card3['state'] = 'active'
        else:
            player1_card4.configure(image=add_image3)
            player1_card4['state'] = 'active'

    pick_up_card = random.randint(1, 10)
    if pick_up_card <= 5:
        pick_up_card = random.randint(1, 4)
        if pick_up_card == 1:
            player1_card1['state'] = 'disabled'
            boss_pick_up_card = 1
        elif pick_up_card == 2:
            player1_card2['state'] = 'disabled'
            boss_pick_up_card = 2
        elif pick_up_card == 3:
            player1_card3['state'] = 'disabled'
            boss_pick_up_card = 3
        elif pick_up_card == 4:
            player1_card4['state'] = 'disabled'
            boss_pick_up_card = 4
    if player_hp <=0:
        window.destroy()
    elif Boss_hp <=0:
        window.destroy()
    else:
        player_hp_label.configure(text=str(player_hp))
        cards = []
        player1_card1.mainloop()
    if effect_card1 == 'heal' and player_hp >= 900:
        player1_card1['state'] = 'disabled'
    if effect_card2 == 'heal' and player_hp >= 900:
        player1_card2['state'] = 'disabled'

def player1_card1():
    global Boss_hp, effect_card1, player_hp,damage_card1,Boss_stihia,element_card1,boss,player1_card1,cards,player_hp_label,Freezing_active
    if effect_card1 == 'poison':
        Boss_hp-=25
        Poison_active = 1
        if Boss_stihia == element_card1:
            Boss_hp -= int(damage_card1)/2
        else:
            Boss_hp -= int(damage_card1)
    if effect_card1 == 'freezing':
        Boss_move = 1
        Freezing_active = 1
        if Boss_stihia == element_card1:
            Boss_hp -= int(damage_card1) / 2
        else:
            Boss_hp -= int(damage_card1)
    if effect_card1 == 'heal':
        if Boss_stihia == element_card1:
            Boss_hp -= int(damage_card1) / 2
        else:
            Boss_hp -= int(damage_card1)
        player_hp+=100
    boss.configure(text='Boss hp='+ str(Boss_hp)+' '+'Boss immunity='+str(Boss_stihia))
    player_hp_label.configure(text = player_hp)
    player1_card1['state'] = 'disabled'
    cards.append('player1_card1')
    if player_hp <=0:
        window.destroy()
    elif Boss_hp <=0:
        window.destroy()
    if effect_card1 == 'heal' and player_hp >= 900:
        player1_card1['state'] = 'disabled'
def player1_card2():
    global Boss_hp, effect_card2, player_hp, damage_card2,Boss_stihia,element_card2,player1_card2,cards,player_hp_label,Freezing_active
    if effect_card2 == 'poison':
        Boss_hp-=25
        if Boss_stihia == element_card2:
            Boss_hp -= int(damage_card2) / 2
        else:
            Boss_hp -= int(damage_card2)
    if effect_card2 == 'freezing':
        Boss_move = 1
        Freezing_active = 1
        if Boss_stihia == element_card2:
            Boss_hp -= int(damage_card2) / 2
        else:
            Boss_hp -= int(damage_card2)
    if effect_card2 == 'heal':
        if Boss_stihia == element_card2:
            Boss_hp -= int(damage_card2) / 2
        else:
            Boss_hp -= int(damage_card2)
        player_hp+=100
    boss.configure(text='Boss hp='+ str(Boss_hp)+' '+'Boss immunity='+str(Boss_stihia))
    player_hp_label.configure(text=player_hp)
    player1_card2['state'] = 'disabled'
    cards.append('player1_card2')
    if player_hp <=0:
        window.destroy()
    elif Boss_hp <=0:
        window.destroy()
    if effect_card2 == 'heal' and player_hp >= 900:
        player1_card2['state'] = 'disabled'
def player1_card3():
    global Boss_hp,damage_card3,Boss_stihia,element_card3,player1_card3
    if Boss_stihia == element_card3:
        Boss_hp -= int(damage_card3) / 2
    else:
        Boss_hp -= int(damage_card3)
    boss.configure(text='Boss hp='+ str(Boss_hp)+' '+'Boss immunity='+str(Boss_stihia))
    player1_card3['state'] = 'disabled'
    cards.append('player1_card3')
    if player_hp <=0:
        window.destroy()
    elif Boss_hp <=0:
        window.destroy()
def player1_card4():
    global Boss_hp, damage_card4, Boss_stihia, element_card4,player1_card4
    if Boss_stihia == element_card4:
        Boss_hp -= int(damage_card4) / 2
    else:
        Boss_hp -= int(damage_card4)
    boss.configure(text='Boss hp='+ str(Boss_hp)+' '+'Boss immunity='+str(Boss_stihia))
    player1_card4['state'] = 'disabled'
    cards.append('player1_card4')
    if player_hp <=0:
        window.destroy()
    elif Boss_hp <=0:
        window.destroy()
class Boss():
    hp = 5000
    list = ["Fire","Water","Wood","Metal"]
    damage = random.randint(30,100)
    a = list[random.randint (0,3)]

class Player():
    hp = 1000
    mp = 10

class Cards():
    def generation_element_start(self):
        list = ["Fire", "Water", "Wood", "Metal"]
        effects = ['heal', 'poison', 'freezing']
        damage_metal = [100, 115, 130, 145, 160]
        damage_water = [100, 115, 130, 145, 160]
        damage_fire = [100, 115, 130, 145, 160]
        damage_wood = [100, 115, 130, 145, 160]

        a1 = list[random.randint(0,3)]
        if a1 == "Water":
            damage = str(damage_water[random.randint(0,4)])
        if a1 == "Fire":
            damage = str(damage_fire[random.randint(0,4)])
        if a1 == "Metal":
            damage = str(damage_metal[random.randint(0,4)])
        if a1 == "Wood":
            damage = str(damage_wood[random.randint(0,4)])
        a = [[effects[random.randint(0,2)]],[a1],[damage]]

        b1 = list[random.randint(0, 3)]
        if b1 == "Water":
            damage = str(damage_water[random.randint(0, 4)])
        if b1 == "Fire":
            damage = str(damage_fire[random.randint(0, 4)])
        if b1 == "Metal":
            damage = str(damage_metal[random.randint(0, 4)])
        if b1 == "Wood":
            damage = str(damage_wood[random.randint(0, 4)])
        b = [[effects[random.randint(0, 2)]], [b1], [damage]]

        c1 = list[random.randint(0, 3)]
        if c1 == "Water":
            damage = str(damage_water[random.randint(0, 4)])
        if c1 == "Fire":
            damage = str(damage_fire[random.randint(0, 4)])
        if c1 == "Metal":
            damage = str(damage_metal[random.randint(0, 4)])
        if c1 == "Wood":
            damage = str(damage_wood[random.randint(0, 4)])
        c = [['damage'], [c1], [damage]]

        d1 = list[random.randint(0, 3)]
        if d1 == "Water":
            damage = str(damage_water[random.randint(0, 4)])
        if d1 == "Fire":
            damage = str(damage_fire[random.randint(0, 4)])
        if d1 == "Metal":
            damage = str(damage_metal[random.randint(0, 4)])
        if d1 == "Wood":
            damage = str(damage_wood[random.randint(0, 4)])
        d = [['damage'], [d1], [damage]]
        return a,b,c,d



window=Tk()
window.geometry('1224x800')
window.resizable(0,0)
window.title('Card Game')
fight=Canvas(window,width=1300,height=800)
fight.grid()

img2=ImageTk.PhotoImage(file="graphics\Fon.png")
fight.create_image(0,0, image=img2,anchor='nw')

boss_oblect=Boss()
Boss_hp=boss_oblect.hp
Boss_stihia=boss_oblect.a
boss_damage=boss_oblect.damage
e=ImageTk.PhotoImage(file="graphics\Boss.jpg")
boss=Label(window,text='Boss hp='+ str(Boss_hp)+' '+'Boss immunity='+str(Boss_stihia),font="Arial 30")
fight.create_window(650,50,window=boss)
bossimg=Label(window, image=e)
fight.create_window(650,250,window=bossimg)

player = Player()
player_hp = int(player.hp)
player_hp_label = Label(window,text =player_hp,font="Arial 20")
fight.create_window(1120,50,window=player_hp_label)
hp_label = Label(window,text ='Hp=',font="Arial 20")
fight.create_window(1050,50,window=hp_label)

global cards
cards = []

end_of_turn=Button(window,text='Конец хода',font="Arial 30",fg='White', bg='red',command = end_of_turn)
fight.create_window(130,60,window=end_of_turn)


carts_object=Cards()
ttt=carts_object.generation_element_start()

card1=ttt[0]
card2=ttt[1]
card3=ttt[2]
card4=ttt[3]

damage_card1 = card1[2]
effect_card1 = card1[0]
element_card1 = card1[1]

damage_card2 = card2[2]
effect_card2 = card2[0]
element_card2 = card2[1]

damage_card3 = card3[2]
effect_card3 = card3[0]
element_card3 = card3[1]

damage_card4 = card4[2]
effect_card4 = card4[0]
element_card4 = card4[1]

damage_card1 = str(damage_card1)
damage_card1 = damage_card1[0:-2]
damage_card1 = damage_card1[::-1]
damage_card1 = damage_card1[0:-2]
damage_card1 = damage_card1[::-1]


effect_card1 = str(effect_card1)
effect_card1 = effect_card1[0:-2]
effect_card1 = effect_card1[::-1]
effect_card1 = effect_card1[0:-2]
effect_card1 = effect_card1[::-1]

element_card1 = str(element_card1)
element_card1 = element_card1[0:-2]
element_card1 = element_card1[::-1]
element_card1 = element_card1[0:-2]
element_card1 = element_card1[::-1]
if element_card1 == 'Fire':
    if effect_card1 == 'poison':
        add_image = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
    elif effect_card1 == 'heal':
        add_image = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
    elif effect_card1 == 'freezing':
        add_image = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
    else:
        add_image = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
elif element_card1 == 'Metal':
    if effect_card1 == 'poison':
        add_image = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
    elif effect_card1 == 'heal':
        add_image = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
    elif effect_card1 == 'freezing':
        add_image = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
    else:
        add_image = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
elif element_card1 == "Wood":
    if effect_card1 == 'poison':
        add_image = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
    elif effect_card1 == 'heal':
        add_image = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
    elif effect_card1 == 'freezing':
        add_image = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
    else:
        add_image = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
else:
    if effect_card1 == 'poison':
        add_image = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
    elif effect_card1 == 'heal':
        add_image = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
    elif effect_card1 == 'freezing':
        add_image = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
    else:
        add_image = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
player1_card1=Button(window, image=add_image, bg="white", bd=0, command=player1_card1)
fight.create_window(180,600,window=player1_card1)

damage_card1_label = Label(window, bg="white", bd=0, text = str(damage_card1), font='Arial 20')
fight.create_window(175,735,window=damage_card1_label)

if effect_card1 == 'heal' and player_hp >= 900:
    player1_card1['state'] = 'disabled'

damage_card2 = str(damage_card2)
damage_card2 = damage_card2[0:-2]
damage_card2 = damage_card2[::-1]
damage_card2 = damage_card2[0:-2]
damage_card2 = damage_card2[::-1]

effect_card2 = str(effect_card2)
effect_card2= effect_card2[0:-2]
effect_card2 = effect_card2[::-1]
effect_card2 = effect_card2[0:-2]
effect_card2 = effect_card2[::-1]

element_card2 = str(element_card2)
element_card2 = element_card2[0:-2]
element_card2 = element_card2[::-1]
element_card2 = element_card2[0:-2]
element_card2 = element_card2[::-1]

if element_card2 == 'Fire':
    if effect_card2 == 'poison':
        add_image1 = ImageTk.PhotoImage(file="graphics\poison_fire.jpg")
    elif effect_card2 == 'heal':
        add_image1 = ImageTk.PhotoImage(file="graphics\heal_fire.jpg")
    elif effect_card2 == 'freezing':
        add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_fire.jpg")
    else:
        add_image1 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
elif element_card2 == 'Metal':
    if effect_card2 == 'poison':
        add_image1 = ImageTk.PhotoImage(file="graphics\poison_metal.jpg")
    elif effect_card2 == 'heal':
        add_image1 = ImageTk.PhotoImage(file="graphics\heal_metal.jpg")
    elif effect_card2 == 'freezing':
        add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_metal.jpg")
    else:
        add_image1 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
elif element_card2 == "Wood":
    if effect_card2 == 'poison':
        add_image1 = ImageTk.PhotoImage(file="graphics\poison_wood.jpg")
    elif effect_card2 == 'heal':
        add_image1 = ImageTk.PhotoImage(file="graphics\heal_wood.jpg")
    elif effect_card2 == 'freezing':
        add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_wood.jpg")
    else:
        add_image1 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
else:
    if effect_card2 == 'poison':
        add_image1 = ImageTk.PhotoImage(file="graphics\poison_water.jpg")
    elif effect_card2 == 'heal':
        add_image1 = ImageTk.PhotoImage(file="graphics\heal_water.jpg")
    elif effect_card2 == 'freezing':
        add_image1 = ImageTk.PhotoImage(file="graphics\ifreezing_water.jpg")
    else:
        add_image1 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
player1_card2=Button(window, image=add_image1, bg="white", bd=0, command=player1_card2)
fight.create_window(480,600,window=player1_card2)

damage_card2_label = Label(window, bg="white", bd=0, text = str(damage_card2), font='Arial 20')
fight.create_window(470,735,window=damage_card2_label)

if effect_card2 == 'heal' and player_hp >= 900:
    player1_card2['state'] = 'disabled'

damage_card3 = str(damage_card3)
damage_card3 = damage_card3[0:-2]
damage_card3 = damage_card3[::-1]
damage_card3 = damage_card3[0:-2]
damage_card3 = damage_card3[::-1]

effect_card3 = str(effect_card3)
effect_card3 = effect_card3[0:-2]
effect_card3 = effect_card3[::-1]
effect_card3 = effect_card3[0:-2]
effect_card3 = effect_card3[::-1]

element_card3 = str(element_card3)
element_card3 = element_card3[0:-2]
element_card3 = element_card3[::-1]
element_card3 = element_card3[0:-2]
element_card3 = element_card3[::-1]

if element_card3 == 'Fire':
        add_image2 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
elif element_card3 == 'Metal':
        add_image2 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
elif element_card3 == "Wood":
        add_image2 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
else:
     add_image2 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
player1_card3=Button(window, image=add_image2, bg="white", bd=0, command=player1_card3)
fight.create_window(780,600,window=player1_card3)

damage_card3_label = Label(window, bg="white", bd=0, text = str(damage_card3), font='Arial 20')
fight.create_window(770,735,window=damage_card3_label)

damage_card4 = str(damage_card4)
damage_card4 = damage_card4[0:-2]
damage_card4 = damage_card4[::-1]
damage_card4 = damage_card4[0:-2]
damage_card4 = damage_card4[::-1]

effect_card4 = str(effect_card4)
effect_card4 = effect_card4[0:-2]
effect_card4 = effect_card4[::-1]
effect_card4 = effect_card4[0:-2]
effect_card4 = effect_card4[::-1]

element_card4 = str(element_card4)
element_card4 = element_card4[0:-2]
element_card4 = element_card4[::-1]
element_card4 = element_card4[0:-2]
element_card4 = element_card4[::-1]

if element_card4 == 'Fire':
        add_image3 = ImageTk.PhotoImage(file="graphics\damage_fire.jpg")
elif element_card4 == 'Metal':
        add_image3 = ImageTk.PhotoImage(file="graphics\damage_metal.jpg")
elif element_card4 == "Wood":
        add_image3 = ImageTk.PhotoImage(file="graphics\damage_wood.jpg")
else:
     add_image3 = ImageTk.PhotoImage(file="graphics\damage_water.jpg")
player1_card4=Button(window, image=add_image3, bg="white", bd=0, command=player1_card4)
fight.create_window(1080,600,window=player1_card4)

damage_card4_label = Label(window, bg="white", bd=0, text = str(damage_card3), font='Arial 20')
fight.create_window(1080,735,window=damage_card4_label)

boss_pick_up_card = 0
Freezing_active = 0

player1_card1.mainloop()
player1_card2.mainloop()
window.mainloop()