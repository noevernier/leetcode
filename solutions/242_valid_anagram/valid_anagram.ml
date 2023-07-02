open String;;

let rec valid_anagram (s: string) (t: string) : bool =
  let s_length = String.length s in
  let t_length = String.length t in
  if s_length <> t_length then false
  else
    let s_counter = Array.make 256 0 in
    let t_counter = Array.make 256 0 in
    for i = 0 to s_length - 1 do
      s_counter.(int_of_char s.[i]) <- s_counter.(int_of_char s.[i]) + 1;
      t_counter.(int_of_char t.[i]) <- t_counter.(int_of_char t.[i]) + 1
    done;
    let is_anagram = ref true in
    for i = 0 to 255 do
      if s_counter.(i) <> t_counter.(i) then is_anagram := false
    done;
    !is_anagram