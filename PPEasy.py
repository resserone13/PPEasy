from scene import *
import sound
import random
import math

# --- To Do ---
#remove the x in the upper right hand corner. 

#Find better N 95 picture. 

#add dewell times for wipes

#list more Faqs

# finish dos and donts



A = Action
app_title = 'PPEasy'
app_title_font = 'Avenir Next Condensed Bold'
text_font = 'Arial'
text_color = 'black'
bg_color = '#9cbeff'
btn_border_color = 'white'
border_color = 'gray'
btn_color = '#9cbeff'
btn_shadow=('gray', 0, 7, 2)
border_radias = 30


class  Intro(Scene):
	def setup(self):

		self.intro_bg = SpriteNode(position=self.size/2, color=bg_color, size=self.size, alpha=1, parent=self)
				
		self.app_title = LabelNode('PPEasy', font=(app_title_font, 50), position=(self.size/2), color=text_color, parent=self)
		
		self.text = 'Thanks for being safe'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)		
		
		self.run_action(A.sequence(A.wait(3), A.call(self.dismiss_scene)))
	
	
	def dismiss_scene(self):
		self.dismiss_modal_scene()		
	
class MyScene (Scene):
	def setup(self):
		
		self.main_node = Node(parent=self)
				
		self.background_color = bg_color			
															
		self.mask_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.mask_box.position=(self.size.w/2, self.size.h * 0.79)
		self.mask_box.fill_color=btn_color
		self.mask_box.line_width=4
		self.mask_box.stroke_color=btn_border_color
		self.mask_box.shadow=btn_shadow
		self.add_child(self.mask_box)	
		
		self.sheild_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.sheild_box.position=(self.size.w/2, self.size.h * 0.69)
		self.sheild_box.fill_color=btn_color
		self.sheild_box.line_width=4
		self.sheild_box.stroke_color=btn_border_color
		self.sheild_box.shadow=btn_shadow		
		self.add_child(self.sheild_box)
		
		self.gowns_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.gowns_box.position=(self.size.w/2, self.size.h * 0.59)
		self.gowns_box.fill_color=btn_color
		self.gowns_box.line_width=4
		self.gowns_box.stroke_color=btn_border_color
		self.gowns_box.shadow=btn_shadow
		self.add_child(self.gowns_box)						
		self.wipes_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.wipes_box.position=(self.size.w/2, self.size.h * 0.49)
		self.wipes_box.fill_color=btn_color
		self.wipes_box.line_width=4
		self.wipes_box.stroke_color=btn_border_color
		self.wipes_box.shadow=btn_shadow		
		self.add_child(self.wipes_box)

		self.faq_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.faq_box.position=(self.size.w/2, self.size.h * 0.39)
		self.faq_box.fill_color=btn_color
		self.faq_box.line_width=4
		self.faq_box.stroke_color=btn_border_color
		self.faq_box.shadow=btn_shadow		
		self.add_child(self.faq_box)				
		
		self.dd_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.dd_box.position=(self.size.w/2, self.size.h * 0.29)
		self.dd_box.fill_color=btn_color
		self.dd_box.line_width=4
		self.dd_box.stroke_color=btn_border_color
		self.dd_box.shadow=btn_shadow		
		self.add_child(self.dd_box)	
		
		self.scene_title = LabelNode(app_title, font=(app_title_font, 50), position=(self.size.w/2, self.size.h * 0.90), color=text_color, parent=self)	
						
		self.mask_link = LabelNode('MASK',font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.80), color=text_color, parent=self)
	
		self.face_shield_link = LabelNode('FACE SHIELDS', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.70), color=text_color, parent=self)
		
		self.gown_link = LabelNode('GOWNS', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.60), color=text_color, parent=self)					
								
		self.wipes_link = LabelNode('WIPES', (text_font, 30), position=(self.size.w/2, self.size.h * 0.50), color=text_color, parent=self)
		
		self.faq_link = LabelNode('FAQ', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.40), color=text_color, parent=self)
		
		self.faq_link = LabelNode("Dos/Don'ts", font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.30), color=text_color, parent=self)
		
		#self.present_modal_scene(Intro())
		
	def did_change_size(self):
		pass
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		if touch.location in self.mask_box.frame:
			self.present_modal_scene(Mask())		

		if touch.location in self.sheild_box.frame:
			self.present_modal_scene(FaceSheild())		

		if touch.location in self.gowns_box.frame:
			self.present_modal_scene(Gowns())		

		if touch.location in self.wipes_box.frame:
			self.present_modal_scene(Wipes())		

		if touch.location in self.faq_box.frame:
			self.present_modal_scene(Faq())		

		if touch.location in self.dd_box.frame:
			self.present_modal_scene(DD())												
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

