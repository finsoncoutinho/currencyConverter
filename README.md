# Real Time Currency Converter

This project is made using Forex Python and tkinter.

##Forex Python
Forex Python is a Free Foreign exchange rates and currency conversion. It has functions and parameters which can take inputs for the required currency codes and then give the result for the conversion.

The below example gives the live conversion rate.
## Example:
```
from forex_python.converter import CurrencyRates

c = CurrencyRates()

print(c.get_rate('USD', 'GBP'))
```
## Output:
```
0.8257387755
```

##Tkinter
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

To creat a GUI application you need to perform the following steps:
1. Import the Tkinter module.
1. Create the GUI application main window.
1. Add one or more of the widgets to the GUI application.
1. Enter the main event loop to take action against each event triggered by the user.

## Example:

```
#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
```
