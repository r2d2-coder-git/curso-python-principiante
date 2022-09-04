#Import module
import modules
modules.make_pizza(16, 'pepperoni')
modules.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Import module with alias
import modules as m 
m.make_pizza(16, 'pepperoni')
m.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Import some functions of module
from modules import make_pizza
make_pizza(16, 'pepperoni')

#Import some functions of module with alias function
from modules import make_pizza as mp 
mp(16, 'pepperoni')

#Import all functions of module
from modules import * 
