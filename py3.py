import pygame, time, sys
from pygame.locals import *
import math 

PI = 3.1415 
WINDOWWIDTH = 1600
WINDOWHEIGHT = 800
RED =   (255, 0,  0)
GREEN = (0,  255, 0)
BLUE =  (0,   0, 255)
WHITE   = (255, 255, 255)
BLACK =   (0, 0, 0)
parking_area_width = 100
pygame.init()
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
car_speed = 10
angle = 0
sensor_range = 200	

def nesneler():   
	pygame.display.set_caption('CAR SIMULATION')
	BasicFont = pygame.font.Font('freesansbold.ttf', 20)
	pygame.draw.line(screen, BLACK, (5, 5), (1500,5), 12) #üst çizgi
	pygame.draw.line(screen, BLACK, (1500, 5), (1500,780), 12)#sag cizgi
	pygame.draw.line(screen, BLACK, (1500,780), (250,780), 12)#alt çizgi
	pygame.draw.line(screen, BLACK, (250,780), (250,150), 12)#sol cizgi
	pygame.draw.line(screen, BLACK, (250,150), (5,150), 12)
	for i in range(6):
		pygame.draw.line(screen, BLACK, (450,150 + (parking_area_width * i)), (750,150 + (parking_area_width * i)), 10)	
	for i in range(6):
		pygame.draw.line(screen, BLACK, (1000,150 + (parking_area_width * i)), (1300,150 + (parking_area_width * i)), 10)
	pygame.draw.line(screen, BLACK, (600,150), (600,150 + (5 * parking_area_width)), 10)
	pygame.draw.line(screen, BLACK, (1150,150), (1150,150 + (5 * parking_area_width)), 10) 
	image = pygame.image.load("car_image.jpeg")
	rect = image.get_rect()
	image = pygame.transform.scale(image, (110, 56))
	rect.x,rect.y = (470,175)
	screen.blit(image,rect)
	rect.x,rect.y = (470,275)
	screen.blit(image,rect)
	rect.x,rect.y = (470,375)
	screen.blit(image,rect)
	rect.x,rect.y = (1180,275)
	screen.blit(image,rect)
	rect.x,rect.y = (470,575)
	screen.blit(image,rect)
	rect.x,rect.y = (1020,175)
	screen.blit(image,rect)
	rect.x,rect.y = (1020,275)
	screen.blit(image,rect)
	rect.x,rect.y = (1020,275)
	screen.blit(image,rect)
	rect.x,rect.y = (1020,275)
	screen.blit(image,rect)
	rect.x,rect.y = (1020,475)
	screen.blit(image,rect)
	rect.x,rect.y = (1020,575)
	screen.blit(image,rect)
	rect.x,rect.y = (470,575)
	screen.blit(image,rect)
	rect.x,rect.y = (630,175)
	screen.blit(image,rect)
	rect.x,rect.y = (630,275)
	screen.blit(image,rect)
	rect.x,rect.y = (630,375)
	screen.blit(image,rect)
	rect.x,rect.y = (630,475)
	screen.blit(image,rect)
	rect.x,rect.y = (630,575)
	screen.blit(image,rect)
	rect.x,rect.y = (1180,375)
	screen.blit(image,rect)
	rect.x,rect.y = (1180,275)
	screen.blit(image,rect)
	rect.x,rect.y = (1180,475)
	screen.blit(image,rect)
	rect.x,rect.y = (1180,575)
	screen.blit(image,rect)
 

pygame.key.set_repeat(40, 40)   
screen_rect = screen.get_rect()
image_orig = pygame.image.load("car_image.jpeg").convert()
image_orig = pygame.transform.scale(image_orig, (110, 55))
image = image_orig.copy()
agent = image_orig.get_rect(center=screen_rect.center)
agent.left = 500
agent.top = 500

def degtorad(derece):
	return ((derece * 2 * PI) / 360)  

