# nameless!

A lambda calculus interpreter written in Python. Lambda calculus is a
minimal, turing complete programming language. In lambda calculus,
everything is an anonymous (i.e. nameless :wink:) function. This
project has no depencencies outside of the standard library.

## Execution

1. Clone this repository:
    ```
    git clone https://github.com/ElliotPenson/nameless.git
    ```

2. Move into the newly created directory:

    ```
    cd nameless
    ```

3. Run the `nameless` package:
    ```
    python nameless
    ```

## Grammar

```
Expression  -> Variable | Application | Abstraction
Variable    -> ID
Application -> (Expression Expression)
Abstraction -> λID.Expression
```

An **abstraction** `λx.e` is a definition of an anonymous function
capable of taking a single input `x` and substituting it into (and
thus evaluating) the expression `e`.  An **application** `(e1 e2)`
applies the `e1` function to the `e2` value, that is, it represents
the act of calling function `e1` on input `e2`.

Note that the at-sign (`@`) may be used instead of lambda (`λ`) to
denote an abstraction.

## Features

Execution follows *normal order reduction*. This means that the
outmost lambda expression is always applied first. The interpreter
displays each reduction step on a different line:


```
> (λm.((m λt.λf.t) λx.λt.λf.f) λz.λs.z)
((λz.λs.z λt.λf.t) λx.λt.λf.f)
(λs.λt.λf.t λx.λt.λf.f)
λt.λf.t
```

Syntax errors are nicely displayed to user:

```
> λx
ParseError: Expected: ., Found: EOF
```

During α-conversion, the interpreter has the capability to rename
variables to avoid variable capture:

```
> (λx.λy.(x y) y)
λa.(y a)
```
