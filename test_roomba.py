from simulation import Roomba



__author__ = 'willflowers'

def test_roomba_should_know_its_position():
    roomba = Roomba(x=5, y-=5)
    assert roomba.position == (5,5)


def test_roomba_should_know_its_angle():
    roomba = Roomba(angle=90)
    assert roomba.angle == 90


def test_roomba_should_have_a_speed():
    roomba = Roomba()
    assert roomba.speed = 1


def test_roomba_should_know_next_position():
    roomba = Roomba(x=10, y=10, angle=45)
    assert roomba.next_position == (10 + math.sqrt(0.5), 10 + math.sqrt(0.5))


def test_roomba_should_turn_45_degrees_on_collision():
    roomba = Roomba(angle = 270)
    roomba.collide()
    assert roomba.angle == 325


roomba.collide()
    assert roomba.angle == 10




