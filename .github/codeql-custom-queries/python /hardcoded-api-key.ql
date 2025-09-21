/**
 * @name Hardcoded API Key in Python
 * @description Detects hardcoded API keys and secrets.
 * @kind problem
 * @problem.severity error
 * @id py/hardcoded-api-key
 * @tags security, external/cwe/cwe-798
 */

import python

predicate isSensitiveAssignment(Assign a) {
  exists(Constant c |
    c = a.getRhs() and
    c.getValue().regexpMatch("DUMMY_SECRET_KEY_[A-Za-z0-9]+")
  )
}

from Assign a, Variable v
where
  isSensitiveAssignment(a) and
  v = a.getAnAssignedVariable()
select a, "Hardcoded API key assigned to variable '" + v.getName() + "'."
