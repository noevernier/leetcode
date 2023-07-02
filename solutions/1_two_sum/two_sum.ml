let rec find (x : int) (l : int list) : int option =
  match l with
  | [] -> None
  | hd :: tl -> if hd = x then Some x else find x tl;;

let rec get_index (x : int) (l : int list) : int =
  match l with
  | [] -> failwith "Not found"
  | hd :: tl -> if hd = x then 0 else 1 + get_index x tl;;

let rec two_sum (l : int list) (target : int) : (int * int) option =
  match l with
  | [] -> None
  | hd :: tl -> (
      match find (target - hd) tl with
      | None -> two_sum tl target
      | Some x -> Some (get_index hd l, get_index x l) );;