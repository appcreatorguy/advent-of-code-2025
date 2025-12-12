mod utils;

use std::error::Error;

pub fn part_one(_input: &str) -> Result<u64, Box<dyn Error>> {
    Ok(0)
}

pub fn part_two(_input: &str) -> Result<u64, Box<dyn Error>> {
        Ok(0)
}

fn print_result_or_exit(res: Result<u64, Box<dyn Error>>) {
    match res {
        Ok(v) => {
            // Print only the numeric result to stdout, nothing else.
            println!("{}", v);
            std::process::exit(0);
        }
        Err(_) => std::process::exit(1),
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();

    // Usage: `cargo run -- solve 1` or `cargo run -- solve 2`
    if args.len() >= 2 && args[1] == "solve" {
        let part = args.get(2).map(|s| s.as_str()).unwrap_or("");
        let input = match utils::read_input() {
            Ok(s) => s,
            Err(_) => std::process::exit(1),
        };

        match part {
            "1" => print_result_or_exit(part_one(&input)),
            "2" => print_result_or_exit(part_two(&input)),
            _ => std::process::exit(1),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = crate::utils::read_input().expect("failed to read example input");
        let result = part_one(&input).expect("part_one failed");
        assert_eq!(result, 0);
    }

    #[test]
    fn test_part_two() {
        let input = crate::utils::read_input().expect("failed to read example input");
        let result = part_two(&input).expect("part_two failed");
        assert_eq!(result, 0);
    }
}