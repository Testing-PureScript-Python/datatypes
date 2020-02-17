module SmallPrelude where

data IO a

foreign import println :: forall a. a -> IO {}
foreign import discard :: forall a b. IO a -> (a -> IO b) -> IO b