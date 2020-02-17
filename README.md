# Datatypes

## Requisite

1. The same as [Hello World of PureScript-Python](https://github.com/Testing-PureScript-Python/hello-world).
2. As in this project we have 2 modules(`Main`, `SmallPrelude`), to keep the first-class IDE experiment,
   in VSCode, open `File -> Preferences -> Settings`, input `purescript` and search, turn on the option `Add Spago Sources`.

## Notes

```purescript

module Main where

import SmallPrelude

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

main :: IO {}
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
```

Currently we don't have pretty print as we have no standard library now,
so we just use python's `print`(`println` in our program) to show its
internal data:

```
enums:
{'.t': <function ps_A at 0x0000024D1397AC18>}
{'.t': <function ps_B at 0x0000024D1397A0D8>}
{'.t': <function ps_C at 0x0000024D139B1438>}
ordinary adts:
{'.t': <function ps_ADT1 at 0x0000024D139B13A8>, 'value0': 'this is a string'}
{'.t': <function ps_ADT2 at 0x0000024D139B1318>, 'value0': 1, 'value1': 2.0}
{'.t': <function ps_ADT3 at 0x0000024D139B1288>, 'value0': {'x': 22, 'y': 33}}
{'.t': <function ps_ADT3 at 0x0000024D139B1288>, 'value0': {'x': 22, 'y': 33}}
parametric adts:
{'.t': <function ps_PADT1 at 0x0000024D13980AF8>, 'value0': 'this is a string'}
{'.t': <function ps_PADT2 at 0x0000024D13980678>, 'value0': 1, 'value1': 2.0}
{'.t': <function ps_PADT3 at 0x0000024D1397C318>, 'value0': {'x': 22, 'y': 33, 'z': 2}}
{'it': {'.t': <function ps_PADT3 at 0x0000024D1397C318>, 'value0': {'x': 22, 'y': 33, 'z': 2}}}
```