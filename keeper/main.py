#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Stop

# Define ports
ev3 = EV3Brick()
m_motor = Motor(Port.A)
l_motor = Motor(Port.B)
r_motor = Motor(Port.C)
c_sensor = ColorSensor(Port.S3)
u_sensor = UltrasonicSensor(Port.S4)
scan_range = 325

# Jos auto ei aja tarpeeksi pitkälle, nosta arvoa: wheel_diameter
# Jos auto kääntyy liian vähän, nosta arvoa: axle_track
robot = DriveBase(l_motor, r_motor, wheel_diameter=55.5, axle_track=114)
robot.settings(turn_rate=90)
ev3.speaker.set_volume(50, which="_all_")

UP_ANGLE = 140
DOWN_ANGLE = 6

class Fork:
    """Haarukan Luokka"""
    def __init__(self, motor: Motor):
        """Alusta haarukka ja siirrä se 'up' asentoon."""
        self.motor = motor
        self.move("up")
        self.motor.reset_angle(UP_ANGLE)

    def position(self):
        """Palauttaa haarukan asennon"""
        angle = self.motor.angle()
        if angle > UP_ANGLE:
            return "up"
        elif angle < DOWN_ANGLE:
            return "down"
        else:
            return "N/A"
        
    def move(self, suunta:str):
        """Liikuta haarukkaa ylös tai alas."""
        if suunta == "up":
            self.motor.run_until_stalled(100, Stop.COAST, 40)
            print(self.motor.angle())
            return
        
        elif suunta == "down":
            self.motor.run_until_stalled(-100, Stop.COAST, 40)
            print(self.motor.angle())
            return

def find_middle():
    """Etsi esineen keskipiste käyttäen ultraäänisensoria."""
    SCAN_RANGE = 325

    # Käänny kunnes sensorin lukema menee suuremmaksi kuin scan_range
    # Etsi objektin vasen laita
    while u_sensor.distance() < SCAN_RANGE:
        robot.turn(-1)
        
    # Käännytään takaisin kunnes esine taas näkyy
    while u_sensor.distance() > SCAN_RANGE: 
        robot.turn(1)

    # Nollataan robotin käännökset, tätä voidaan käyttää esineen vasempana laitana
    robot.reset()

    # Etsi objektin oikea laita
    while u_sensor.distance() < SCAN_RANGE: 
        robot.turn(1)
        
    while u_sensor.distance() > SCAN_RANGE: 
        robot.turn(-1)

    
    # Koska käännökset nollattiin, voidaan jakaa robotin nykyiset asteet, joka antaa esineen keskikohdan
    object_center = robot.angle() / 2
    print("right:", robot.angle(), "mid:", object_center)

    robot.turn(-object_center)
    ev3.speaker.play_file("air_release.wav")
    return


def find_object(radius: int):
    '''
    Parametri: halutun alueen säde. \n
    Käänny vasemmalle ja oikealle edestaas,
    palauta sitten etäisyys esineeseen
    '''

    maara = 9
    asteet = radius / 2
    SCAN_RANGE = 325

    while u_sensor.distance() > SCAN_RANGE:

        for i in range(maara):
            print(u_sensor.distance())
            robot.turn(asteet/maara)

        if asteet > 0: 
            # jos asteet positiiviset
            robot.turn(-abs(asteet))
            asteet = -abs(asteet)

        else: #asteet negatiiviset
            robot.turn(abs(asteet))
            asteet = abs(asteet)

    distance = u_sensor.distance()

    ev3.speaker.play_file("sonar.wav")
    return distance


# main loop
def main():
    hand = Fork(m_motor)
    viiva_ylitetty = False

    while True:

        # Ajetaan ensin niin kauan kunnes viiva on ylitetty
        while not viiva_ylitetty:
            if c_sensor.reflection() > 40:
                robot.drive(100, 0)
                wait(10)
            else:
                robot.stop()
                viiva_ylitetty = True

        distance = find_object(120)
        
        find_middle()
        robot.straight(distance-5)

        hand.move("down")

        # Peruutetaan
        robot.straight(-200)

        # Liikutetaan käsi alas, jos käsi ei liiku kokonaan alas, lopetetaan sovellus
        hand.move("down")
        wait(500)
        if hand.position() not in ["up", "down"]:
            ev3.speaker.play_file("confirm.wav")
            wait(500)
            break

        # Jos käsi ei mene kokonaan alas, pallo ei ole haarukassa, mennään takaisin main loopin alkuun
        else:
            hand.move("up")

main()

