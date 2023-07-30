from MainController import MainController
from command import *
from Tank import Tank
from Telecom import Telecom


if __name__ == "__main__":
    tank = Tank()
    telecom = Telecom()
    main_controller = MainController(
        {
            '1': TankMoveForward(tank),
            '2': TankMoveBackward(tank),
            '3': TelecomConnect(telecom),
            '4': TelecomDisconnect(telecom),
        }
    )
    main_controller.command['5'] = ResetMainController(main_controller)
    main_controller.start()
