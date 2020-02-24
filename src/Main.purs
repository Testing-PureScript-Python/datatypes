module Main where

import SmallPrelude
import Effect
import Prelude

data MyEnum = A | B | C

-- ADT is abbr for algebraic data types
data MyADT -- this is the type declaration
    = ADT1 String
    | ADT2 Int Number
    | ADT3 { x :: Int, y :: Int }

newtype F = F MyADT

data MyParametricADT a -- this is the type declaration
    = PADT1 a
    | PADT2 Int Number
    | PADT3 { x :: Int, y :: Int, z :: a }

newtype PF a = PF {it :: MyParametricADT a}

main :: Effect Unit
main = do
    println("enums:")
    println A
    println B
    println C
    
    println("ordinary adts:")
    println (ADT1 "this is a string")
    println (ADT2 1 2.0)
    println (ADT3 {x : 22, y : 33})
    println (F (ADT3 {x : 22, y : 33}))

    println("parametric adts:")
    println (PADT1 "this is a string")
    println (PADT2 1 2.0)
    println (PADT3 {x : 22, y : 33, z : 2})
    println (PF {it : PADT3 {x : 22, y : 33, z: 2}})
