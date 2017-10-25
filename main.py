import pygame
import random
from config import *
from signal import Signal
from road import Road
from car import Car


class MessagePassing:

	def __init__(self):
		self.road = Road()
		self.signal1 = Signal(True, 540, 130)
		self.signal2 = Signal(False, 400, 50)
		self.car1 = Car(1)
		self.car2 = Car(2)


	def render(self):
		self.road.render()
		self.signal1.render()
		self.signal2.render()
		self.car1.render()
		self.car2.render()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
			    self.close()

		pygame.display.flip()
		screen.fill(WHITE)
		clock.tick(FPS)


	def run(self):
		while True:
			self.render()

			#random simulation
			if self.car1.move(self.signal1.on) or self.car2.move(self.signal2.on):
				if random.getrandbits(1):
					self.signal1.switch(1)
					self.signal2.switch(0)

				else:
					self.signal1.switch(0)
					self.signal2.switch(1)


	def close(self):
		pygame.quit()
		exit(0)


def main():
	mp = MessagePassing()
	mp.run()


if __name__ == '__main__':
	main()








