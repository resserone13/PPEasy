from scene import *
import sound
import random
import math
import ui


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
        
        self.description = LabelNode(f'{self.text}', (text_font, 25), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)      
        
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
                        
        self.mask_link = LabelNode('MASKS',font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.80), color=text_color, parent=self)
    
        self.face_shield_link = LabelNode('FACE SHIELDS', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.70), color=text_color, parent=self)
        
        self.gown_link = LabelNode('GOWNS', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.60), color=text_color, parent=self)
                
        self.wipes_link = LabelNode('WIPES', (text_font, 30), position=(self.size.w/2, self.size.h * 0.50), color=text_color, parent=self)
        
        self.faq_link = LabelNode('FAQ', font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.40), color=text_color, parent=self)
        
        self.faq_link = LabelNode("Dos/Don'ts", font=(text_font, 30), position=(self.size.w/2, self.size.h * 0.30), color=text_color, parent=self)
        
        self.present_modal_scene(Intro())
        
    def did_change_size(self):
        pass
    
    def update(self):
        pass
    
    def touch_began(self, touch):
        if touch.location in self.mask_box.frame:
            self.present_modal_scene(Mask())
                
        if touch.location in self.sheild_box.frame:
            sc = Any()
            sc.title_param = 'Faceshield'
            sc.image_param = 'FaceSheild.JPG'
            sc.text_param  = 'Face sheilds protect the entire face, \nincluding the eyes, from any splashes \nor sprays, which along with the nose \nand mouth can be a gateway for the \ncoronavirus. Wearing a face shield \nmay make you less likely to touch your \nface with unwashed hands. You should \nware a face shield while caring for \npatients. You never know what may \ncause something to splash towards \nyour face.'    
            
            self.present_modal_scene(sc)

        if touch.location in self.gowns_box.frame:
            self.present_modal_scene(Gowns())       

        if touch.location in self.wipes_box.frame:
            self.present_modal_scene(Wipes())       

        if touch.location in self.faq_box.frame:
            tv = ui.TableView()
            items = ['Q. What is the difference between \na K-N96 and a N95?', 'A. Both products are said to filter \n95 percent of aerosol particulates. \nKN95 respirators differ from N95 \nrespirators because they meet the \nChinese standard but are not \nregulated by U.S. agencies.', "Q. Do mask really work?", "A. Hell Yes"]
            tv.data_source = ui.ListDataSource(items=items)
            tv.present()        

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

        self.lvl3_mask = SpriteNode('FrontMask 2.PNG', position=(self.size.w * 0.75, self.size.h * 0.30), scale=0.25, parent=self)

        self.kn95_mask = SpriteNode('Kn95Mask.PNG', position=(self.size.w * 0.25, self.size.h * 0.15), scale=0.23, parent=self)

        self.n95_mask = SpriteNode('N95Mask.PNG', position=(self.size.w * 0.25, self.size.h * 0.29), scale=0.23, parent=self)   
        
        self.papr_mask = SpriteNode('PaprMask.PNG', position=(self.size.w * 0.60, self.size.h * 0.17), scale=0.50, parent=self)
        
    def touch_began(self, touch):
        if touch.location in self.level_1_box.frame:        
            sc = Any()
            sc.title_param = 'LEVEL 1'
            sc.image_param = 'FrontMask 2.PNG'
            sc.text_param  = "A level 1 mask provides adequate \nprotection in areas such as lobbies \nand the cafeteria. Its primary \nfunction is to stop any saliva\nor mucus from being transferred from \nperson to person \nIt's not recommended to wear \na level 1 mask while caring \nfor patients."
            self.present_modal_scene(sc)

        if touch.location in self.level_3_box.frame:
            sc = Any()
            sc.title_param = 'LEVEL 3'
            sc.image_param = 'Level3Mask.PNG'
            sc.text_param  = "A level 3 mask provides a higher \nlevel of protection than a level 1. \nAlthougth it looks very similar \na level 1 it can be distinguished \nfrom a level 1 by having at least 3 \nlayers of material. It also might \nhave a anti-fog stip to help with \nfogging. It's ok to ware a level 3 \nwhile around patients."
            self.present_modal_scene(sc)
            
        if touch.location in self.k_n95_box.frame:
            sc = Any()
            sc.title_param = 'K-N95'
            sc.image_param = 'Kn95Mask.PNG'
            sc.text_param  = "K-N95 masks are usually thicker \nand tighter fitting than a level 1 or 3 \nand provide a higher level of \nprotection. It's recommended for \nuse in patient areas such as the \nEmergency Dept and patient floors. \nA K-N95 is NOT fit tested and is \nNOT the same as a N95."
            self.present_modal_scene(sc)
            
        if touch.location in self.n95_box.frame:
            sc = Any()
            sc.title_param = 'N95'
            sc.image_param = 'N95Mask.PNG'
            sc.text_param  = "This is a N95 mask. \nIt should be worn while \ncaring for patients undergoing \nmedical procedures that \nhave been deemed as \naerosol generating procedures. \nYou should wear the N95 \nyou passed a fit test for."
            self.present_modal_scene(sc)

        if touch.location in self.papr_box.frame:
            sc = Any()
            sc.title_param = 'Papr'
            sc.image_param = 'PaprMask.PNG'
            sc.text_param  = "This is a Papr mask. \nIt is recommended for \nuse by individuals who \nhave not been or did not \npass a fit test. You should \nbe trained to ensure you \nproperly wear and clean \nthe Papr."
            self.present_modal_scene(sc)
            
        if touch.location in self.back.frame:
            self.dismiss_modal_scene()
                                