def rear_sensor():
	a, b = agent.center
	angle_arka = angle + 180
	if(0 <= angle_arka <= 90):
		b -= int(math.sin(degtorad(abs(angle_arka))) * 55)
		a += int(math.cos(degtorad(abs(angle_arka))) * 55)
	elif(90 <= angle_arka <= 180):
		b -= int(math.sin(degtorad(abs(angle_arka))) * 55)
		a += int(math.cos(degtorad(abs(angle_arka))) * 55)
	elif(270 >= angle_arka >= 180):
		b -= int(math.sin(degtorad(180 - (angle_arka))) * 55)
		a -= int(math.cos(degtorad(180 - (angle_arka))) * 55)
	elif(360 >= angle_arka >= 270):
		b -= int(math.sin(degtorad(180 - (angle_arka))) * 55)
		a -= int(math.cos(degtorad(180 - (angle_arka))) * 55)
	
	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle_arka <= 90):
				b -= int(math.sin(degtorad(abs(angle_arka))) * 10)
				a += int(math.cos(degtorad(abs(angle_arka))) * 10)
			elif(90 <= angle_arka <= 180):
				b -= int(math.sin(degtorad(abs(angle_arka))) * 10)
				a += int(math.cos(degtorad(abs(angle_arka))) * 10)
			elif(270 >= angle_arka >= 180):
				b -= int(math.sin(degtorad(180 - (angle_arka))) * 10)
				a -= int(math.cos(degtorad(180 - (angle_arka))) * 10)
			elif(360 >= angle_arka >= 270):
				b -= int(math.sin(degtorad(180 - (angle_arka))) * 10)
				a -= int(math.cos(degtorad(180 - (angle_arka))) * 10)

	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2)  
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1 - y2),2))
	if mesafe < 0:
		mesafe = 0
	return round (mesafe, 5)

def rear_right_sensor():
	angle_sagarka = 45 + angle
	a, b = agent.center
	if(27 >= 27 + angle >= -63):
		b += int(math.sin(degtorad((27 + angle))) * 61.7)
		a -= int(math.cos(degtorad((27 + angle))) * 61.7)
	elif(-63 >= 27 + angle >= -153):
		b -= int(math.sin(degtorad(abs(27 + angle))) * 61.7)
		a -= int(math.cos(degtorad(abs(27 + angle))) * 61.7)
	elif(117 <= (27 + angle) <= 207):
		b += int(math.sin(degtorad(abs(27 + angle))) * 61.7)
		a -= int(math.cos(degtorad(abs(27 + angle))) * 61.7)
	elif(27 <= (27 + angle) <= 117):
		b += int(math.sin(degtorad(180 - abs(27 + angle))) * 61.7)
		a += int(math.cos(degtorad(180 - abs(27 + angle))) * 61.7)
	
	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(27 >= angle_sagarka >= -63):
				b += int(math.sin(degtorad((angle_sagarka))) * 10)
				a -= int(math.cos(degtorad((angle_sagarka))) * 10)
			elif(-63 >= angle_sagarka >= -153):
				b -= int(math.sin(degtorad(abs(angle_sagarka))) * 10)
				a -= int(math.cos(degtorad(abs(angle_sagarka))) * 10)
			elif(117 <= angle_sagarka <= 230):
				b += int(math.sin(degtorad(abs(angle_sagarka))) * 10)
				a -= int(math.cos(degtorad(abs(angle_sagarka))) * 10)
			elif(27 <= (angle_sagarka) <= 117):
				b += int(math.sin(degtorad(180 - abs(angle_sagarka))) * 10)
				a += int(math.cos(degtorad(180 - abs(angle_sagarka))) * 10)
	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2) 
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	if(mesafe < 0):
		mesafe = 0
	return round (mesafe, 5)

def rear_left_sensor():
	angle_solarka = 45 - angle
	a, b = agent.center
	if(0 <= (27 - angle) <= 117):
		b -= int(math.sin(degtorad(abs(27 - angle))) * 61.7)
		a -= int(math.cos(degtorad(abs(27 - angle))) * 61.7)
	elif(117 <= (27 - angle) <= 207):
		b -= int(math.sin(degtorad(abs(27 - angle))) * 61.7)
		a -= int(math.cos(degtorad(abs(27 - angle))) * 61.7)
	elif(-63 >= 27 - angle >= -153):
		b += int(math.sin(degtorad(abs(27 - angle))) * 61.7)
		a -= int(math.cos(degtorad(abs(27 - angle))) * 61.7)
	elif(27 >= (27 - angle) >= -63):
		b += int(math.sin(degtorad(180 - abs(27 - angle))) * 61.7)
		a += int(math.cos(degtorad(180 - abs(27 - angle))) * 61.7)
	
	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle_solarka <= 117):
				b -= int(math.sin(degtorad(abs(angle_solarka))) * 10)
				a -= int(math.cos(degtorad(abs(angle_solarka))) * 10)
			elif(117 <= angle_solarka <= 230):
				b -= int(math.sin(degtorad(abs(angle_solarka))) * 10)
				a -= int(math.cos(degtorad(abs(angle_solarka))) * 10)
			elif(-63 >= angle_solarka >= -153):
				b += int(math.sin(degtorad(abs(angle_solarka))) * 10)
				a -= int(math.cos(degtorad(abs(angle_solarka))) * 10)
			elif(27 >= angle_solarka >= -63):
				b += int(math.sin(degtorad(180 - abs(angle_solarka))) * 10)
				a += int(math.cos(degtorad(180 - abs(angle_solarka))) * 10)
	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2) 
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	if(mesafe < 0):
		mesafe = 0
	return round (mesafe, 5)

