# ~/.config/ranger/colorschemes/my_custom_scheme.py

from ranger.gui.colorschemes.default import Default

class MyCustomScheme(Default):
    def use(self, context):
        # Default colors for foreground, background, and attributes
        foreground, background, attribute = super().use(context)
        
        # Check if the item is selected
        if context.selected:
            foreground = 11  # bright yellow (change this index to any other color)
            background = 0   # transparent background
        
        return foreground, background, attribute
