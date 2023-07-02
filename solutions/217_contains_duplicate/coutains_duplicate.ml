let rec contains_duplicate nums =
  match nums with
  | [] -> false
  | x :: xs -> List.mem x xs || contains_duplicate xs;;