class Mask(Scene):
	def setup(self):

		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)
					
		self.level_1_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.level_1_box.position=(self.size.w/2, self.size.h * 0.79)
		self.level_1_box.fill_color=btn_color
		self.level_1_box.line_width=4
		self.level_1_box.stroke_color=btn_border_color
		self.level_1_box.shadow=btn_shadow		
		self.add_child(self.level_1_box)	

		self.level_3_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.level_3_box.position=(self.size.w/2, self.size.h * 0.69)
		self.level_3_box.fill_color=btn_color
		self.level_3_box.line_width=4
		self.level_3_box.stroke_color=btn_border_color
		self.level_3_box.shadow=btn_shadow		
		self.add_child(self.level_3_box)	

		self.k_n95_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.k_n95_box.position=(self.size.w/2, self.size.h * 0.59)
		self.k_n95_box.fill_color=btn_color
		self.k_n95_box.line_width=4
		self.k_n95_box.stroke_color=btn_border_color
		self.k_n95_box.shadow=btn_shadow		
		self.add_child(self.k_n95_box)

		self.n95_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.n95_box.position=(self.size.w/2, self.size.h * 0.49)
		self.n95_box.fill_color=btn_color
		self.n95_box.line_width=4
		self.n95_box.stroke_color=btn_border_color
		self.n95_box.shadow=btn_shadow		
		self.add_child(self.n95_box)
		
		self.papr_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.papr_box.position=(self.size.w/2, self.size.h * 0.39)
		self.papr_box.fill_color=btn_color
		self.papr_box.line_width=4
		self.papr_box.stroke_color=btn_border_color
		self.papr_box.shadow=btn_shadow		
		self.add_child(self.papr_box)						
											
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.93), parent=self)
				
		self.scene_title = LabelNode('Mask', font=(app_title_font, 50), position=(self.size.w/2, self.size.h * 0.90), color=text_color, parent=self)									
		self.level_1_link = LabelNode('Level 1',font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.80), color=text_color, parent=self)
	
		self.level_3_link = LabelNode('Level 3', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.70), color=text_color, parent=self)
		
		self.k_n95_link = LabelNode('K-N95', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.60), color=text_color, parent=self)					
								
		self.n95_link = LabelNode('N95', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.50), color=text_color, parent=self)		

		self.papr_link = LabelNode('PAPR', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.40), color=text_color, parent=self)
		
		#self.lvl1_mask = SpriteNode('FrontMask 2.PNG', position=(self.size.w * 0.75, self.size.h * 0.15), scale=0.25, parent=self)

		self.lvl3_mask = SpriteNode('FrontMask 2.PNG', position=(self.size.w * 0.75, self.size.h * 0.30), scale=0.25, parent=self)

		self.kn95_mask = SpriteNode('Kn95Mask.PNG', position=(self.size.w * 0.25, self.size.h * 0.15), scale=0.23, parent=self)

		self.n95_mask = SpriteNode('N95Mask.PNG', position=(self.size.w * 0.25, self.size.h * 0.29), scale=0.23, parent=self)	
		
		self.papr_mask = SpriteNode('PaprMask.PNG', position=(self.size.w * 0.60, self.size.h * 0.17), scale=0.50, parent=self)				
								
	def touch_began(self, touch):
		if touch.location in self.level_1_box.frame:
			self.present_modal_scene(Lvl_1())	
			
		if touch.location in self.level_3_box.frame:
			self.present_modal_scene(Lvl_3())	
			
		if touch.location in self.k_n95_box.frame:
			self.present_modal_scene(K_N95())
				
		if touch.location in self.n95_box.frame:
			self.present_modal_scene(N95())

		if touch.location in self.papr_box.frame:
			self.present_modal_scene(Papr())
			
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()
						
