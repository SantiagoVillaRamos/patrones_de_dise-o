from abstract_factory import UIAbstracFactory, Button, TextBox


class DarkButton(Button):
    def paint(self):
        print("\nDark Button")
        
class DarkTextBox(TextBox):
    def paint(self):
        print("\nDark TextBox")
        
class LightButton(Button):
    def paint(self):
        print("\n Light Button")
        
class LightTextBox(TextBox):
    def paint(self):
        print("\nLight TextBox")
        
        
"""Fabrica"""
# 1
class DarkUIFactory(UIAbstracFactory):
    def create_button(self):
        return DarkButton()
    
    def create_textbox(self):
        return DarkTextBox()
    
#2
class LightUIFactory(UIAbstracFactory):
    def create_button(self):
        return LightButton()
    
    def create_textbox(self):
        return LightTextBox()