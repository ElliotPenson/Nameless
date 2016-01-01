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
