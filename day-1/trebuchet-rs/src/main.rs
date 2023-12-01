use std::fs;

fn main() {
    let file_name = "input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Should have been able to read file");

    println!("{contents}");
}
