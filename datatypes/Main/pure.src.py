from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign_star( "ps_Control_Bind"
                        , call( var('import_module')
                              , "datatypes.Control.Bind.pure" ) )
           , assign_star( "ps_Effect"
                        , call(var('import_module'), "datatypes.Effect.pure") )
           , assign_star( "ps_SmallPrelude"
                        , call( var('import_module')
                              , "datatypes.SmallPrelude.pure" ) )
           , assign_star( "ps_PADT1"
                        , block( define( "ps_PADT1"
                                       , ["ps_value0", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_PADT1")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( new( var( "ps_PADT1" )
                                                                  , var( "ps_value0" ) ) ) ) ) )
                               , var("ps_PADT1") ) )
           , assign_star( "ps_PADT2"
                        , block( define( "ps_PADT2"
                                       , ["ps_value0", "ps_value1", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , set_item( var(".this")
                                                        , "value1"
                                                        , var("ps_value1") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_PADT2")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( define( None
                                                                     , [ "ps_value1" ]
                                                                     , block( ret( new( var( "ps_PADT2" )
                                                                                      , var( "ps_value0" )
                                                                                      , var( "ps_value1" ) ) ) ) ) ) ) ) )
                               , var("ps_PADT2") ) )
           , assign_star( "ps_PADT3"
                        , block( define( "ps_PADT3"
                                       , ["ps_value0", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_PADT3")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( new( var( "ps_PADT3" )
                                                                  , var( "ps_value0" ) ) ) ) ) )
                               , var("ps_PADT3") ) )
           , assign_star( "ps_PF"
                        , define(None, ["ps_x"], block(ret(var("ps_x")))) )
           , assign_star( "ps_A"
                        , block( define("ps_A", [".this"], block(var(".this")))
                               , set_attr( var("ps_A")
                                         , "value"
                                         , new(var("ps_A")) )
                               , var("ps_A") ) )
           , assign_star( "ps_B"
                        , block( define("ps_B", [".this"], block(var(".this")))
                               , set_attr( var("ps_B")
                                         , "value"
                                         , new(var("ps_B")) )
                               , var("ps_B") ) )
           , assign_star( "ps_C"
                        , block( define("ps_C", [".this"], block(var(".this")))
                               , set_attr( var("ps_C")
                                         , "value"
                                         , new(var("ps_C")) )
                               , var("ps_C") ) )
           , assign_star( "ps_ADT1"
                        , block( define( "ps_ADT1"
                                       , ["ps_value0", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_ADT1")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( new( var( "ps_ADT1" )
                                                                  , var( "ps_value0" ) ) ) ) ) )
                               , var("ps_ADT1") ) )
           , assign_star( "ps_ADT2"
                        , block( define( "ps_ADT2"
                                       , ["ps_value0", "ps_value1", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , set_item( var(".this")
                                                        , "value1"
                                                        , var("ps_value1") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_ADT2")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( define( None
                                                                     , [ "ps_value1" ]
                                                                     , block( ret( new( var( "ps_ADT2" )
                                                                                      , var( "ps_value0" )
                                                                                      , var( "ps_value1" ) ) ) ) ) ) ) ) )
                               , var("ps_ADT2") ) )
           , assign_star( "ps_ADT3"
                        , block( define( "ps_ADT3"
                                       , ["ps_value0", ".this"]
                                       , block( set_item( var(".this")
                                                        , "value0"
                                                        , var("ps_value0") )
                                              , ret(var(".this")) ) )
                               , set_attr( var("ps_ADT3")
                                         , "create"
                                         , define( None
                                                 , ["ps_value0"]
                                                 , block( ret( new( var( "ps_ADT3" )
                                                                  , var( "ps_value0" ) ) ) ) ) )
                               , var("ps_ADT3") ) )
           , assign_star( "ps_F"
                        , define(None, ["ps_x"], block(ret(var("ps_x")))) )
           , assign_star( "ps_main"
                        , call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                          , "discard" )
                                                , get_item( var( "ps_Control_Bind" )
                                                          , "discardUnit" ) )
                                          , get_item( var("ps_Effect")
                                                    , "bindEffect" ) )
                                    , call( get_item( var("ps_SmallPrelude")
                                                    , "println" )
                                          , metadata( 27
                                                    , 13
                                                    , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                    , "enums:" ) ) )
                              , define( None
                                      , ["ps_$__unused"]
                                      , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                    , "discard" )
                                                                          , get_item( var( "ps_Control_Bind" )
                                                                                    , "discardUnit" ) )
                                                                    , get_item( var( "ps_Effect" )
                                                                              , "bindEffect" ) )
                                                              , call( get_item( var( "ps_SmallPrelude" )
                                                                              , "println" )
                                                                    , get_attr( var( "ps_A" )
                                                                              , "value" ) ) )
                                                        , define( None
                                                                , [ "ps_$__unused" ]
                                                                , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                              , "discard" )
                                                                                                    , get_item( var( "ps_Control_Bind" )
                                                                                                              , "discardUnit" ) )
                                                                                              , get_item( var( "ps_Effect" )
                                                                                                        , "bindEffect" ) )
                                                                                        , call( get_item( var( "ps_SmallPrelude" )
                                                                                                        , "println" )
                                                                                              , get_attr( var( "ps_B" )
                                                                                                        , "value" ) ) )
                                                                                  , define( None
                                                                                          , [ "ps_$__unused" ]
                                                                                          , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                        , "discard" )
                                                                                                                              , get_item( var( "ps_Control_Bind" )
                                                                                                                                        , "discardUnit" ) )
                                                                                                                        , get_item( var( "ps_Effect" )
                                                                                                                                  , "bindEffect" ) )
                                                                                                                  , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                  , "println" )
                                                                                                                        , get_attr( var( "ps_C" )
                                                                                                                                  , "value" ) ) )
                                                                                                            , define( None
                                                                                                                    , [ "ps_$__unused" ]
                                                                                                                    , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                  , "discard" )
                                                                                                                                                        , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                  , "discardUnit" ) )
                                                                                                                                                  , get_item( var( "ps_Effect" )
                                                                                                                                                            , "bindEffect" ) )
                                                                                                                                            , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                            , "println" )
                                                                                                                                                  , metadata( 32
                                                                                                                                                            , 13
                                                                                                                                                            , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                            , "ordinary adts:" ) ) )
                                                                                                                                      , define( None
                                                                                                                                              , [ "ps_$__unused" ]
                                                                                                                                              , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                            , "discard" )
                                                                                                                                                                                  , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                            , "discardUnit" ) )
                                                                                                                                                                            , get_item( var( "ps_Effect" )
                                                                                                                                                                                      , "bindEffect" ) )
                                                                                                                                                                      , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                      , "println" )
                                                                                                                                                                            , new( var( "ps_ADT1" )
                                                                                                                                                                                 , metadata( 33
                                                                                                                                                                                           , 19
                                                                                                                                                                                           , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                           , "this is a string" ) ) ) )
                                                                                                                                                                , define( None
                                                                                                                                                                        , [ "ps_$__unused" ]
                                                                                                                                                                        , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                      , "discard" )
                                                                                                                                                                                                            , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                      , "discardUnit" ) )
                                                                                                                                                                                                      , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                , "bindEffect" ) )
                                                                                                                                                                                                , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                , "println" )
                                                                                                                                                                                                      , new( var( "ps_ADT2" )
                                                                                                                                                                                                           , metadata( 34
                                                                                                                                                                                                                     , 19
                                                                                                                                                                                                                     , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                     , 1 )
                                                                                                                                                                                                           , metadata( 34
                                                                                                                                                                                                                     , 21
                                                                                                                                                                                                                     , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                     , 2.0 ) ) ) )
                                                                                                                                                                                          , define( None
                                                                                                                                                                                                  , [ "ps_$__unused" ]
                                                                                                                                                                                                  , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                , "discard" )
                                                                                                                                                                                                                                      , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                , "discardUnit" ) )
                                                                                                                                                                                                                                , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                          , "bindEffect" ) )
                                                                                                                                                                                                                          , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                          , "println" )
                                                                                                                                                                                                                                , new( var( "ps_ADT3" )
                                                                                                                                                                                                                                     , metadata( 35
                                                                                                                                                                                                                                               , 19
                                                                                                                                                                                                                                               , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                               , record( ( "x"
                                                                                                                                                                                                                                                         , metadata( 35
                                                                                                                                                                                                                                                                   , 24
                                                                                                                                                                                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                   , 22 ) )
                                                                                                                                                                                                                                                       , ( "y"
                                                                                                                                                                                                                                                         , metadata( 35
                                                                                                                                                                                                                                                                   , 32
                                                                                                                                                                                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                   , 33 ) ) ) ) ) ) )
                                                                                                                                                                                                                    , define( None
                                                                                                                                                                                                                            , [ "ps_$__unused" ]
                                                                                                                                                                                                                            , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                          , "discard" )
                                                                                                                                                                                                                                                                , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                          , "discardUnit" ) )
                                                                                                                                                                                                                                                          , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                                                    , "bindEffect" ) )
                                                                                                                                                                                                                                                    , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                                                    , "println" )
                                                                                                                                                                                                                                                          , new( var( "ps_ADT3" )
                                                                                                                                                                                                                                                               , metadata( 36
                                                                                                                                                                                                                                                                         , 22
                                                                                                                                                                                                                                                                         , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                         , record( ( "x"
                                                                                                                                                                                                                                                                                   , metadata( 36
                                                                                                                                                                                                                                                                                             , 27
                                                                                                                                                                                                                                                                                             , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                             , 22 ) )
                                                                                                                                                                                                                                                                                 , ( "y"
                                                                                                                                                                                                                                                                                   , metadata( 36
                                                                                                                                                                                                                                                                                             , 35
                                                                                                                                                                                                                                                                                             , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                             , 33 ) ) ) ) ) ) )
                                                                                                                                                                                                                                              , define( None
                                                                                                                                                                                                                                                      , [ "ps_$__unused" ]
                                                                                                                                                                                                                                                      , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                    , "discard" )
                                                                                                                                                                                                                                                                                          , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                    , "discardUnit" ) )
                                                                                                                                                                                                                                                                                    , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                                                                              , "bindEffect" ) )
                                                                                                                                                                                                                                                                              , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                                                                              , "println" )
                                                                                                                                                                                                                                                                                    , metadata( 38
                                                                                                                                                                                                                                                                                              , 13
                                                                                                                                                                                                                                                                                              , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                              , "parametric adts:" ) ) )
                                                                                                                                                                                                                                                                        , define( None
                                                                                                                                                                                                                                                                                , [ "ps_$__unused" ]
                                                                                                                                                                                                                                                                                , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                                              , "discard" )
                                                                                                                                                                                                                                                                                                                    , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                                              , "discardUnit" ) )
                                                                                                                                                                                                                                                                                                              , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                                                                                                        , "bindEffect" ) )
                                                                                                                                                                                                                                                                                                        , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                                                                                                        , "println" )
                                                                                                                                                                                                                                                                                                              , new( var( "ps_PADT1" )
                                                                                                                                                                                                                                                                                                                   , metadata( 39
                                                                                                                                                                                                                                                                                                                             , 20
                                                                                                                                                                                                                                                                                                                             , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                             , "this is a string" ) ) ) )
                                                                                                                                                                                                                                                                                                  , define( None
                                                                                                                                                                                                                                                                                                          , [ "ps_$__unused" ]
                                                                                                                                                                                                                                                                                                          , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                                                                        , "discard" )
                                                                                                                                                                                                                                                                                                                                              , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                                                                        , "discardUnit" ) )
                                                                                                                                                                                                                                                                                                                                        , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                                                                                                                                  , "bindEffect" ) )
                                                                                                                                                                                                                                                                                                                                  , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                                                                                                                                  , "println" )
                                                                                                                                                                                                                                                                                                                                        , new( var( "ps_PADT2" )
                                                                                                                                                                                                                                                                                                                                             , metadata( 40
                                                                                                                                                                                                                                                                                                                                                       , 20
                                                                                                                                                                                                                                                                                                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                       , 1 )
                                                                                                                                                                                                                                                                                                                                             , metadata( 40
                                                                                                                                                                                                                                                                                                                                                       , 22
                                                                                                                                                                                                                                                                                                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                       , 2.0 ) ) ) )
                                                                                                                                                                                                                                                                                                                            , define( None
                                                                                                                                                                                                                                                                                                                                    , [ "ps_$__unused" ]
                                                                                                                                                                                                                                                                                                                                    , block( ret( call( call( call( call( get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                                                                                                  , "discard" )
                                                                                                                                                                                                                                                                                                                                                                        , get_item( var( "ps_Control_Bind" )
                                                                                                                                                                                                                                                                                                                                                                                  , "discardUnit" ) )
                                                                                                                                                                                                                                                                                                                                                                  , get_item( var( "ps_Effect" )
                                                                                                                                                                                                                                                                                                                                                                            , "bindEffect" ) )
                                                                                                                                                                                                                                                                                                                                                            , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                                                                                                                                                            , "println" )
                                                                                                                                                                                                                                                                                                                                                                  , new( var( "ps_PADT3" )
                                                                                                                                                                                                                                                                                                                                                                       , metadata( 41
                                                                                                                                                                                                                                                                                                                                                                                 , 20
                                                                                                                                                                                                                                                                                                                                                                                 , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                 , record( ( "x"
                                                                                                                                                                                                                                                                                                                                                                                           , metadata( 41
                                                                                                                                                                                                                                                                                                                                                                                                     , 25
                                                                                                                                                                                                                                                                                                                                                                                                     , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                     , 22 ) )
                                                                                                                                                                                                                                                                                                                                                                                         , ( "y"
                                                                                                                                                                                                                                                                                                                                                                                           , metadata( 41
                                                                                                                                                                                                                                                                                                                                                                                                     , 33
                                                                                                                                                                                                                                                                                                                                                                                                     , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                     , 33 ) )
                                                                                                                                                                                                                                                                                                                                                                                         , ( "z"
                                                                                                                                                                                                                                                                                                                                                                                           , metadata( 41
                                                                                                                                                                                                                                                                                                                                                                                                     , 41
                                                                                                                                                                                                                                                                                                                                                                                                     , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                     , 2 ) ) ) ) ) ) )
                                                                                                                                                                                                                                                                                                                                                      , define( None
                                                                                                                                                                                                                                                                                                                                                              , [ "ps_$__unused" ]
                                                                                                                                                                                                                                                                                                                                                              , block( ret( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                                                                                                                                                                                                                                          , "println" )
                                                                                                                                                                                                                                                                                                                                                                                , metadata( 42
                                                                                                                                                                                                                                                                                                                                                                                          , 17
                                                                                                                                                                                                                                                                                                                                                                                          , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                          , record( ( "it"
                                                                                                                                                                                                                                                                                                                                                                                                    , new( var( "ps_PADT3" )
                                                                                                                                                                                                                                                                                                                                                                                                         , metadata( 42
                                                                                                                                                                                                                                                                                                                                                                                                                   , 29
                                                                                                                                                                                                                                                                                                                                                                                                                   , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                                   , record( ( "x"
                                                                                                                                                                                                                                                                                                                                                                                                                             , metadata( 42
                                                                                                                                                                                                                                                                                                                                                                                                                                       , 34
                                                                                                                                                                                                                                                                                                                                                                                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                                                       , 22 ) )
                                                                                                                                                                                                                                                                                                                                                                                                                           , ( "y"
                                                                                                                                                                                                                                                                                                                                                                                                                             , metadata( 42
                                                                                                                                                                                                                                                                                                                                                                                                                                       , 42
                                                                                                                                                                                                                                                                                                                                                                                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                                                       , 33 ) )
                                                                                                                                                                                                                                                                                                                                                                                                                           , ( "z"
                                                                                                                                                                                                                                                                                                                                                                                                                             , metadata( 42
                                                                                                                                                                                                                                                                                                                                                                                                                                       , 49
                                                                                                                                                                                                                                                                                                                                                                                                                                       , "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs"
                                                                                                                                                                                                                                                                                                                                                                                                                                       , 2 ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("A", var("ps_A"))
                           , ("B", var("ps_B"))
                           , ("C", var("ps_C"))
                           , ("ADT1", var("ps_ADT1"))
                           , ("ADT2", var("ps_ADT2"))
                           , ("ADT3", var("ps_ADT3"))
                           , ("F", var("ps_F"))
                           , ("PADT1", var("ps_PADT1"))
                           , ("PADT2", var("ps_PADT2"))
                           , ("PADT3", var("ps_PADT3"))
                           , ("PF", var("ps_PF"))
                           , ("main", var("ps_main")) ) ) )
res = module_code(res, filename="C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes\\src\\Main.purs", name="datatypes.Main.pure")
