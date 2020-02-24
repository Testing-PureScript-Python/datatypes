from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block("No document", assign("exports", record()))
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\.spago\\prelude\\v4.1.1\\src\\Prelude.purs", name="datatypes.Prelude.pure")
