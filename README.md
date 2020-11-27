# pylog

A simple yet effective logging solution that doesnt require `import logging`!

# Installation

`pip install git+https://github.com/9u3/pylog/`

# Usage

```python
from PYLog import PYLog # Do this unless you want PYLog.PYLog.log

from PYLog import Colors, Strings # This is for diagnostic purposes mainly.

# In Strings._all and Colors._all you will see one for [LOG], This is the generic one.

info = PYLog.mode("info") # You MUST define the ones you need
error = PYLog.mode("error")
warn = PYLog.mode("warn")
success = PYLog.mode("success")
generic = PYLog.mode("") # If you want generic, You can have it as an empty string, Or put anything in there. Even PYLog.mode("protogen") would still come out as generic!

PYLog.log(info, "what") # The log.
PYLog.log(error, "what")
PYLog.log(warn, "what")
PYLog.log(success, "what")
PYLog.log(generic, "what")
```

# Note from Nox.

I thank you all for using my modules, It really means a lot to me. You don't understand.
The time and effort I put into making these for people to use is extreme, And I almost get no users in return..
So if you could just credit me if you use this module, I would really appreciate it!

You can use this for credits:
```python
# Module 'PYLog' created by NoxProtogen / 9u3.
# Github: https://github.com/9u3
# Module: https://github.com/9u3/pylog
# Twitter: https://twitter.com/noxprotogen
```
I'll say it again. Thank you.
