use std::{fs, collections::HashMap};

fn main() {
    let file_name = "input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Should have been able to read file");

    // TODO: Add mapping for string version of numbers
    // Ex. "five" -> 5
    static NUMBERS: &[&str; 10] = &[
       "zero", 
       "one", 
       "two", 
       "three", 
       "four", 
       "five", 
       "six", 
       "seven", 
       "eight", 
       "nine", 
    ];

    let number_map: HashMap<&str, i32> = vec![
        ("zero", 0),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9)
    ].into_iter().collect();

    let mut numbers: Vec<i32> = vec![];

    for line in contents.split("\n") {
        
        let _numbers: String = line
            .chars()
            .filter(|x| x.is_digit(10))
            .collect();

        if _numbers.len() > 1 {
            let _final_char_idx = _numbers.len() - 1;
            let _result = [&_numbers[0..1], &_numbers[_final_char_idx..]].to_owned().join("");
            println!("{_result}");
            numbers.push(_result.parse::<i32>().unwrap());
        } else if _numbers.len() > 0 {
            let _result = &_numbers[0..1].to_owned();
            println!("{_result}");
            numbers.push(_result.parse::<i32>().unwrap());
        }
    }

    let total: i32 = numbers.iter().sum();
    println!("{total}");
}
