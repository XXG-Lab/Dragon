Dragon
======

Some exercises in the dragon book second edition.

# Summary

* 1 Introduction
    * [1.1 Language Processors](01/1.1.ipynb)
    * 1.2 The Structure of a Compiler
    * [1.3 The Evolution of Programming Languages](01/1.3.ipynb)
    * 1.4 The Science of Building a Compiler
    * 1.5 Applications of Compiler Technology
    * [1.6 Programming Language Basics](01/1.6.ipynb)
* 2 A Simple Syntax-Directed Translator
    * 2.1 Introduction
    * [2.2 Syntax Definition](02/2.2.ipynb)
    * [2.3 Syntax-Directed Translation](02/2.3.ipynb)
    * [2.4 Parsing](02/2.4.ipynb)
    * 2.5 A Translator for Simple Expression
    * [2.6 Lexical Analysis](02/2.6.ipynb)
    * 2.7 Symbol Tables
    * [2.8 Intermediate Code Generation](02/2.8.ipynb)
* 3 Lexical Analysis
    * [3.1 The Role of the Lexical Analyzer](03/3.1.ipynb)
    * 3.2 Input Buffering
    * [3.3 Specification of Tokens](03/3.3.ipynb)
    * [3.4 Recognition of Tokens](03/3.4.ipynb)
    * [3.5 The Lexical-Analyzer Generator Lex](03/3.5.ipynb)
    * [3.6 Finite Automata](03/3.6.ipynb)
    * [3.7 From Regular Expressions to Automata](03/3.7.ipynb)
    * [3.8 Design of a Lexical-Analyzer Generator](03/3.8.ipynb)
    * [3.9 Optimization of DFA-Based Pattern Matches](03/3.9.ipynb)
* 4 Syntax Analysis
    * 4.1 Introduction
    * [4.2 Context-Free Grammars](04/4.2.ipynb)
    * [4.3 Writing a Grammar](04/4.3.ipynb)
    * [4.4 Top-Down Parsing](04/4.4.ipynb)
    * [4.5 Bottom-Up Parsing](04/4.5.ipynb)
    * [4.6 Introduction to LR Parsing: Simple LR](04/4.6.ipynb)
    * [4.7 More Powerful LR Parsers](04/4.7.ipynb)
    * [4.8 Using Ambiguous Grammars](04/4.8.ipynb)
    * [4.9 Parser Generators](04/4.9.ipynb)
* 5 Syntax-Directed Translation
    * [5.1 Syntax-Directed Definitions](05/5.1.ipynb)
    * [5.2 Evaluation Orders for SDD's](05/5.2.ipynb)
    * [5.3 Applications of Syntax-Directed Translation](05/5.3.ipynb)
    * [5.4 Syntax-Directed Translation Schemes](05/5.4.ipynb)
    * [5.5 Implementing L-Attributed SDD's](05/5.5.ipynb)
* 6 Intermediate-Code Generation
    * [6.1 Variants of Syntax Trees](06/6.1.ipynb)
    * [6.2 Three-Address Code](06/6.2.ipynb)
    * [6.3 Types and Declarations](06/6.3.ipynb)
    * [6.4 Translation of Expressions](06/6.4.ipynb)
    * [6.5 Type Checking](06/6.5.ipynb)
    * [6.6 Control Flow](06/6.6.ipynb)
    * [6.7 Backpatching](06/6.7.ipynb)
    * 6.8 Switch-Statements
    * 6.9 Intermediate Code for Procedures
* 7 Run-Time Environments
    * 7.1 Storage Organization
    * [7.2 Stack Allocation of Space](07/7.2.ipynb)
    * [7.3 Access to Nonlocal Data on the Stack](07/7.3.ipynb)
    * [7.4 Heap Management](07/7.4.ipynb)
    * [7.5 Introduction to Garbage Collection](07/7.5.ipynb)
    * [7.6 Introduction to Trace-Based Collection](07/7.6.ipynb)
    * [7.7 Short-Pause Garbage Collection](07/7.7.ipynb)
    * 7.8 Advanced Topics in Garbage Collection
* 8 Code Generation
    * 8.1 Issues in the Design of a Code Generator
    * [8.2 The Target Language](08/8.2.ipynb)
    * [8.3 Addresses in the Target Code](08/8.3.ipynb)
    * [8.4 Basic Blocks and Flow Graphs](08/8.4.ipynb)
    * [8.5 Optimization of Basic Blocks](08/8.5.ipynb)
    * [8.6 A Simple Code Generator](08/8.6.ipynb)
    * 8.7 Peephole Optimization
    * [8.8 Register Allocation and Assignment](08/8.8.ipynb)
    * [8.9 Instruction Selection by Tree Rewriting](08/8.9.ipynb)
    * [8.10 Optimal Code Generation for Expressions](08/8.10.ipynb)
    * 8.11 Dynamic Programming Code-Generation
* 9 Machine-Independent Optimizations
    * [9.1 The Principal Sources of Optimization](09/9.1.ipynb)
    * [9.2 Introduction to Data-Flow Analysis](09/9.2.ipynb)
    * [9.3 Foundations of Data-Flow Analysis](09/9.3.ipynb)
    * [9.4 Constant Propagation](09/9.4.ipynb)
    * [9.5 Partial-Redundancy Elimination](09/9.5.ipynb)
    * [9.6 Loops in Flow Graphs](09/9.6.ipynb)
    * [9.7 Region-Based Analysis](09/9.7.ipynb)
    * [9.8 Symbolic Analysis](09/9.8.ipynb)
* 10 Instruction-Level Parallelism
    * 10.1 Processor Architectures
    * [10.2 Code-Scheduling Constraints](10/10.2.ipynb)
    * [10.3 Basic-Block Scheduling](10/10.3.ipynb)
    * [10.4 Global Code Scheduling](10/10.4.ipynb)
    * [10.5 Software Pipelining](10/10.5.ipynb)
* 11 Optimizing for Parallelism and Locality
    * 11.1 Basic Concepts
    * [11.2 Matrix Multiply: An In-Depth Example](11/11.2.ipynb)
    * [11.3 Iteration Spaces](11/11.3.ipynb)
    * [11.4 Affine Array Indexes](11/11.4.ipynb)
    * [11.5 Data Reuse](11/11.5.ipynb)
    * [11.6 Array Data-Dependence Analysis](11/11.6.ipynb)
    * 11.7 Finding Synchronization-Free Parallelism
    * 11.8 Synchronization Between Parallel Loops
    * 11.9 Pipelining
    * 11.10 Locality Optimizations
    * 11.11 Other Uses of Affine Transforms
* 12 Interprocedural Analysis
    * 12.1 Basic Concepts
    * 12.2 Why Interprocedural Analysis?
    * 12.3 A Logical Representation of Data Flow
    * 12.4 A Simple Pointer-Analysis Algorithm
    * 12.5 Context-Insensitive Interprocedural Analysis
    * 12.6 Context-Sensitive Pointer Analysis
    * 12.7 Datalog Implementation by BDD's