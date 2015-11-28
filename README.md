# nameless

A lambda calculus interpreter written in Python. Lambda calculus is a
minimal, turing complete programming language. In lambda calculus,
everything is an anonymous (i.e. nameless :wink:) function.

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
