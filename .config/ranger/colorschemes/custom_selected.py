# ~/.config/ranger/plugins/custom_selected.py

import ranger.gui.context
import ranger.gui.widgets.browsercolumn

# Add the custom context tag 'selected' for the selected item
ranger.gui.context.CONTEXT_KEYS.append('selected')
ranger.gui.context.Context.selected = False

# Modify the hook to set 'selected' context when an item is selected
def new_hook_before_drawing(fsobject, color_list):
    if fsobject.is_selected:
        print(f"Selected: {fsobject.basename}")  # Debug print to check selection
        color_list.append('selected')  # Add 'selected' context tag
    return ranger.gui.widgets.browsercolumn.hook_before_drawing(fsobject, color_list)   
    # Call the original hook for other processing
    return ranger.gui.widgets.browsercolumn.hook_before_drawing(fsobject, color_list)

# Assign the modified hook back to the original one
ranger.gui.widgets.browsercolumn.hook_before_drawing = new_hook_before_drawing

