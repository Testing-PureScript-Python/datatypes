from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_otherwise"
                        , metadata( 11
                                  , 13
                                  , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\.spago\\prelude\\v4.1.1\\src\\Data\\Boolean.purs"
                                  , True ) )
           , assign("exports", record(("otherwise", var("ps_otherwise")))) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\.spago\\prelude\\v4.1.1\\src\\Data\\Boolean.purs", name="datatypes.Data.Boolean.pure")
