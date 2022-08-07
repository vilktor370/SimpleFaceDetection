
import pyfirmata
import time
USB_PORT = "/dev/ttyACM0" 
def main():
    board = pyfirmata.Arduino(USB_PORT)
    it = pyfirmata.util.Iterator(board)
    it.start()
    Tv1 = board.get_pin('d:10:i')
    time.sleep(1.0)
    print(Tv1.read())

if __name__ =='__main__':
    main()