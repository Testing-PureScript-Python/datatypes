module SmallPrelude where

import Effect
import Prelude
import Effect.Console

foreign import showAny :: forall a. a -> String

println = log <<< showAny
