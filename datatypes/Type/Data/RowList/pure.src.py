from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_RLProxy"
                        , block( define( "ps_RLProxy"
                                       , [".this"]
                                       , block(var(".this")) )
                               , set_attr( var("ps_RLProxy")
                                         , "value"
                                         , new(var("ps_RLProxy")) )
                               , var("ps_RLProxy") ) )
           , assign("exports", record(("RLProxy", var("ps_RLProxy")))) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\.spago\\prelude\\v4.1.1\\src\\Type\\Data\\RowList.purs", name="datatypes.Type.Data.RowList.pure")
