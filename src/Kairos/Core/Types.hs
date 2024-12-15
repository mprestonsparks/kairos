{-|
Module      : Kairos.Core.Types
Description : Core types for the Kairos HoTT implementation
Copyright   : (c) Kairos Team, 2024
License     : MIT

Core type definitions for Kairos, implementing HoTT primitives and pattern system foundations.
-}
module Kairos.Core.Types
    ( -- * HoTT Types
      Type(..)
    , Term(..)
    , Path(..)
      -- * Pattern System
    , Pattern(..)
    , Evidence(..)
    ) where

import GHC.Generics (Generic)
import Data.Text (Text)

-- | Represents HoTT types in our system
data Type
    = Universe Int           -- ^ Universe at level n
    | Pi Type Type          -- ^ Dependent function type
    | Sigma Type Type       -- ^ Dependent pair type
    | Path Type Term Term   -- ^ Path type between terms
    deriving (Show, Eq, Generic)

-- | Terms in our type theory
data Term
    = Var Text              -- ^ Variables
    | Lambda Text Term      -- ^ Lambda abstractions
    | App Term Term         -- ^ Function application
    | Pair Term Term        -- ^ Pairs
    | Refl Term            -- ^ Reflexivity proof
    deriving (Show, Eq, Generic)

-- | Path types for homotopy
data Path
    = PathRefl Term         -- ^ Reflexivity path
    | PathSym Path          -- ^ Path symmetry
    | PathTrans Path Path   -- ^ Path transitivity
    deriving (Show, Eq, Generic)

-- | Pattern representation
data Pattern
    = AtomicPattern Text              -- ^ Basic pattern
    | CompositePattern [Pattern]      -- ^ Composite pattern
    | TypedPattern Pattern Type       -- ^ Pattern with type annotation
    deriving (Show, Eq, Generic)

-- | Evidence for pattern matching
data Evidence
    = DirectEvidence Term             -- ^ Direct term evidence
    | IndirectEvidence [Evidence]     -- ^ Composite evidence
    | PathEvidence Path              -- ^ Path-based evidence
    deriving (Show, Eq, Generic)