def left_sensor():
	angle_sol = angle + 90
	a, b =agent.center
	if(0 < (angle + 90) < 90):
		b -= int(math.sin(degtorad(abs(angle + 90))) * 27.5)
		a += int(math.cos(degtorad(abs(angle + 90))) * 27.5)
	elif(90 <= (angle + 90) <= 180):
		b -= int(math.sin(degtorad(abs(angle + 90))) * 27.5)
		a += int(math.cos(degtorad(abs(angle + 90))) * 27.5)
	elif(0 >= (angle + 90) > -90):
		b += int(math.sin(degtorad(abs(angle + 90))) * 27.5)
		a += int(math.cos(degtorad(abs(angle + 90))) * 27.5)
	elif(-90 >= (angle + 90) > -180):
		b += int(math.sin(degtorad(180 - abs(angle + 90))) * 27.5)
		a -= int(math.cos(degtorad(180 - abs(angle + 90))) * 27.5)

	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle_sol <= 90):
				b -= int(math.sin(degtorad(abs(angle_sol))) * 10)
				a += int(math.cos(degtorad(abs(angle_sol))) * 10)
			elif(180 <= angle_sol <= 270):
				b -= int(math.sin(degtorad(abs(angle_sol))) * 10)
				a += int(math.cos(degtorad(abs(angle_sol))) * 10)
			elif(0 >= angle_sol >= -90):
				b += int(math.sin(degtorad(abs(angle_sol))) * 10)
				a += int(math.cos(degtorad(abs(angle_sol))) * 10)
			elif(180 >= angle_sol >= 90):
				b += int(math.sin(degtorad(180 + abs(angle_sol))) * 10)
				a -= int(math.cos(degtorad(180 + abs(angle_sol))) * 10)
	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2) 
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	if(mesafe < 0):
		mesafe = 0
	return round (mesafe, 5)

def right_sensor():
	angle_sag = angle - 90
	a, b =agent.center
	if(0 < (angle - 90) < 90):
		b -= int(math.sin(degtorad(abs(angle - 90))) * 27.5)
		a += int(math.cos(degtorad(abs(angle - 90))) * 27.5)
	elif(90 <= (angle - 90) <= 180):
		b -= int(math.sin(degtorad(abs(angle - 90))) * 27.5)
		a += int(math.cos(degtorad(abs(angle - 90))) * 27.5)
	elif(0 >= (angle - 90) > -90):
		b += int(math.sin(degtorad(abs(angle - 90))) * 27.5)
		a += int(math.cos(degtorad(abs(angle - 90))) * 27.5)
	elif(-90 >= (angle - 90) > -180):
		b += int(math.sin(degtorad(180 - abs(angle - 90))) * 27.5)
		a -= int(math.cos(degtorad(180 - abs(angle - 90))) * 27.5)

	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle_sag <= 90):
				b -= int(math.sin(degtorad(abs(angle_sag))) * 10)
				a += int(math.cos(degtorad(abs(angle_sag))) * 10)
			elif(-270 <= angle_sag <= -180):
				b -= int(math.sin(degtorad(-abs(angle_sag))) * 10)
				a += int(math.cos(degtorad(-abs(angle_sag))) * 10)
			elif(0 >= angle_sag >= -90):
				b += int(math.sin(degtorad(abs(angle_sag))) * 10)
				a += int(math.cos(degtorad(abs(angle_sag))) * 10)
			elif(-90 >= angle_sag >= -180):
				b += int(math.sin(degtorad(180 - abs(angle_sag))) * 10)
				a -= int(math.cos(degtorad(180 - abs(angle_sag))) * 10)
	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2) 
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	if(mesafe < 0):
		mesafe = 0
	return round (mesafe, 5)

