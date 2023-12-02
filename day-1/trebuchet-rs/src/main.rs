use std::{collections::HashMap, fs};

fn digit_to_word(digit: &str) -> String {
    match digit {
        "0" => "zero",
        "1" => "one",
        "2" => "two",
        "3" => "three",
        "4" => "four",
        "5" => "five",
        "6" => "six",
        "7" => "seven",
        "8" => "eight",
        "9" => "nine",
        _ => digit,
    }
    .to_string()
}

fn main() {
    let file_name = "input2.txt";
    let contents = fs::read_to_string(file_name).expect("Should have been able to read file");

    // This maps the string form of a number to an i32
    // Ex. "five" -> 5
    let number_map: HashMap<&str, &str> = vec![
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]
    .into_iter()
    .collect();

    let mut sum = 0;

    for line in contents.split("\n") {
        println!("{line}");

        let mapped_line: String = line
            .chars()
            .map(|c| digit_to_word(c.to_string().as_str()))
            .collect();

        let mut values: Vec<&str> = vec![];
        for idx in 0..mapped_line.len() {
            let mut word: Vec<char> = vec![];
            for next in mapped_line.chars().skip(idx) {
                word.push(next);
                let cur_word: String = word.iter().collect();
                let word_str = cur_word.as_str();
                match number_map.get(word_str) {
                    Some(&value) => {
                        print!("{word_str} ");
                        values.push(value);
                        break;
                    }
                    None => continue,
                }
            }
        }
        println!();
        if values.len() > 1 {
            let result_str: String = values[0].to_string() + &values[values.len() - 1].to_string();
            println!("{result_str}");
            let result: i32 = result_str.parse::<i32>().unwrap();
            sum = sum + result;
        } else if values.len() > 0 {
            let result_str: String = values[0].to_string() + &values[0].to_string();
            println!("{result_str}");
            let result: i32 = result_str.parse::<i32>().unwrap();
            sum = sum + result;
        } else {
            println!("BLARG");
        }
        println!("Current sum: {sum}");
    }
    println!("Done.");
}
