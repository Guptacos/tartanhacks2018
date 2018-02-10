Help on module qm:

NAME
    qm - Quine-McCluskey two-level logic minimization method.

FILE
    /home/dickrp/svn/support/python/qm/qm.py

DESCRIPTION
    Copyright 2008, Robert Dick <dickrp@eecs.umich.edu> with improvements
    from Pat Maupin <pmaupin@gmail.com>.
    
    Routines to compute the optimal sum of products implementation from sets of
    don't-care terms, minterms, and maxterms.
    
    Command-line usage example:
      qm.py -o1,2,5 -d0,7
    
    Library usage example:
      import qm
      print qm.qm(ones=[1, 2, 5], dc=[0, 7])
    
    Please see the license file for legal information.

FUNCTIONS
    active_primes(cubesel, primes)
        Return the primes selected by the cube selection integer.
    
    b2s(i, vars)
        Convert from an integer to a binary string.
    
    bitcount(s)
        Return the sum of on bits in s.
    
    compute_primes(cubes, vars)
        Compute primes for the given set of cubes and variable count.
    
    is_cover(prime, one)
        Return a bool: Does the prime cover the minterm?
    
    is_full_cover(all_primes, ones)
        Return a bool: Does the set of primes cover all minterms?
    
    merge(i, j)
        Return cube merge.  'X' is don't-care.  'None' if merge impossible.
    
    qm(ones=[], zeros=[], dc=[])
        Compute minimal two-level sum-of-products form.
        Arguments are:
                ones: iterable of integer minterms
                zeros: iterable of integer maxterms
                dc: iterable of integers specifying don't-care terms
        
        For proper operation, either (or both) the 'ones' and 'zeros'
        parameters must be specified.  If one of these parameters is not
        specified, it will be computed from the combination of the other
        parameter and the optional 'dc' parameter.
        
        An assertion error will be raised if any terms are specified
        in more than one argument, or if all three arguments are given
        and not all terms are specified.
    
    unate_cover(primes, ones)
        Return the minimal cardinality subset of primes covering all ones.
        
        Exhaustive for now.  Feel free to replace this with an efficient unate
        covering problem solver.

DATA
    __author__ = 'Robert Dick'
    __author_email__ = 'dickrp@eecs.umich.edu'
    __version__ = '0.2'

VERSION
    0.2

AUTHOR
    Robert Dick


