import random

print(""" A Lv.100 Richu (Electric/Land, Sp Atk: 350) attacks a Lv. 100 Squirtle(Water, Sp. Def: 200
with the shock wave, a Electric Type move eith a power of 100 and against same-type attack bonus.. it hits
the target normall bit deals a super effective damage. The weather on the field is noraml. Given the following
condirions, detemine how much damage richu attack will deal. """)

target = 1
weather = 1
badge = 1
crit = random.randint(1,2)
random1 = round(random.uniform(0.85, 1.00),2)
stab = 1
type = round(random.uniform(0.85,1.00),2)
opt = random.randint(0,1)
other = 1

modifier = target * weather * badge * crit * random1 * stab * type * other
damage = round(((((2*100)/5+2)* 100 *(350/200))/50)+2,2)
tdamage = round((damage * modifier),2)

print("Modifiers: ")

print("Target: ",target)
print("Weather: ",weather)
print("Badge: ",badge)
print("Crit: ",crit)
print("Random: ",random)
print("Stab: ",stab)
print("Type: ",type)
print("other: ",other)

print("Damage: ",damage)
print("Modifier: ",modifier)
print("Total Damage: ",tdamage)