class Lvl_1(Scene):
	def setup(self):

		self.node = Node(parent=self)
		
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)




		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)				
			
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
		
		self.name = LabelNode('LEVEL 1', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.mask = SpriteNode('FrontMask 2.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'This is a level 1 mask. \nLevel 1 masks provides \nadequate protection in \nareas such as lobbies \nand the cafeteria. \nIts not recommended \nto wear a level 1 mask \nwhile caring for patients.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
		


	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()

class Lvl_3(Scene):
	def setup(self):

		self.node = Node(parent=self)
		
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)

		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)	
			
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
						
		self.name = LabelNode('Level 3', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.mask = SpriteNode('FrontMask 2.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = "This is a level 3 mask. \nA level 3 mask provides \na higher level of protection \nthan a level 1 by having \nat least 3 layers of material. \nIt's ok to ware a level 3 \nwhile around patients."
		
		self.discription = LabelNode(f'{self.text.center(100)}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
		


	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()
					
class K_N95(Scene):
	def setup(self):

		self.node = Node(parent=self)
		
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)

		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)	
			
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
						
		self.name = LabelNode('K-N95', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.mask = SpriteNode('Kn95Mask.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = "This is a K-N95 mask. \nIt is recommended for \nuse in areas patient areas \nsuch as the Emergency Dept \nand the patient floors. It's \nrecommended to wear a \nK-N95 mask while working \nwith Covid patients."
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
		

	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()
		
class N95(Scene):
	def setup(self):

		self.node = Node(parent=self)
		
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)

		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)
			
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
						
		self.name = LabelNode('N95', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.mask = SpriteNode('N95Mask.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = "This is a N95 mask. \nIt should be worn while \ncaring for patients undergoing \nmedical procedures that \nhave been deemed as \naerosol generating procedures. \nYou should wear the N95 \nyou passed a fit test for."
		
		self.discription = LabelNode(f'{self.text}', (text_font, 24), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()
		
class Papr(Scene):
	def setup(self):

		self.node = Node(parent=self)
		
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)

		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)
			
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
						
		self.name = LabelNode('Papr', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.mask = SpriteNode('PaprMask.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'This is a Papr mask. \nIt is recommended for \nuse by individuals who \nhave not been or did not \npass a fit test. You should \nbe trained to ensure you \nproperly wear and clean \nthe Papr.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)		

	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()		

class FaceSheild(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)	
		
		self.name = LabelNode('Face Sheild', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.face_sheild = SpriteNode('FaceSheild.JPG', position=(self.size.w/2, self.size.h * 0.60), scale=0.30, parent=self)
		
		self.text = 'This is a face sheild. \nA face sheild protects \nyour face and eyes. \nYou should ware a \n face sheild while \ncaring for patients.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
		
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()	
				
class Gowns(Scene):
	def setup(self):
	
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)	
		
		self.root_node = Node(parent=self)
		
		self.cloth_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.cloth_box.position=(self.size.w/2, self.size.h * 0.79)
		self.cloth_box.fill_color=btn_color
		self.cloth_box.line_width=4
		self.cloth_box.stroke_color=btn_border_color
		self.cloth_box.shadow=btn_shadow		
		self.root_node.add_child(self.cloth_box)	

		self.plastic_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.plastic_box.position=(self.size.w/2, self.size.h * 0.69)
		self.plastic_box.fill_color=btn_color
		self.plastic_box.line_width=4
		self.plastic_box.stroke_color=btn_border_color
		self.plastic_box.shadow=btn_shadow		
		self.root_node.add_child(self.plastic_box)	
										
		self.scene_title = LabelNode('Gowns', font=(app_title_font, 50), position=(self.size.w/2, self.size.h * 0.90), color=text_color, parent=self)
	
		self.cloth_link = LabelNode('Cloth', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.80), color=text_color, parent=self.root_node)

		self.plastic_link = LabelNode('Plastic',font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.70), color=text_color, parent=self.root_node)
		
		self.cloth_label = LabelNode('Cloth', font=(text_font, 30), position=(self.size.w  * 0.25, self.size.h * 0.50), color=text_color, parent=self.root_node)										
		self.plastic_label = LabelNode('Plastic',font=(text_font, 30), position=(self.size.w * 0.75, self.size.h * 0.60), color=text_color, parent=self.root_node)
	

		
		self.plastic = SpriteNode('PlasticGown.PNG', position=(self.size.w * 0.75, self.size.h * 0.40), scale=0.75, parent=self.root_node)

		self.cloth = SpriteNode('ClothGown.PNG', position=(self.size.w * 0.26, self.size.h * 0.26), scale=0.70, parent=self)		
		
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()	

		if touch.location in self.cloth_box.frame:
			self.present_modal_scene(ClothGown())

		if touch.location in self.plastic_box.frame:
			self.present_modal_scene(PlasticGown())											
class ClothGown(Scene):
	def setup(self):
	
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)	
		
		self.root_node = Node(parent=self)
		
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		

		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)				
		
		self.name = LabelNode('Cloth', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.gown = SpriteNode('ClothGown.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'This is a cloth gown. \nIt must be worn while \nproviding care to patients \nwho are in isolation. \n\nIts NOT recommended to \nwear a cloth gown while \ncaring for patients \nwith C-diff or TB.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
						
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()				
				
						
class PlasticGown(Scene):
	def setup(self):
	
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)	
		
		self.root_node = Node(parent=self)	
		
		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)				
		
		self.name = LabelNode('Plastic', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.gown = SpriteNode('PlasticGown.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'This is a plastic gown. \nIt must be worn while \nproviding care to C-Diff \npatients. \n\nIts is recommended to \nwear a plastic gown while \nproviding care to patients \nwith TB.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)
				
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()
							
class Wipes(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		self.oxy_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.oxy_box.position=(self.size.w/2, self.size.h * 0.79)
		self.oxy_box.fill_color=btn_color
		self.oxy_box.line_width=4
		self.oxy_box.stroke_color=btn_border_color
		self.oxy_box.shadow=btn_shadow		
		self.add_child(self.oxy_box)	

		self.sani_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.sani_box.position=(self.size.w/2, self.size.h * 0.69)
		self.sani_box.fill_color=btn_color
		self.sani_box.line_width=4
		self.sani_box.stroke_color=btn_border_color
		self.sani_box.shadow=btn_shadow		
		self.add_child(self.sani_box)	

		self.bleach_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.bleach_box.position=(self.size.w/2, self.size.h * 0.59)
		self.bleach_box.fill_color=btn_color
		self.bleach_box.line_width=4
		self.bleach_box.stroke_color=btn_border_color
		self.bleach_box.shadow=btn_shadow		
		self.add_child(self.bleach_box)

		self.ammonia_box = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.65, self.size.h * 0.07, 20))
		self.ammonia_box.position=(self.size.w/2, self.size.h * 0.49)
		self.ammonia_box.fill_color=btn_color
		self.ammonia_box.line_width=4
		self.ammonia_box.stroke_color=btn_border_color
		self.ammonia_box.shadow=btn_shadow		
		self.add_child(self.ammonia_box)
		
								
		self.scene_title = LabelNode('Wipes', font=(app_title_font, 50), position=(self.size.w/2, self.size.h * 0.90), color=text_color, parent=self)	

		self.oxy_link = LabelNode('Oxyvir',font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.80), color=text_color, parent=self)
	
		self.alcohol_link = LabelNode('Sani (alcohol)', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.70), color=text_color, parent=self)
		
		self.bleach_link = LabelNode('Bleach', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.60), color=text_color, parent=self)					
								
		self.ammonia_link = LabelNode('Ammonia', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.50), color=text_color, parent=self)		

		self.oxy = SpriteNode('OxyvirWipes.PNG', position=(self.size.w * 0.29, self.size.h * 0.35), scale=0.30, parent=self)

		self.alcohol = SpriteNode('SaniWipes.PNG', position=(self.size.w * 0.75, self.size.h * 0.35), scale=0.30, parent=self)

		self.bleach = SpriteNode('BleachWipes.PNG', position=(self.size.w * 0.30, self.size.h * 0.15), scale=0.30, parent=self)	
		
		self.ammonia = SpriteNode('AmmoniaWipes.PNG', position=(self.size.w * 0.75, self.size.h * 0.15), scale=0.30, parent=self)
		
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()	

		if touch.location in self.oxy_box.frame:
			self.present_modal_scene(Oxy())	

		if touch.location in self.sani_box.frame:
			self.present_modal_scene(Sani())	

		if touch.location in self.bleach_box.frame:
			self.present_modal_scene(Bleach())	

		if touch.location in self.ammonia_box.frame:
			self.present_modal_scene(Ammonia())	
												
