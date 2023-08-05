import json
import os
import vpython
game = {}
with open("jsons/13322787102478_hawkeye.json") as file:
    game = json.load(file)


'''
bouncePosition : 
    X : Length / meters
    Y : Line   / - 0 +
    Z : N/A

trajectory :
    releaseSpeed : mph

'''


bowlers = set([])
smallest = 99
largest = -1
large_deliv = {}
smallest_deliv = {}

for delivery in game:
    
    impact_position_x = delivery["match"]["delivery"]["trajectory"]["impactPosition"]["x"]
    impact_position_y = delivery["match"]["delivery"]["trajectory"]["impactPosition"]["y"]
    impact_position_z = delivery["match"]["delivery"]["trajectory"]["impactPosition"]["z"]
    impact_position = (impact_position_x, impact_position_y, impact_position_z)
    landing_position_x = delivery["match"]["delivery"]["trajectory"]["landingPosition"]["x"]
    landing_position_y = delivery["match"]["delivery"]["trajectory"]["landingPosition"]["y"]
    six_distance = delivery["match"]["delivery"]["trajectory"]["realDistance"]
    landing_position = (landing_position_x, landing_position_y)
    length = delivery["match"]["delivery"]["trajectory"]["bouncePosition"]["x"]
    ball = delivery["match"]["delivery"]["deliveryNumber"]["ball"]
    over = delivery["match"]["delivery"]["deliveryNumber"]["over"]
    inning = delivery["match"]["delivery"]["deliveryNumber"]["innings"]
    delivery_number = (over-1, ball, inning)
    score = delivery["match"]["delivery"]["scoringInformation"]["score"]
    release_position_z = delivery["match"]["delivery"]["trajectory"]["releasePosition"]["z"]
    shot_attacked = delivery["match"]["delivery"]["shotInformation"]["shotAttacked"]
    shot_played = delivery["match"]["delivery"]["shotInformation"]["shotPlayed"]
    batter = delivery["match"]["battingTeam"]["batsman"]["name"]
    
    bounce_position_x = delivery["match"]["delivery"]["trajectory"]["bouncePosition"]["x"]
    bounce_position_y = delivery["match"]["delivery"]["trajectory"]["bouncePosition"]["y"]

    # Create Bounce Position animation on a cricket pitch (20m x 3m), bounce position value in meters
    if (bounce_position_x != 0):
        vpython.rate(50) 
        vpython.scene = vpython.canvas(title="Bounce Position", width=800, height=800, center=vpython.vector(10, 1.5, 0), background=vpython.color.white)
        ball = vpython.sphere(pos=vpython.vector(bounce_position_x, bounce_position_y, 0), radius=0.1, color=vpython.color.red)
        pitch = vpython.box(pos=vpython.vector(10, 1.5, 0), size=vpython.vector(20, 3, 0.1), color=vpython.color.green)
        velocity = vpython.vector(1, 1, 0)
        dt = 0.01
        t = 0

        ball.pos = ball.pos + velocity*dt
        t+=dt

        


    
    # if (largest < release_position_z):
    #     largest = release_position_z
    #     large_deliv = delivery_number
    # if (smallest > release_position_z and release_position_z > -100):
    #     smallest = release_position_z
    #     smallest_deliv = delivery_number
    
    # if (score == 6):
    #     if (landing_position_x != 0):
    #         print(f"{landing_position} - {delivery_number} - {six_distance}")

# print(f"{smallest} : {largest}  -  {smallest_deliv} : {large_deliv}")
    
    # if ((score == 4) or (score == 6) or (score == -1)):
    #     print(score)
    #     print(impact_position)
    #     print(delivery_number)
    #     print("\n\n")
    


    # finding creasePosition meaning
    #score = delivery["match"]["delivery"]["scoringInformation"]["score"]
    # creaseY = delivery["match"]["delivery"]["trajectory"]["creasePosition"]["y"]
    # creaseZ = delivery["match"]["delivery"]["trajectory"]["creasePosition"]["z"]
    # if ((score == 4 or score == 6 or score == -1) and (creaseY < -0.2 or creaseY > 0.2)):
    #     print(delivery["match"]["delivery"]["deliveryNumber"]["ball"])
    #     print(delivery["match"]["delivery"]["deliveryNumber"]["over"])
    #     print(delivery["match"]["delivery"]["deliveryNumber"]["innings"])
    #     print(f'{creaseY} {creaseZ}')
    #     print("\n\n")

    # finding swing and deviation meaning
    # deviation = delivery["match"]["delivery"]["trajectory"]["deviation"]
    # drop_angle = delivery["match"]["delivery"]["trajectory"]["dropAngle"]
    # delivery_type = delivery["match"]["delivery"]["deliveryType"]
    # bounce_angle = delivery["match"]["delivery"]["trajectory"]["bounceAngle"]
    # swing = delivery["match"]["delivery"]["trajectory"]["swing"]
    # reaction_time_crease = delivery["match"]["delivery"]["trajectory"]["reactionTime(to crease)"]
    # reaction_time_interception = delivery["match"]["delivery"]["trajectory"]["reactionTime(to interception)"]
    # realDistance = delivery["match"]["delivery"]["trajectory"]["realDistance"]

    # if (realDistance != 0):
    #     print(realDistance)

