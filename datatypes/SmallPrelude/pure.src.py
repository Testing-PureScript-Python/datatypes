from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "$foreign"
                        , call( var('import_module')
                              , "datatypes.ffi.SmallPrelude" ) )
           , assign_star( "ps_Effect_Console"
                        , call( var('import_module')
                              , "datatypes.Effect.Console.pure" ) )
           , assign_star( "ps_println"
                        , define( None
                                , ["ps_$5"]
                                , block( ret( call( get_item( var( "ps_Effect_Console" )
                                                            , "log" )
                                                  , call( get_item( var( "$foreign" )
                                                                  , "showAny" )
                                                        , var( "ps_$5" ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("println", var("ps_println"))
                           , ( "showAny"
                             , get_item(var("$foreign"), "showAny") ) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\SmallPrelude.purs", name="datatypes.SmallPrelude.pure")
