pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = std::collections::HashMap::new();
    for (i, &num) in nums.iter().enumerate() {
        let complement = target - num;
        if map.contains_key(&complement) {
            return vec![*map.get(&complement).unwrap() as i32, i as i32];
        }
        map.insert(num, i);
    }
    vec![]
}