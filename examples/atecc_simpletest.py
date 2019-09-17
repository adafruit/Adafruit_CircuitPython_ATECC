# testing adafruit atecc module
import board
import adafruit_atecc
import busio


_WAKE_CLK_FREQ = 100000 # slower clock speed 	
i2c = busio.I2C(board.SCL, board.SDA, frequency=_WAKE_CLK_FREQ)

adafruit_atecc.ATECCx08A(i2c)