class Any(Scene):
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
            
            self.title = LabelNode(self.title_param, (app_title_font, 30), position=(self.size.w/2, self.size.h * 0.85), color=text_color, parent=self)
            
            self.image = SpriteNode(self.image_param, position=(self.size.w/2, self.size.h * 0.60), scale=0.50, parent=self)
            
        self.txt = text
        
        self.description = LabelNode(f'{self.text_param}', (text_font, 20), position=(self.size.w/2, self.size.h * 0.25), color=text_color, parent=self)    
        
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

        if touch.location in self.cloth_box.frame:
            sc = Any()
            sc.title_param = 'CLOTH'
            sc.image_param = 'ClothGown.PNG'
            sc.text_param  = 'This is a cloth gown. \nIt must be worn while \nproviding care to patients \nwho are in isolation. \n\nIts NOT recommended to \nwear a cloth gown while \ncaring for patients \nwith C-diff or TB.'
            self.present_modal_scene(sc)

        if touch.location in self.plastic_box.frame:
            sc = Any()
            sc.title_param = 'PLASTIC'
            sc.image_param = 'PlasticGown.PNG'
            sc.text_param  = 'This is a plastic gown. \nIt must be worn while \nproviding care to C-Diff \npatients. \n\nIts is recommended to \nwear a plastic gown while \nproviding care to patients \nwith TB.'
            self.present_modal_scene(sc)

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
            sc = Any()
            sc.title_param = 'OXIVIR'
            sc.image_param = 'OxyvirWipes.PNG'
            sc.text_param  = 'Oxivir is recommended for general \ndisinfecting. The active ingredient \nhydrogen peroxide. It does NOT \nkill the bacteria that causes C-Diff \nand should never be used to \ndisinfect anything that may be \ncontaminated with C-Diff.'
            self.present_modal_scene(sc)

        if touch.location in self.sani_box.frame:
            sc = Any()
            sc.title_param = 'BLEACH'
            sc.image_param = 'BleachWipes.PNG'
            sc.text_param  = 'Bleach is a Sporicidal disinfectant. \nThe active ingredient is Sodium \nhypochlorite. Bleach kills the \nbacteria that causes C-Diff \nand should always be used to \ndisinfect anything that may be \ncontaminated with C-Diff.'
            self.present_modal_scene(sc)

        if touch.location in self.bleach_box.frame:
            sc = Any()
            sc.title_param = 'SANI'
            sc.image_param = 'SaniWipes.PNG'
            sc.text_param  = 'Sani is recommended for general \ndisinfecting. The active ingredient \nis Alcohol. It does NOT kill the \nbacteria that causes C-Diff and \nshould never be used to \ndisinfect anything that may be \ncontaminated nwith C-Diff.'
            self.present_modal_scene(sc)

        if touch.location in self.ammonia_box.frame:
            sc = Any()
            sc.title_param = 'AMMONIA'
            sc.image_param = 'AmmoniaWipes.PNG'
            sc.text_param  = 'Ammonia is recommended for \ncleaning sensitive electiral devices. \nThe active ingredient Ammonia. \nIt does NOT kill the bacteria that \ncauses C-Diff and should never \nbe used to disinfect anything that \nmay be contaminated with C-Diff.'
            self.present_modal_scene(sc)
            
if __name__ == '__main__':
    run(MyScene(), show_fps=False)
