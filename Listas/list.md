﻿"""
The listbox offers four different selection modes through the selectmode option. These are SINGLE (just a single choice), BROWSE (same, but the selection can be moved using the mouse), MULTIPLE (multiple item can be choosen, by clicking at them one at a time), or EXTENDED (multiple ranges of items can be chosen, using the Shift and Control keyboard modifiers). The default is BROWSE. Use MULTIPLE to get “checklist” behavior, and EXTENDED when the user would usually pick only one item, but sometimes would like to select one or more ranges of items.

As for listbox.get(ACTIVE), the item that is ACTIVE is the one that is underlined. You can see that this is only updated upon release of the mouse button. Because the <<ListboxSelect>> event is triggered on the mouse press, you get the previously selected item, because the ACTIVE is not updated yet.
 """