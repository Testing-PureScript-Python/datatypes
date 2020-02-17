from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as _joinpath
def joinpath(a, b):
    global joinpath, __file__
    joinpath = _joinpath
    __file__ = _joinpath(a, b)
    return __file__
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\datatypes"
res = block( "No document"
           , assign( "ps_SmallPrelude"
                   , call( var('import_module')
                         , "datatypes.SmallPrelude.purescript_impl" ) )
           , assign( "ps_A"
                   , block( define("ps_A", [], block(this))
                          , set_attr(var("ps_A"), "value", new(var("ps_A")))
                          , var("ps_A") ) )
           , assign( "ps_B"
                   , block( define("ps_B", [], block(this))
                          , set_attr(var("ps_B"), "value", new(var("ps_B")))
                          , var("ps_B") ) )
           , assign( "ps_C"
                   , block( define("ps_C", [], block(this))
                          , set_attr(var("ps_C"), "value", new(var("ps_C")))
                          , var("ps_C") ) )
           , assign( "ps_ADT1"
                   , define( "ps_ADT1"
                           , ["ps_value0"]
                           , block( set_item(this, "value0", var("ps_value0"))
                                  , ret(this) ) ) )
           , assign( "ps_ADT2"
                   , define( "ps_ADT2"
                           , ["ps_value0", "ps_value1"]
                           , block( set_item(this, "value0", var("ps_value0"))
                                  , set_item(this, "value1", var("ps_value1"))
                                  , ret(this) ) ) )
           , assign( "ps_ADT3"
                   , define( "ps_ADT3"
                           , ["ps_value0"]
                           , block( set_item(this, "value0", var("ps_value0"))
                                  , ret(this) ) ) )
           , assign( "ps_main"
                   , call( call( get_item(var("ps_SmallPrelude"), "discard")
                               , call( get_item( var("ps_SmallPrelude")
                                               , "println" )
                                     , get_attr(var("ps_A"), "value") ) )
                         , define( None
                                 , ["ps_$__unused"]
                                 , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                   , "discard" )
                                                         , call( get_item( var( "ps_SmallPrelude" )
                                                                         , "println" )
                                                               , get_attr( var( "ps_B" )
                                                                         , "value" ) ) )
                                                   , define( None
                                                           , ["ps_$__unused"]
                                                           , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                                             , "discard" )
                                                                                   , call( get_item( var( "ps_SmallPrelude" )
                                                                                                   , "println" )
                                                                                         , get_attr( var( "ps_C" )
                                                                                                   , "value" ) ) )
                                                                             , define( None
                                                                                     , [ "ps_$__unused" ]
                                                                                     , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                       , "discard" )
                                                                                                             , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                             , "println" )
                                                                                                                   , new( var( "ps_ADT1" )
                                                                                                                        , metadata( 20
                                                                                                                                  , 19
                                                                                                                                  , joinpath( project_path
                                                                                                                                  , "src\\Main.purs" )
                                                                                                                                  , "this is a string" ) ) ) )
                                                                                                       , define( None
                                                                                                               , [ "ps_$__unused" ]
                                                                                                               , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                 , "discard" )
                                                                                                                                       , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                       , "println" )
                                                                                                                                             , new( var( "ps_ADT2" )
                                                                                                                                                  , metadata( 21
                                                                                                                                                            , 19
                                                                                                                                                            , joinpath( project_path
                                                                                                                                                            , "src\\Main.purs" )
                                                                                                                                                            , 1 )
                                                                                                                                                  , metadata( 21
                                                                                                                                                            , 21
                                                                                                                                                            , joinpath( project_path
                                                                                                                                                            , "src\\Main.purs" )
                                                                                                                                                            , 2.0 ) ) ) )
                                                                                                                                 , define( None
                                                                                                                                         , [ "ps_$__unused" ]
                                                                                                                                         , block( ret( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                                     , "println" )
                                                                                                                                                           , new( var( "ps_ADT3" )
                                                                                                                                                                , metadata( 22
                                                                                                                                                                          , 19
                                                                                                                                                                          , joinpath( project_path
                                                                                                                                                                          , "src\\Main.purs" )
                                                                                                                                                                          , record( ( "x"
                                                                                                                                                                                    , metadata( 22
                                                                                                                                                                                              , 24
                                                                                                                                                                                              , joinpath( project_path
                                                                                                                                                                                              , "src\\Main.purs" )
                                                                                                                                                                                              , 22 ) )
                                                                                                                                                                                  , ( "y"
                                                                                                                                                                                    , metadata( 22
                                                                                                                                                                                              , 32
                                                                                                                                                                                              , joinpath( project_path
                                                                                                                                                                                              , "src\\Main.purs" )
                                                                                                                                                                                              , 33 ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("A", var("ps_A"))
                           , ("B", var("ps_B"))
                           , ("C", var("ps_C"))
                           , ("ADT1", var("ps_ADT1"))
                           , ("ADT2", var("ps_ADT2"))
                           , ("ADT3", var("ps_ADT3"))
                           , ("main", var("ps_main")) ) ) )
res = module_code(res, filename=__file__, name="datatypes.Main")