class Oxy(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		self.root_node = Node(parent=self)	
		
		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)
			
		self.title = LabelNode('Oxivir', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.oxivir = SpriteNode('OxyvirWipes.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'Oxivir is recommended for general \ndisinfecting. The active ingredient \nhydrogen peroxide. It does NOT \nkill the bacteria that causes C-Diff \nand should never be used to \ndisinfect anything that may be \ncontaminated with C-Diff.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)					
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()
			
class Sani(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)	
		
		self.root_node = Node(parent=self)	
		
		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)
			
		self.title = LabelNode('Sani (Alcohol)', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.sani = SpriteNode('SaniWipes.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'Sani is recommended for general \ndisinfecting. The active ingredient \nis Alcohol. It does NOT kill the \nbacteria that causes C-Diff and \nshould never be used to \ndisinfect anything that may be \ncontaminated nwith C-Diff.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)			
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()	
			
class Bleach(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		self.root_node = Node(parent=self)	
		
		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)	

		self.title = LabelNode('Bleach', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.bleach = SpriteNode('BleachWipes.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'Bleach is a Sporicidal disinfectant. \nThe active ingredient is Sodium \nhypochlorite. Bleach kills the \nbacteria that causes C-Diff \nand should always be used to \ndisinfect anything that may be \ncontaminated with C-Diff.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)						
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()	
					
class Ammonia(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		self.root_node = Node(parent=self)	
		
		for i in (self.size.w/2, self.size.h * 0.8), (self.size.w/2, self.size.h * 0.4), (self.size.w/2, self.size.h * 0.1):
			self.text_line = ShapeNode(ui.Path.rounded_rect(0, 0, self.size.w * 0.8, 0, 20))
			self.text_line.position=i
			self.text_line.fill_color=btn_color
			self.text_line.line_width=4
			self.text_line.stroke_color=text_color
			self.add_child(self.text_line)
			
		self.title = LabelNode('Ammonia', (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)

		self.oxivir = SpriteNode('AmmoniaWipes.PNG', position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
		
		self.text = 'Ammonia is recommended for \ncleaning sensitive electiral devices. \nThe active ingredient Ammonia. \nIt does NOT kill the bacteria that \ncauses C-Diff and should never \nbe used to disinfect anything that \nmay be contaminated with C-Diff.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)					
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()

class Faq(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		self.scene_title = LabelNode('FAQ', font=(app_title_font, 50), position=(self.size.w/2, self.size.h * 0.90), color=text_color, parent=self)
		
		self.text = 'On March 13, 2020, the CDC \nupdated their recommendations for \nEPA-registered disinfectants to \nrefer to the EPA website \nfor EPA’s List N entitled Products \nwith Emerging Viral Pathogens and \nHuman Coronavirus claims for use against \nSARS-CoV-2 (COVID-19). \nSuper Sani-Cloth® Germicidal \nDisposable Wipes ,can be found on List N.'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)							
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()

class DD(Scene):
	def setup(self):
		self.bg_color = SpriteNode(color=bg_color, size=self.size, position=(self.size.w/2, self.size.h/2), parent=self)			

		self.scene_title = LabelNode("Dos and Don'ts", font=(app_title_font, 50), position=(self.size.w/2, self.size.h * 0.90), color=text_color, parent=self)
		
		self.text = 'Don’t put the mask around \nyour neck or up on your forehead. \n\nDon’t touch the mask, \nif you do, wash your hands \nor use hand sanitizer to disinfect​'
		
		self.discription = LabelNode(f'{self.text}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)							
		self.back = SpriteNode('iob:ios7_redo_32', position=(self.size.w * 0.87, self.size.h * 0.95), parent=self)		
	
	def touch_began(self, touch):
		if touch.location in self.back.frame:
			self.dismiss_modal_scene()						
									
if __name__ == '__main__':
	run(MyScene(), PORTRAIT, show_fps=False)