def front_right_sensor():
	angle_sagon = angle - 45
	a, b = agent.center
	if(0 < (angle - 27) < 90 ):
		b -= int(math.sin(degtorad(abs(angle - 27))) * 61.7)
		a += int(math.cos(degtorad(abs(angle - 27))) * 61.7)
	elif(90 <= (angle - 27) <= 180 ):
		b -= int(math.sin(degtorad(abs(angle - 27))) * 61.7)
		a += int(math.cos(degtorad(abs(angle - 27))) * 61.7)
	elif(0 >= (angle - 27) > -90):
		b += int(math.sin(degtorad(abs(angle - 27))) * 61.7)
		a += int(math.cos(degtorad(abs(angle - 27))) * 61.7)
	elif(-90 >= (angle - 27) >= -207):
		b += int(math.sin(degtorad(180 - abs(angle - 27))) * 61.7)
		a -= int(math.cos(degtorad(180 - abs(angle - 27))) * 61.7)
	
	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle_sagon <= 90):
				b -= int(math.sin(degtorad(abs(angle_sagon))) * 10)
				a += int(math.cos(degtorad(abs(angle_sagon))) * 10)
			elif(90 <= angle_sagon <= 180 ):
				b -= int(math.sin(degtorad(abs(angle_sagon))) * 10)
				a += int(math.cos(degtorad(abs(angle_sagon))) * 10)
			elif(0 >= angle_sagon >= -90 or -215 >= angle_sagon >= -225):
				b += int(math.sin(degtorad(abs(angle_sagon))) * 10)
				a += int(math.cos(degtorad(abs(angle_sagon))) * 10)
			elif(-90 >= angle_sagon >= -207):
				b += int(math.sin(degtorad(180 - abs(angle_sagon))) * 10)
				a -= int(math.cos(degtorad(180 - abs(angle_sagon))) * 10)
	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2) 
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	if(mesafe < 0):
		mesafe = 0
	return round (mesafe, 5)
	

def front_sensor():
	a, b = agent.center
	if(0 <= angle <= 90):
		b -= int(math.sin(degtorad(abs(angle))) * 55)
		a += int(math.cos(degtorad(abs(angle))) * 55)
	elif(90 <= angle <= 180):
		b -= int(math.sin(degtorad(abs(angle))) * 55)
		a += int(math.cos(degtorad(abs(angle))) * 55)
	elif(0 >= angle >= -90):
		b += int(math.sin(degtorad(abs(angle))) * 55)
		a += int(math.cos(degtorad(abs(angle))) * 55)
	elif(-90 >= angle >= -180):
		b += int(math.sin(degtorad(180 - abs(angle))) * 55)
		a -= int(math.cos(degtorad(180 - abs(angle))) * 55)
	
	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle <= 90):
				b -= int(math.sin(degtorad(abs(angle))) * 10)
				a += int(math.cos(degtorad(abs(angle))) * 10)
			elif(90 <= angle <= 180):
				b -= int(math.sin(degtorad(abs(angle))) * 10)
				a += int(math.cos(degtorad(abs(angle))) * 10)
			elif(0 >= angle >= -90):
				b += int(math.sin(degtorad(abs(angle))) * 10)
				a += int(math.cos(degtorad(abs(angle))) * 10)
			elif(-90 >= angle >= -180):
				b += int(math.sin(degtorad(180 - abs(angle))) * 10)
				a -= int(math.cos(degtorad(180 - abs(angle))) * 10)

	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2)  
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1 - y2),2))
	if mesafe < 0:
		mesafe = 0
	return round (mesafe, 5)

def front_left_sensor():
	angle_solon = angle + 45
	a, b = agent.center
	if(0 < (angle + 27) < 90):
		b -= int(math.sin(degtorad(abs(angle + 27))) * 61.7)
		a += int(math.cos(degtorad(abs(angle + 27))) * 61.7)
	elif(90 <= (angle + 27) <= 207):
		b -= int(math.sin(degtorad(abs(angle + 27))) * 61.7)
		a += int(math.cos(degtorad(abs(angle + 27))) * 61.7)
	elif(0 >= (angle + 27) > -90):
		b += int(math.sin(degtorad(abs(angle + 27))) * 61.7)
		a += int(math.cos(degtorad(abs(angle + 27))) * 61.7)
	elif(-90 >= (angle + 27) > -180):
		b += int(math.sin(degtorad(180 - abs(angle + 27))) * 61.7)
		a -= int(math.cos(degtorad(180 - abs(angle + 27))) * 61.7)
	
	x2,y2 = a,b
	for i in range(sensor_range):
		reference = (a,b)
		if (screen.get_at(reference) != (255, 255, 255, 255)):
			intersect = reference 
			break      
		else:
			if(0 <= angle_solon <= 90):
				b -= int(math.sin(degtorad(abs(angle_solon))) * 10)
				a += int(math.cos(degtorad(abs(angle_solon))) * 10)
			elif(90 <= angle_solon <= 225):
				b -= int(math.sin(degtorad(abs(angle_solon))) * 10)
				a += int(math.cos(degtorad(abs(angle_solon))) * 10)
			elif(0 >= angle_solon >= -90):
				b += int(math.sin(degtorad(abs(angle_solon))) * 10)
				a += int(math.cos(degtorad(abs(angle_solon))) * 10)
			elif(-90 >= angle_solon >= -180):
				b += int(math.sin(degtorad(180 - abs(angle_solon))) * 10)
				a -= int(math.cos(degtorad(180 - abs(angle_solon))) * 10)
	x1,y1 = reference
	pygame.draw.line(screen, BLACK, (x2,y2), (x1,y1), 2) 
	mesafe = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
	if(mesafe < 0):
		mesafe = 0
	return round (mesafe, 5)
	

