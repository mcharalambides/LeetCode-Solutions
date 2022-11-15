SELECT id,
  CASE 
    WHEN p_id is null THEN 'Root'
    WHEN id IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'
    WHEN id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
  END AS type
FROM 
  Tree