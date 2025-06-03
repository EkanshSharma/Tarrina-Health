# Tarrina-Health
Take Home Assignment- Backend Developer

Problem 01: Happy Meeting Days
  
    Time complexity: O(nlog⁡n)
    Space complexity: O(n)
  Real World: Agreedy approach would try to schedule meetings one by one, moving them just enough to avoid conflicts. It works well in most cases. This approach however has some constraints-
      Choose a time that works right now, but causes problems later.
      Miss a better overall arrangement that uses fewer days.
  For an overall best approach, we could define constraints such as meetings must not overlap on the same day and each meeting must be within ±k minutes of its original time. The solver would through all possible combinations that satisfy the rules. This will be a slower but much more accurate solution.

Scale: To handle millions of meetings across time zones, split the problem by region, use distributed scheduling, and apply fast heuristics with small time shifts to reduce conflicts. Store times in UTC and use efficient data structures for availability checks. For complex cases, apply optimization or machine learning selectively.