while True: 
	nesneler()
	sensor_left = left_sensor()
	sensor_right = right_sensor()
	sensor_front_right = front_right_sensor()
	sensor_front = front_sensor()
	sensor_front_left = front_left_sensor()
	sensor_rear_left = rear_left_sensor()
	sensor_rear_right = rear_right_sensor()
	sensor_rear = rear_sensor()
	print(f"sensor_front -- {sensor_front}")
	print(f"sensor_front_left -- {sensor_front_left}")
	print(f"sensor_front_right -- {sensor_front_right}")
	print(f"sensor_right -- {sensor_right}")
	print(f"sensor_left -- {sensor_left}")
	print(f"sensor_rear_left -- {sensor_rear_left}")
	print(f"sensor_rear_right -- {sensor_rear_right}")
	print(f"sensor_rear-- {sensor_rear}")

	image = pygame.transform.rotate(image_orig, angle)
	agent = image.get_rect(center=agent.center)
	screen.blit(image, agent)
	pygame.display.update()
	screen.fill(WHITE)
	x1,y1 = agent.center
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:     
			if event.key == pygame.K_LEFT:      #ileri sol
				if(angle >= 180):
					angle = -170
				else:
					angle += 10
				if(0 <= angle <= 90):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(90 <= angle <= 180):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(0 >= angle >= -90):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(-90 >= angle >= -180):
					agent.top += math.sin(degtorad(180 - abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(180 - abs(angle))) * car_speed
			elif event.key == pygame.K_RIGHT:       #ileri sağ
				if(angle <= -180):
					angle = 170
				else:
					angle += -10
				if(0 <= angle <= 90):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(90 <= angle <= 180):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(0 >= angle >= -90):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(-90 >= angle >= -180):
					agent.top += math.sin(degtorad(180 - abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(180 - abs(angle))) * car_speed
			elif event.key == pygame.K_UP:      #ileri
				if(0 <= angle <= 90):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(90 <= angle < 180):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(0 >= angle >= -90):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right += math.cos(degtorad(abs(angle))) * car_speed
				elif(-90 >= angle >= -180 or angle == 180):
					agent.top += math.sin(degtorad(180 - abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(180 - abs(angle))) * car_speed
			elif event.key == pygame.K_a:       #geri sol
				if(angle <= -180):
					angle = 170
				else:
					angle += -10
				if(0 <= angle <= 90):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(90 <= angle <= 180):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(0 >= angle >= -90):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(-90 >= angle >= -180):
					agent.top -= math.sin(degtorad(180 - abs(angle))) * car_speed
					agent.right += math.cos(degtorad(180 - abs(angle))) * car_speed
			elif event.key == pygame.K_d:       #geri sağ
				if(angle >= 180):
					angle = -170
				else:
					angle += 10
				if(0 <= angle <= 90):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(90 <= angle <= 180):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(0 >= angle >= -90):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(-90 >= angle >= -180):
					agent.top -= math.sin(degtorad(180 - abs(angle))) * car_speed
					agent.right += math.cos(degtorad(180 - abs(angle))) * car_speed
			elif event.key == pygame.K_DOWN:        #geri
				if(0 <= angle <= 90):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					if(angle != 90):
						agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(90 <= angle <= 180):
					agent.top += math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(0 >= angle > -90):
					agent.top -= math.sin(degtorad(abs(angle))) * car_speed
					agent.right -= math.cos(degtorad(abs(angle))) * car_speed
				elif(-90 >= angle >= -180):
					agent.top -= math.sin(degtorad(180 - abs(angle))) * car_speed
					agent.right += math.cos(degtorad(180 - abs(angle))) * car_speed



