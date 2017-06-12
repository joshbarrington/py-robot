import pygame, sys, time ,os
from pygame.locals import *

#PS4 controller functions and variables
class ps4:
	joystick=0
	joystick_count=0
	numaxes=0
	numbuttons=0
	numhats = 0
	#left=right=up=down=l1=l2=r1=r2=triangle=circle=square=cross=select=start=ps=joystick_left=joystick_right=0
	#a_left=a_right=a_up=a_down=a_l1=a_l2=a_r1=a_r2=a_triangle=a_circle=a_square=a_cross=a_select=a_start=a_ps=a_joystick_left_x=a_joystick_left_y=a_joystick_right_x=a_joystick_right_y=acc_x=acc_y=acc_z=gyro_yaw=0
	
	#Initialize the controller when the oject is created
	def __init__(self):
		#Make the stdout buffer as 0,because of bug in Pygame which keeps on printing debug statements
		#http://stackoverflow.com/questions/107705/python-output-buffering
		sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
		
		pygame.init()
		pygame.joystick.init()
		ps4.joystick = pygame.joystick.Joystick(0)
		ps4.joystick.init()
		ps4.joystick_count = pygame.joystick.get_count()
		ps4.numaxes = ps4.joystick.get_numaxes()
		ps4.numbuttons = ps4.joystick.get_numbuttons()
		ps4.numhats = ps4.joystick.get_numhats()
		# get count of joysticks=1, axes=12, buttons=14 for DualShock 4
	
	def update(self):
                button_state = [0]*self.numbuttons
		button_analog = [0]*self.numaxes
                outstr =""

                #Start suppressing the output on stdout from Pygame
		devnull = open('/dev/null', 'w')
		oldstdout_fno = os.dup(sys.stdout.fileno())
		os.dup2(devnull.fileno(), 1)

                #Read analog values
                for i in range(0,self.numaxes):
			button_analog[i] = self.joystick.get_axis(i)
                
		self.left_analog_x	=button_analog[0] # -1.0 Left, 1.0 Right
		self.left_analog_y	=button_analog[1] # -1.0 Up, 1.0 Down 
		
		self.right_analog_x	=button_analog[2] # -1.0 Left, 1.0 Right
		self.right_analog_y     =button_analog[5] # -1.0 Up, 1.0 Down
		
		self.a_L2		=button_analog[3] # Both triggers: -1.0 Released, 1.0 Held 
		self.a_R2		=button_analog[4]
		
		# Accelerometer and other data
		self.a_1	=button_analog[6]
		self.a_2	=button_analog[7]
		self.a_3	=button_analog[8]
		self.a_4	=button_analog[9]
		self.a_5	=button_analog[10]
                
                
		#Read digital values - returns True or False states
		for i in range(0,self.numbuttons):
			button_state[i]=self.joystick.get_button(i)
		self.square  			=button_state[0]
		self.x  			=button_state[1]
		self.circle  			=button_state[2]
		self.triangle			=button_state[3]
		self.L1			        =button_state[4]
		self.R1			        =button_state[5]
                self.L2                         =button_state[6]
                self.R2                         =button_state[7]
                self.share                      =button_state[8]
                self.options                    =button_state[9]
                self.left_analog                =button_state[10]
                self.right_analog               =button_state[11]
                self.ps_button                  =button_state[12]
                
		#Enable output on stdout
		os.dup2(oldstdout_fno, 1)	
		os.close(oldstdout_fno)
		
		#refresh
		pygame.event.get()
		return button_analog

	
	
