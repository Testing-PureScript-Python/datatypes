module Main where

import SmallPrelude

data MyEnum = A | B | C

-- ADT is abbr for algebraic data types
data MyADT -- this is the type declaration
    = ADT1 String
    | ADT2 Int Number
    | ADT3 { x :: Int, y :: Int }


main :: IO {}
main = do
    println A
    println B
    println C

    println (ADT1 "this is a string")
    println (ADT2 1 2.0)
    println (ADT3 {x : 22, y : 33})

