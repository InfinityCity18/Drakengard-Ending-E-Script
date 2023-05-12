import vgamepad as vg
import time

class Controller:
    def __init__(self, gamepad):
        self.gamepad = gamepad
    def x(self):
        self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        self.gamepad.update()
        time.sleep(0.15)
        self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        self.gamepad.update()
    def y(self):
        self.gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.gamepad.update()
        time.sleep(0.15)
        self.gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        self.gamepad.update()

def main():
    
    print("start")
    gamepad = vg.VX360Gamepad()
    controller = Controller(gamepad=gamepad)
    time.sleep(1)
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.5)
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(11.5)
    controller.x()
    time.sleep(2.5)
    controller.x()
    time.sleep(2.5)
    controller.x()
    time.sleep(2.5)
    controller.x()
    time.sleep(2.5)
    controller.y()
    time.sleep(2.5)
    controller.y()
    time.sleep(2.5)
    controller.y()
    time.sleep(2.5)
    controller.y()
    time.sleep(2.5)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.y()
    time.sleep(0.67)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(6.5)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.y()
    time.sleep(0.37)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(0.55)
    controller.x()
    time.sleep(0.55)
    controller.y()
    time.sleep(0.55)
    controller.x()
    time.sleep(0.55)
    controller.y()
    time.sleep(0.55)
    controller.x()
    time.sleep(0.55)
    controller.x()
    time.sleep(1.25)
    controller.y()
    time.sleep(0.55)
    controller.x()
    time.sleep(0.55)
    controller.y()
    time.sleep(0.55)
    controller.x()
    time.sleep(0.55)
    controller.y()
    time.sleep(0.60)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.x()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.67)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.x()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.7)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.8)
    controller.y() #----
    time.sleep(0.05) # one chain
    controller.x() #
    time.sleep(0.05) #----
    controller.y() #----
    time.sleep(0.05) # one chain
    controller.x() #
    time.sleep(0.05) #----
    controller.y() #----
    time.sleep(0.05) # one chain
    controller.x() #
    time.sleep(0.05) #----
    controller.y() #----
    time.sleep(0.05) # one chain
    controller.x() #
    time.sleep(0.05) #----
    controller.x()
    time.sleep(5.25)
    controller.y()
    time.sleep(5.25)
    controller.y()
    time.sleep(1.25)
    controller.x()
    time.sleep(0.5)
    controller.x()
    time.sleep(0.5)
    controller.x()
    time.sleep(0.5)
    controller.y()
    time.sleep(0.5)
    controller.x()
    time.sleep(0.5)
    controller.x()
    time.sleep(0.5)
    controller.x()
    time.sleep(0.5)
    controller.y()
    time.sleep(0.5)
    controller.x()
    time.sleep(0.02)
    controller.x()
    time.sleep(0.02)
    controller.x()
    time.sleep(0.02)
    controller.x()
    time.sleep(0.6)
    controller.x()
    time.sleep(0.6)
    controller.y()
    time.sleep(0.6)
    controller.x()
    time.sleep(0.02)
    controller.x()
    time.sleep(0.02)
    controller.x()
    time.sleep(0.02)
    controller.x()
    time.sleep(0.6)
    controller.x()
    time.sleep(0.6)
    print("debug 0")
    controller.y()
    time.sleep(0.6)
    controller.y() # chain start
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.y()
    time.sleep(0.05)
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.y()
    time.sleep(0.05)
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(0.05)
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x() # seq start
    time.sleep(0.05)
    controller.y()
    time.sleep(0.05) # seq end
    controller.x()
    time.sleep(0.05)
    controller.x()
    time.sleep(9.5)
    controller.y()

    




if __name__ == '__main__':
    main()