use std::env;
use std::fs;
use std::path::PathBuf;
use std::error::Error;

#[must_use]
pub fn read_input() -> Result<String, Box<dyn Error>> {
    // Assume crate root is `.../template/rust/template` and example.txt lives at `.../template/example.txt`.
    let cwd: PathBuf = env::current_dir()?;
    // Go up two levels to reach the `template` directory that contains `example.txt`.
    let example_path = cwd
        .parent()
        .and_then(|p| p.parent())
        .map(|p| p.join("example.txt"))
        .ok_or("could not determine example file path")?;

    // canonicalize so relative `..` are resolved (optional)
    let example_path = fs::canonicalize(example_path)?;
    let contents = fs::read_to_string(example_path)?;
    Ok(contents)
}