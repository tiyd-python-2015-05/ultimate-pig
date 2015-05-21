__author__ = 'willflowers'


from simulation import Room, Roomba, Simulation

@pytest.fixture
def room():
    return Room(length=10, width=10)


def test_simulation_can_have_a_room_and_roombas(room):
    roomba = Roomba()
    sim = Simulation(room=room, roombas=[roomba])


    assert sim.room is room
    assert sim.roombas == [roomba]
    sim.step()

    assert roomba.position != start_position
    assert roomba.angle != 90


def test_simulation_runs():
    room = Room(3,3)
    roomba = Roomba(1,1, angle=90)


