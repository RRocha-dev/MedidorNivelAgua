import RPi.GPIO as GPIO
import time
import requests
  
def enviaDado(dado):
    request = requests.get("http://estacioapi.herokuapp.com/estacio/insert/" + dado)

def cor(r,g,b):
  GPIO.output(29, r)
  GPIO.output(33, g)
  GPIO.output(31, b)

try:
  GPIO.setmode(GPIO.BOARD)
  
  TRIG = 7
  ECHO = 16
  
  GPIO.setup(TRIG, GPIO.OUT)
  GPIO.setup(ECHO, GPIO.IN)

  GPIO.setup(33, GPIO.OUT)
  GPIO.setup(31, GPIO.OUT)
  GPIO.setup(29, GPIO.OUT)

  while True:
    #cor(159,0,159)
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(1)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.0004)
    GPIO.output(TRIG, GPIO.LOW)
    
    while GPIO.input(ECHO) == 0:
      pulse_start_time = time.time()
      
    while GPIO.input(ECHO) == 1:
      pulse_end_time = time.time()
      
    pulse_duration = (pulse_end_time - pulse_start_time) * .5
    distance = round(pulse_duration * 17150, 2)
    
    print("Distancia: " , distance)
    
    percentual = ((distance - 3) * 11) / 100
    percentual = 100 - percentual
    percentual = round(percentual,2)
    
    enviaDado(str(percentual))
    
    if percentual < 0 :
      percentual = 0
    if percentual <= 25:
      cor(1,0,0)
    if percentual >= 50 or percentual > 25:
      cor(1,0,1)
    if percentual >= 75:
      cor(0,0,1)
    if percentual > 100:
        percentual = 100
      
    print("Percentual: " , percentual)
      
except KeyboardInterrupt:
  print("Terminado pelo usuário")

finally:
  GPIO.cleanup()
